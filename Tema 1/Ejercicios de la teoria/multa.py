# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:52:15 2020

Este es un programa que lo que mira es si pasa de la cantidad de días para devolver un libro (3)
te dice la cantidad de multa que es 2€ por cada día de más.


@author: Raul
"""

NUM_DIAS_LIMITE = 3
def main():
    numDias = int(input("Escriba el numero de dias: "))
    if numDias > NUM_DIAS_LIMITE:
        print("La multa es de " + str(2*(numDias-NUM_DIAS_LIMITE)) + "€")
    if numDias <= NUM_DIAS_LIMITE:
        print("No hay multa")
    
if __name__ == "__main__":
    main()