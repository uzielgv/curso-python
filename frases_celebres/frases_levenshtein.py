''' Programa que busca una lista de palabras en las frases célebres de películas '''
import os
import csv
import argparse
import Levenshtein

# Función para leer el archivo CSV y devolver una lista de frases
def leer_csv(archivo:str)->list:
    ''' Lee un archivo CSV y devuelve una lista de frases '''
    frases = []
    with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            frases.append([fila[0], fila[1]])
    return frases

# Función para buscar palabras en las frases
def buscar_palabras(frases:list, frase_a_buscar:str)->list:
    ''' Busca una frase en una lista de frases '''
    frases_encontradas = []
    frase_a_buscar = frase_a_buscar.lower()
    for lista in frases: #Lista contiene la frase y película
        frase = lista[0].lower()
        pelicula = lista[1]
        ratio = Levenshtein.ratio(frase, frase_a_buscar)
        if ratio > 0.8: #Si la distancia es menor a 0.8, se considera una coincidencia
            frases_encontradas.append([frase, pelicula, ratio])   
    return frases_encontradas

# Función para mostrar las frases encontradas
def mostrar_frases(frases:list, porcentaje:float=0.8):
    ''' Muestra una lista de frases '''
    for lista in frases:
        frase = lista[0]
        pelicula = lista[1]
        ratio = lista[2]
        if ratio >= porcentaje:
            print(f"{frase} - {pelicula} - Ratio: {ratio:.2f}")

# Función principal
def main(archivo:str, una_frase:str, porcentaje:float):
    ''' Función principal del programa '''
    # Leer el archivo CSV
    frases = leer_csv(archivo)
    # Buscar las palabras en las frases
    frases_encontradas = buscar_palabras(frases, una_frase)
    # Desplegar la frase a encontrar
    print(f"Buscando la frase: {una_frase}")
    # Mostrar las frases encontradas
    mostrar_frases(frases_encontradas, porcentaje)

if __name__ == "__main__":
    # Crear el parser
    parser = argparse.ArgumentParser(description='Buscar palabras en frases célebres de películas.')
    # Añadir argumentos
    parser.add_argument('frase', type=str, help='Frase a buscar')
    parser.add_argument('porcentaje', type=float, default=0.8, help='Porcentaje de coincidencia (default: 0.8)')
    # Obtener argumentos
    args = parser.parse_args()
    archivo_frases = os.path.join(os.path.dirname(__file__), 'frases_consolidadas.csv')
    # Llamar a la función principal
    main(archivo_frases, args.frase, args.porcentaje)