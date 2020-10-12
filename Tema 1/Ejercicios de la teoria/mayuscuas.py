# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:05:00 2020

Este programa dirá dada una letra si es mayúscula  minúscula o número o no es nada

@author: Raul
"""

def main():
    #ENTRADA DE DATOS
    letra = input("Escribe letra");
    
    #PROCESO DE DATOS
    if letra >= "A" and letra <= "Z" or letra == "Ñ":
        print("Es mayúscula");
    elif letra >= "a" and letra <="z" or letra == "ñ":
        print("Es minúscula");
    elif letra >= "0" and letra <= "9":
        print("Es un número");
    else:
        print("No es nada")
    
    
if __name__ == "__main__":
    main()