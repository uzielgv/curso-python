''' Programa principal de MovieDB '''
from flask import Flask, request, url_for, render_template, redirect
import os
import random
import movie_classes as mc

app = Flask(__name__)
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

@app.route('/actor/<id_estrella>', methods=['GET'])
def actor(id_estrella:str):
    ''' Muestra información sobre un cierto actor '''
    int_id = int(id_estrella)
    actor = sistema.actores[int_id]
    peliculas = sistema.obtener_peliculas_por_actor(int_id)
    personajes = sistema.obtener_personajes_por_actor_en_pelicula(int_id)
    return render_template('actor.html', actor=actor, peliculas=peliculas, personajes=personajes)

@app.route('/peliculas')
def peliculas():
    ''' Muestra la lista de las películas'''
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/pelicula/<id_pelicula>', methods=['GET'])
def pelicula(id_pelicula:str):
    ''' Muestra información sobre una película '''
    int_id = int(id_pelicula)
    pelicula = sistema.peliculas[int_id]
    actores = sistema.obtener_actores_por_pelicula(int_id)
    personajes = sistema.obtener_personajes_en_pelicula(int_id)
    return render_template('pelicula.html', pelicula=pelicula, actores=actores, personajes=personajes)

if __name__ == "__main__":
    app.run(debug=True)