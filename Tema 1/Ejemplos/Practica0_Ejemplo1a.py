"""
Practica0_Ejemplo1.py

Prácticas de Fundamentos de programacion
Ejemplo 1: Calculo de edades.

Determina la edad del usuario a partir de la informacion proporcionada 
por teclado.

Autor: Ricardo Ferris

Fecha: 12/09/2018
Version 1.0
"""

ANYO_ACTUAL = 2018
"""
Anyo actual para calcular la edad del usuario
"""

# Empezamos explicando al usuario lo que hace el programa
print("\nEste programa determina la edad del usuario a partir de la")
print("informacion proporcionada por teclado.")

# ENTRADA DE DATOS
nombre = input("Indica tu nombre: ")

anyo = int(input("Indica tu anyo de nacimiento: ") )

#PROCESAMIENTO DE INFORMACION
edad = ANYO_ACTUAL - anyo

#SALIDA DE RESULTADOS
print(nombre, "tienes", edad, "anyos.")
if (edad >= 17):
    print("Yo acabo de ser creado !!!")
else:
    print("¡¡¡No me lo creo!!!")
