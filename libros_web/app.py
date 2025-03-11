''' Programa principal de Libros Web '''
from flask import Flask, render_template, request
import funciones as fn

app = Flask(__name__)

archivo_csv = "booklist2000.csv"
lista_libros = fn.lee_archivo_csv(archivo_csv)
diccionario_titulos = fn.crea_diccionario(lista_libros, 'title')
diccionario_autores = fn.crea_diccionario(lista_libros, 'author')
diccionario_id = fn.crea_diccionario(lista_libros, 'id')

@app.route('/')
def inicio():
    ''' Página de inicio '''
    return render_template('index.html')

@app.route('/titulo', methods = ['GET', 'POST'])
def busqueda_titulo():
    ''' Página de búsqueda por título '''
    resultado = []
    if request.method == 'POST':
        titulo = request.form['titulo']
        resultado = fn.busca_en_diccionario(diccionario_titulos, titulo)
    return render_template('titulo.html', lista_libros=resultado)

@app.route('/libro/<id_libro>', methods=['GET'])
def libro(id_libro:str):
    ''' Página de información de un libro '''
    if id_libro in diccionario_id:
        book = diccionario_id[id_libro]
        return render_template('libro.html', libro=book)
    else:
        return render_template('libro.html', libro=None)

if __name__ == "__main__":
    app.run(debug=True)