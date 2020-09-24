"""
Practica0_Ejemplo4.py

Prácticas de Fundamentos de programacion
Ejemplo 4: Resolución de una ecuacion de segundo grado.

Resolución de una ecuacion de segundo grado para soluciones reales

Version 1.1
Autor: Profeores de FP
Fecha 16/10/2008
"""

from math import sqrt

def main():
    print("Resolucion de una ecuacion de 2o. grado en la forma:")
    print("  A * x2 + B * x + C = 0")
    
    # ENTRADAS
    print("Introducir a continuacion el valor de los coeficientes A, B y C.")
    a = float(input("Coef. A: ") )
    b = float(input("Coef. B: ") )
    c = float(input("Coef. C: ") )

    # CALCULO DE SOLUCIONES
    if (a == 0) and (b == 0):
        tipo = 1
    elif a == 0:
        x1 = -c / b
        tipo = 2
    else:
        discr = b * b - 4 * a * c
        if discr < 0:
            tipo = 3
        else:
            x1 = -b + sqrt (discr) / (2 * a)
            x2 = -b - sqrt (discr) / (2 * a)
            tipo = 4

    # SALIDA DE RESULTADOS EN FUNCION DEL TIPO DE ECUACION
    # Ecuacion de grado cero
    print("asd")
    print(x1)
    print(x2)
    if tipo == 1:
        if c == 0:
            print("La solucion es cualquier numero real.")
        else:
            print("La ecuación no tiene solucion.")
    # Ecuacion de 1er. grado
    elif tipo == 2:
        print("Solucion x =", x1)
    # Ecuacion de 2o grado
	# Soluciones complejas
    elif tipo == 3:
        print("Las soluciones a la ecuacion son numeros complejos.")
    # Soluciones reales
    else:
        print("Las soluciones a la ecuacion son:")
        print("x1 =", x1)
        print("x2 =", x2)

if __name__ == '__main__':
    main()
