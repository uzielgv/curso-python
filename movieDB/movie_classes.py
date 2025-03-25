import csv
import os
import hashlib
from datetime import datetime

class Actor:
    ''' Clase para manejar la información de un actor '''
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        self.id_estrella = int(id_estrella)
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.url_imagen = url_imagen
        self.username = username
    
    def to_dict(self):
        ''' Devuelve un diccionario con la información del actor '''
        return {
            'id_estrella':self.id_estrella,
            'nombre':self.nombre,
            'fecha_nacimiento':self.fecha_nacimiento,
            'ciudad_nacimiento':self.ciudad_nacimiento,
            'url_imagen':self.url_imagen,
            'username':self.username
        }

class Pelicula():
    '''  '''
    def __init__(self, id_pelicula, titulo_pelicula, fecha_lanzamiento, url_poster):
        self.id_pelicula = int(id_pelicula)
        self.titulo_pelicula = titulo_pelicula
        self.fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, "%Y-%m-%d").date()
        self.url_poster = url_poster

    def to_dict(self):
        ''' Devuelve un diccionario con la información de la película '''
        return {
            'id_pelicula':self.id_pelicula,
            'titulo_pelicula':self.titulo_pelicula,
            'fecha_lanzamiento':self.fecha_lanzamiento,
            'ciudad_nacimiento':self.ciudad_nacimiento,
            'url_poster':self.url_poster
        }
    
    def __str__(self):
        ''' Devuelve una representación en string de la película '''
        return f"{self.titulo_pelicula} ({self.fecha_lanzamiento.year})"

class Relacion:
    '''  '''
    def __init__(self, id_relacion, id_pelicula, id_estrella):
        self.id_relacion = int(id_relacion)
        self.id_pelicula = int(id_pelicula)
        self.id_estrella = int(id_estrella)
    
    def to_dict(self):
        '''  '''
        return {
            'id_relacion':self.id_relacion,
            'id_pelicula':self.id_pelicula,
            'id_estrella':self.id_estrella
        }

class User:
    def __init__(self, username, nombre_completo, email, password):
        ''''''
        self.username = username
        self.nombre_completo = nombre_completo
        self.email = email
        self.password = password
    
    def to_dict(self):
        '''   '''
        return {
            'username':self.username,
            'nombre_completo':self.nombre_completo,
            'email':self.email,
            'password':self.password
        }
    
    def hash_string(self, string):
        return hashlib.sha256(string.encode()).hexdigest()

class SistemaCine:
    def __init__(self):
        ''''''
        self.actores = {}
        self.peliculas = {}
        self.relaciones = {}
        self.usuarios = {}
        self.idx_actor = 0
        self.idx_pelicula = 0
        self.idx_relacion = 0
        self.usuario_actual = None
    
    def cargar_csv(self, archivo, clase):
        ''''''
        with open(archivo, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if clase == Actor:
                    actor = Actor(**row)
                    self.actores[actor.id_estrella] = actor
                elif clase == Pelicula:
                    pelicula = Pelicula(**row)
                    self.peliculas[pelicula.id_pelicula] = pelicula
                elif clase == Relacion:
                    relacion = Relacion(**row)
                    self.relaciones[relacion.id_relacion] = relacion
                elif clase == User:
                    user = User(**row)
                    self.usuarios[user.username] = user
        
        if clase == Actor:
            self.idx_actor = max(self.actores.keys()) if self.actores else 0
        elif clase == Pelicula:
            self.idx_pelicula = max(self.peliculas.keys()) if self.peliculas else 0
        elif clase == Relacion:
            self.idx_relacion = max(self.relaciones.keys()) if self.relaciones else 0

    def guardar_csv(self, archivo, objetos):
        if not objetos:
            return
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=next(iter(objetos.values())).to_dict().keys())
            writer.writeheader()
            for obj in objetos.values():
                writer.writerow(obj.to_dict())

    def obtener_peliculas_por_actor(self, id_estrella):
        ''' Devuelve una lista de películas en las que ha participado un actor '''
        ids_peliculas = [rel.id_pelicula for rel in self.relaciones.values() if rel.id_estrella == id_estrella]
        return [self.peliculas[id_pelicula] for id_pelicula in ids_peliculas]
    
    def obtener_actores_por_pelicula(self, id_pelicula):
        ''' Devuelve  '''
        ids_actores = [rel.id_estrella for rel in self.relaciones.values() if rel.id_pelicula == id_pelicula]
        return [self.actores[id_estrella] for id_estrella in ids_actores]
    
    def login(self, username, password):
        if username in self.usuarios:
            user = self.usuarios[username]
            print(f"{u.password}, {password}")
            if user.hash_string(password) == user.password:
                self.usuario_actual = user
                return True
        return False
    
    def agregar_actor(self, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen):
        if self.usuario_actual is not None:
            self.idx_actor += 1
            actor = Actor(self.idx_actor, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, self.usuario_actual.username)
            self.actores[self.idx_actor] = actor

if __name__ == "__main__":
    archivo_actores = "datos/movies_db - actores.csv"
    archivo_peliculas = "datos/movies_db - peliculas.csv"
    archivo_relaciones = "datos/movies_db - relacion.csv"
    archivo_usuarios = "datos/movies_db - users_hashed.csv"
    sistema = SistemaCine()
    sistema.cargar_csv(archivo_actores, Actor)
    sistema.cargar_csv(archivo_peliculas, Pelicula)
    sistema.cargar_csv(archivo_relaciones, Relacion)
    sistema.cargar_csv(archivo_usuarios, User)
    actores = sistema.actores
    for id_estrella, actor in actores.items():
        print(f"{id_estrella}: {actor.nombre:35s} - {actor.fecha_nacimiento}")
    lista_peliculas = sistema.obtener_peliculas_por_actor(1)
    for pelicula in lista_peliculas:
        print(pelicula)
    print(len(lista_peliculas))
    lista_actores_en_pelicula = sistema.obtener_actores_por_pelicula(1)
    for actor in lista_actores_en_pelicula:
        print(actor.nombre)
    #for u in sistema.usuarios.values():
    #    u.password = u.hash_string(u.password)
    #hashed_users = "datos/movies_db - users_hashed.csv"
    #sistema.guardar_csv(hashed_users, sistema.usuarios)
    #print(f"Se escribió el archivo {hashed_users}")
    u = sistema.usuarios['fcirettg']
    print(type(u))
    print(u.username)
    print(u.password)
    print(u.hash_string(u.password))
    exito = sistema.login('fcirettg', '12345')
    print(exito)
    if exito:
        print(sistema.usuario_actual.username)
    else:
        print(f"Usuario o contraseña incorrectos...")
    sistema.agregar_actor('Millie Bobby Brown', '2004-02-19', 'Marbella', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Millie_Bobby_Brown_-_MBB_-_Portrait_1_-_SFM5_-_July_10%2C_2022_at_Stranger_Fan_Meet_5_People_Convention.jpg/640px-Millie_Bobby_Brown_-_MBB_-_Portrait_1_-_SFM5_-_July_10%2C_2022_at_Stranger_Fan_Meet_5_People_Convention.jpg')
    for actor in sistema.actores.values():
        print(f'{actor.id_estrella}: {actor.nombre:35s} - {actor.fecha_nacimiento}')
    sistema.guardar_csv(archivo_actores, sistema.actores)