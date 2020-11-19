# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:47:40 2020

@author: Raul
"""

def Factorial(num:int)->int:
    if num == 0 or num == 1:
        retorna = 1
    else:
        retorna = Factorial(num - 1)
    return retorna

def Taylor(x:int, cantidad_terminos:int)->int:
    cont = 0
    for i in range(cantidad_terminos):
        cont += x**i/Factorial(i)
    return cont

def main():
    print(__doc__)
    
    x = int(input("Dame una x: "))
    cantidad_terminos = int(input("Dame la cantidad de terminos: "))
    
    print(Taylor(x, cantidad_terminos))
    
if __name__ == "__main__":
    main()