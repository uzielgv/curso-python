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

if __name__ == "__main__":
    app.run(debug=True)