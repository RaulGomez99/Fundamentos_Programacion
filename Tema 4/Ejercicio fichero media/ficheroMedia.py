# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:50:33 2020

@author: Raul
"""

def main():
    nombre = input("Escriba nombre del fichero")
    try:
        f = open(nombre, encoding="UTF-8")
    except:
        print("Ocurrio un error")
    else:
        contAprobados = 0
        contSuspendidos = 0
        numLinea = 1
        for linea in f:
            if numLinea % 2 == 0:
                if float(linea) >= 5: contAprobados += 1
                else: contSuspendidos += 1
            numLinea+=1
        print(str(contAprobados/(contAprobados+contSuspendidos)*100)+"% de aprobados")
        print(str(contSuspendidos/(contAprobados+contSuspendidos)*100)+"% de suspendidos")
            
    
    
if __name__ == "__main__":
    main()