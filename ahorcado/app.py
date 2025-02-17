'''
Programa principal del juego del ahorcado
'''
import string
import funciones as fn
from random import choice

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal
    '''
    plantillas = fn.carga_plantillas(nombre_plantilla)
    lista_oraciones = fn.carga_texto_archivo(archivo_texto)
    palabras = fn.obten_palabras(lista_oraciones)
    p = choice(palabras)
    o = 5
    abecedario = {letra:letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abecedario, p, letras_adivinadas, o)
        if p == ''.join([letra if letra in letras_adivinadas else '_' for letra in p]):
            print('Ganaste')
            break
    print(f"La palabra era: '{p}'")

if __name__ == '__main__':
    archivo = './datos/pg15532.txt'
    main(archivo)