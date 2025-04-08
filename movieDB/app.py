''' Programa principal de MovieDB '''
from flask import Flask, request, url_for, render_template, redirect, flash
import os
import random
import movie_classes as mc

app = Flask(__name__)
app.secret_key = os.urandom(24) # Clave secreta para la sesión 
sistema = mc.SistemaCine()
archivo_actores = "datos/movies_db - actores.csv"
archivo_peliculas = "datos/movies_db - peliculas.csv"
archivo_relaciones = "datos/movies_db - relacion.csv"
archivo_usuarios = "datos/movies_db - users_hashed.csv"
sistema.cargar_csv(archivo_actores, mc.Actor)
sistema.cargar_csv(archivo_peliculas, mc.Pelicula)
sistema.cargar_csv(archivo_relaciones, mc.Relacion)
sistema.cargar_csv(archivo_usuarios, mc.User)

@app.route('/')
def index():
    ''' Página principal de la aplicación '''
    return render_template('index.html')

@app.route('/actores')
def actores():
    ''' Muestra la lista de los actores '''
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)

@app.route('/actor/<int:id_actor>')
def actor(id_actor):
    ''' Muestra la información de un actor '''
    actor = sistema.actores[id_actor]
    personajes = sistema.obtener_personajes_por_estrella(id_actor)
    return render_template('actor.html', actor=actor, lista_peliculas=personajes)

@app.route('/peliculas')
def peliculas():
    ''' Muestra la lista de las películas'''
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    ''' Muestra la información de una película '''
    pelicula = sistema.peliculas[id_pelicula]
    personajes = sistema.obtener_personajes_por_pelicula(id_pelicula)
    return render_template('pelicula.html', pelicula=pelicula, lista_actores=personajes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' Muestra el formulario de login '''
    session = {}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exito = sistema.login(username, password)
        if exito:
            session['logged_in'] = True
            session['username'] = sistema.usuario_actual.nombre_completo
            return redirect(url_for('index'))
        else:
            error = 'Usuario o contraseña incorrectos...'
            return render_template('login.html')
    return render_template('login.html')

@app.route('/agregar_relacion', methods=['GET', 'POST'])
def agregar_relacion():
    if sistema.usuario_actual is None:
        flash('Debes iniciar sesión para agregar relaciones', 'warning')
        return redirect(url_for('login'))
    if request.method == 'GET':
        actores_list=[]
        for actor in sistema.actores.values():
            actores_list.append({
                'id_estrella': actor.id_estrella,
                'nombre': actor.nombre
            })
            sorted_actores = sorted(actores_list, key=lambda x: x['nombre'])
        peliculas_list=[]
        for pelicula in sistema.peliculas.values():
            peliculas_list.append({
                'id_pelicula': pelicula.id_pelicula,
                'titulo': pelicula.titulo_pelicula
            })
            sorted_peliculas = sorted(peliculas_list, key=lambda x: x['titulo'])
        return render_template('agregar_relacion.html', actores=sorted_actores, peliculas=sorted_peliculas)
    if request.method == 'POST':
        id_actor = int(request.form['actorSelect'])
        id_pelicula = int(request.form['movieSelect'])
        personaje = request.form['character']
        sistema.agregar_relacion(id_pelicula, id_actor, personaje)
        sistema.guardar_csv(archivo_relaciones, sistema.relaciones)
        flash('Relación agregada correctamente', 'success')
        return redirect(url_for('actor', id_actor=id_actor))
    
@app.route('/agregar_pelicula', methods=['GET', 'POST'])
def agregar_pelicula():
    if sistema.usuario_actual is None:
        flash('Debes iniciar sesión para agregar una película', 'warning')
        return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('agregar_pelicula.html')
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        fecha_lanzamiento = request.form.get('fecha_lanzamiento')
        url_poster = request.form.get('url_poster')
        sistema.agregar_pelicula(titulo,fecha_lanzamiento,url_poster)
        sistema.guardar_csv(archivo_peliculas, sistema.peliculas)
        return redirect(url_for('peliculas'))

@app.route('/agregar_actor', methods=['GET', 'POST'])
def agregar_actor():
    if sistema.usuario_actual is None:
        flash('Debes iniciar sesión para agregar un actor o actriz', 'warning')
        return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('agregar_actor.html')
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        ciudad_nacimiento = request.form.get('ciudad_nacimiento')
        url_imagen = request.form.get('url_imagen')
        sistema.agregar_actor(nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen)
        sistema.guardar_csv(archivo_actores, sistema.actores)
        return redirect(url_for('actores'))

if __name__ == "__main__":
    app.run(debug=True)