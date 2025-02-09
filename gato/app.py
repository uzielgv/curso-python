import argparse

import tablero

def main(u:str):
    '''Función principal'''
    X = {"G":0, "P":0, "E":0}
    O = {"G":0, "P":0, "E":0}
    score = {"X":X, "O":O}
    numeros = [str(i) for i in range(1, 10)]
    corriendo = True
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_scores(score, g, u)
        tablero.despliega_tablero(score, u)
        seguir = input('¿Quieres seguir jugando? (s/n): ')
        if seguir.lower() == 'n':
            corriendo = False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type=str, help='Nombre del usuario', default='Usuario')
    args = parser.parse_args()
    main(args.u)