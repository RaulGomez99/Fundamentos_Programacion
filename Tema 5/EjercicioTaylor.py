# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:47:40 2020
Calcula el taylor de e^x
@author: Raul
"""
from math import e

def Factorial(num:int)->int:
    if num == 0 or num == 1:
        retorna = 1
    else:
        retorna = Factorial(num - 1)
    return retorna

def Taylor(x:int, cantidad_terminos:int, a:int)->int:
    cont = 0
    for i in range(cantidad_terminos):
        cont += (((e**a)/Factorial(i)) * (x - a)**i)
    return cont

def main():
    print(__doc__)
    
    x = int(input("Dame una x: "))
    a = int(input("Dame una a: "))
    cantidad_terminos = int(input("Dame la cantidad de terminos: "))
    
    print(Taylor(x, cantidad_terminos, a))
    
if __name__ == "__main__":
    main()