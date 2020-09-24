"""
Practica0_Ejemplo1c.py

Prácticas de Fundamentos de programacion
Ejemplo 1: Calculo del area de un círculo

Determina el area de un círculo a partir del radio.

Autor: Ricardo Ferris

Fecha: 12/09/2018
Version 1.0
"""

from math import pi

RADIO_MAXIMO = 10
"""
Radio maximo para realización de los cálculos
"""

# Módulo principal
def main():
    # Empezamos explicando al usuario lo que hace el programa
    print("\nEste programa determina el area de un círculo, de a lo")
    print("sumo", RADIO_MAXIMO, "unidades de radio, a partir del radio.")

    # ENTRADA DE DATOS
    radio = int(input("Dime el radio del círculo: ") )
    while radio < 0 or radio > RADIO_MAXIMO:
          radio = int(input("Dime el radio del círculo: ") )

    #PROCESAMIENTO DE INFORMACION
    area = pi * radio ** 2

    #SALIDA DE RESULTADOS
    print("El area del círculo de radio", radio, "es", area)

if __name__ == '__main__':
    main()
