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

def juego(simbolos:dict):
    '''Juego del gato'''
    lista_combinaciones = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['1', '4', '7'],
        ['2', '5', '8'],
        ['3', '6', '9'],
        ['1', '5', '9'],
        ['3', '5', '7']
    ]
    en_juego = True
    gana = None
    movimientos = 0
    dibuja_tablero(simbolos)
    while en_juego:
        if movimientos < 9:
            usuario(simbolos)
            dibuja_tablero(simbolos)
            movimientos += 1
            gana = checa_winner(simbolos, lista_combinaciones)
            if gana is not None:
                en_juego = False
                continue
            if movimientos >= 9:
                en_juego = False
                continue
            ia(simbolos)
            dibuja_tablero(simbolos)
            movimientos += 1
            if gana is not None:
                en_juego = False
                continue
            if movimientos >= 9:
                en_juego = False
                continue
    return gana

def checa_winner(simbolos:dict, combinaciones:list):
    '''Checa si hay un ganador'''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None

if __name__ == '__main__':
    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x:x for x in numeros}
    g = juego(dsimbolos)
    if g is not None:
        print(f"El ganador es {g}")
    else:
        print("Empate")
    '''dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)
    x = random.choice(numeros)
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