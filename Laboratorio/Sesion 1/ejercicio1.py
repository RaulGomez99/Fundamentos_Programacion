# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:06:15 2020
Es un programa que pasa los grados Celsius a Fahrenheit
@author: Iker y Raúl
"""
FACTOR_DE_ESCALA=9/5
DESFASE=32

def main():
    #ENTRADA
    C=float(input("¿Que temperatura desea añadir?(en Celsius):"));
    #PROCESAMIENTO
    F=FACTOR_DE_ESCALA*C+DESFASE
    #SALIDA
    print("El valor exacto de grados Celsius convertidos Fahrenheit es de ",F)
    
if __name__=="__main__":
    main()