'''
Funciones auxiliares del juego Ahorcado
'''
import string
import unicodedata
from random import choice

def carga_texto_archivo(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las
    oraciones del archivo
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla)->dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_texto_archivo(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel >= 0 and nivel <= 5:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

def obten_palabras(lista:list)->list:
    '''
    Obtiene las palabras de un texto
    '''
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)

def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, turnos:int):
    '''
    Adivina una letra de una palabra
    '''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    print(f'Tienes {turnos} turnos')
    abcd = ' '.join(abc.values())
    print(f'El abecedario es: {abcd}')
    print(f'La palabra es: {palabra_oculta}')
    letra = input('Ingrese una letra: ')
    if len(letra) != 1 or letra not in abc:
        print('Ingresa una letra válida')
    else:
        if abc[letra] == "*":
            print('Ya ingresaste esa letra...')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1
        
if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla, 5)
    lista_oraciones = carga_texto_archivo('./datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)
    abecedario = {letra:letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    turnos = 5
    adivina_letra(abecedario, p, letras_adivinadas, turnos)
    adivina_letra(abecedario, p, letras_adivinadas, turnos)