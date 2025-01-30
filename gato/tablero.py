'''
tablero.py: Dibuja el tablero del juego del gato.
'''
import random

def dibuja_tablero(dsimbolos:dict):
    ''' Dibuja el tablero del juego. '''
    print(f'''
    {dsimbolos['1']} | {dsimbolos['2']} | {dsimbolos['3']}
    ----------
    {dsimbolos['4']} | {dsimbolos['5']} | {dsimbolos['6']}
    ----------
    {dsimbolos['7']} | {dsimbolos['8']} | {dsimbolos['9']}
    ''')

def ia(simbolos:dict):
    ''' Juega la máquina '''
    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X', 'O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(dsimbolos:dict):
    ''' Juega el usuario'''
    numeros = [str(i) for i in range(1, 10)]
    ocupado = True
    while ocupado == True:
        x = input('Ingresa el número de la casilla: ')
        if x in numeros:
            if dsimbolos[x] not in ['X', 'O']:
                dsimbolos[x] = 'X'
                ocupado = False
            else:
                print('Casilla ocupada')
        else:
            print('Número incorrecto')

if __name__ == '__main__':
    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)
    '''x = random.choice(numeros)
    numeros.remove(x)
    dibuja_tablero(dsimbolos)
    dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    o = random.choice(numeros)
    numeros.remove(o)
    dsimbolos[o] = 'O'
    dibuja_tablero(dsimbolos)
    print(numeros)
    '''