# Cálculo de coordenadas de líneas
import funciones

def main():
    m = 2.0
    b = 3.0
    # X = [x for x in range(1, 11)]
    # Y = [funciones.calcular_y(x, m, b) for x in X]
    # print("Enteros:")
    # coordenadas_enteros = list(zip(X, Y))
    # print(coordenadas_enteros)
    XF = [x/10.0 for x in range(1, 110, 5)]
    YF = [funciones.calcular_y(x, m, b) for x in XF]
    coordenadas_flotantes = list(zip(XF, YF))
    print("Flotantes:")
    print(coordenadas_flotantes)

if __name__ == '__main__':
    main()