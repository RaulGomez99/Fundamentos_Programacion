
"""
Practica0_Ejemplo6.py

Prácticas de Fundamentos de programacion
Ejemplo 6: Inverso de la division.

Este programa divide dos numeros entre si y a continuacion invierte
el resultado

      Este programa contiene errores de ejecución que hay
      que corregir depurando el codigo y trazando el valor de
      las variables

Version 1.1
Autor Profesores de FP
Fecha 16/10/2008
"""

NUMERADOR = 1;
DENOMINADOR = 4;

def main():

    division = NUMERADOR // DENOMINADOR;

    print("Invertimos la division y se obtiene:", 1 // division)

if __name__ == '__main__':
    main()