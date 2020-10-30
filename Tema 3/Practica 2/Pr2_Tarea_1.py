# -*- coding: utf-8 -*-
"""
Pr2_Tarea_1.py
Este programa pasa una cierta medida de distancia en metros a las
distintas medidas de distancia del sistema anglosajón: Pulgadas,
pies, yardas, millas y leguas.
Version 1.0
Autor: Ricardo Ferrís Castell
Fecha: 25/09/2018
"""
#Definición de los factores de conversión (constantes)
METROS2PULGADAS = 39.3700787  # Factor de conversión entre metros y pulgadas
METROS2PIES = 3.2808399 # Factor de conversión entre metros y pies
METROS2YARDAS = 1.0936133 # Factor de conversión entre metros y yardas
METROS2MILLAS = 0.00062137  # Factor de conversión entre metros y millas 
METROS2LEGUAS = 0.00020712373  # Factor de conversión entre metros y leguas
def main():
 print("Este programa pasa una cierta medida de distancia en")
 print("metros a las distintas medidas de distancia del sistema")
 print("anglosajón: Pulgadas, pies, yardas, millas y leguas.")
 metros = float(input("Valor en metros: "))
 pulgadas = metros * METROS2PULGADAS
 pies = metros * METROS2PIES
 yardas = metros * METROS2YARDAS
 millas = metros / METROS2MILLAS
 leguas = metros * METROS2LEGUAS
 print("Los", metros, "metros introducidos son:")
 print(pulgadas, "in")
 print(pies, "ft")
 print(yardas, "yd")
 print(millas, "mi")
 print(leguas, "leguas")
if __name__ == '__main__':
 main () 
