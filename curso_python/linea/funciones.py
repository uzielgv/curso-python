# Archivo con todas las funciones necesarias para la aplicación línea
def calcular_y(x:float, m:float, b:float) -> float:
    '''
    Calcula el valor de y en una línea recta
    x: valor de x
    m: pendiente
    b: intersección con el eje y
    Regresa el valor de y
    '''
    return m*x + b

def test_linea():
    '''
    Comprobamos calcular_y()
    '''
    y = calcular_y(0.0, 2.0, 3.0)
    return y

if __name__ == '__main__':
    if test_linea() == 3.0:
        print('Test exitoso')
    else:
        print('Test fallido')