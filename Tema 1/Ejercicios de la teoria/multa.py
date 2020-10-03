# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:52:15 2020

@author: Raul
"""

def main():
    numDias = int(input("Escriba el numero de dias"));
    if(numDias > 2):
        print("La multa es de",2*(numDias-2))
    
if __name__ == "__main__":
    main();