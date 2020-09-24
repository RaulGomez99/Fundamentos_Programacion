"""
Practica0_Ejemplo5.py

Prácticas de Fundamentos de programacion
Ejemplo 5: Suma, resta y multiplicacion.

Este programa suma, resta y multiplica dos valores introducidos por teclado

      Este programa contiene errores de compilacion que hay
      que corregir leyendo y entendiendo los mensajes de
      error que proporciona el compilador

Version 1.1
Autor Profeores de FP
Fecha 16/10/2008
"""

def mani():
    print ("Introducir 2 numeros enteros:)
    x = int(input())
    y = int(input())

    suma = x + y
    resta = x - y
    mult = x * y

    print(x, "+", y, "=", suma)
    print(x, "-", y, "=", rest)
    print(x, "*", y, "=", mult)

if __name__ == '__main__':
    main()