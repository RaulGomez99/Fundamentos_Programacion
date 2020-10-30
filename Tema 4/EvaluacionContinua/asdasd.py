# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:22:10 2020

@author: Raul
"""

def main():
    nombre = input("adsasdasd")
    try:
        f = open(nombre, encoding="UTF-8")
    except:
        print("asd")
    else:
        nombre = f.readline()
        while nombre != "":
            nota1 = float(f.readline())
            nota2 = float(f.readline())
            nota3 = float(f.readline())
            
            if nota1 < 3.5:
                print(nombre)
            elif nota2 < 3.5:
                print(nombre)
            elif nota3 < 3.5:
                print(nombre)
            nombre = f.readline()
        f.close()
    
    
if __name__ == "__main__":
    main()