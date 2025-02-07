import tablero

def main():
     numeros = [str(x) for x in range(1,10)]
     dsimbolos = {x:x for x in numeros}
     g = tablero.juego(dsimbolos)
     if g is not None:
        print(f'El ganador es {g}')
     else:
         print('Empate')
         
if __name__ == '_main_':
    main()