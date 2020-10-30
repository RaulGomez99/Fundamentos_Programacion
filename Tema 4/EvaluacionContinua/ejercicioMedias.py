# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:14:08 2020

@author: Raul
"""

NOTA_CORTE = 3.5

def main():
    nombre = input("Escriba nombre del fichero")
    try:
        f = open(nombre, encoding="UTF-8")
    except:
        print("Ocurrio un error")
    else:
        nombre = f.readline()
        while nombre != "":
            continua = float(f.readline())
            examenes = float(f.readline())   
            practicas = float(f.readline())
            
            if continua < NOTA_CORTE or examenes < NOTA_CORTE or practicas < NOTA_CORTE:
                print(nombre)
            nombre = f.readline()
        f.close()
                
    
    
if __name__ == "__main__":
    main()