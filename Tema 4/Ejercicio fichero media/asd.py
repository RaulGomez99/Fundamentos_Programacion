# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:50:15 2020

@author: Raul
"""

def main():    
    fichero = input("Escribe nombre del fichero")
    try:
        f = open(fichero, encoding = "UTF-8")
    except:
        print("Error del fichero")
    else:
        contAprobados = 0
        contSuspendidos = 0
        numeroLinea = 1
        for linea in f:
            if numeroLinea % 2 == 0:
                linea = int(linea)                
                if linea >= 5:
                    contAprobados += 1
                else:
                    contSuspendidos += 1
            numeroLinea+=1
        print(contAprobados*100/(contAprobados+contSuspendidos),"% Aprobados")
        print(contSuspendidos*100/(contAprobados+contSuspendidos), "% Suspendidos")
            

    
        
    
            
        
        
            
        
    
    
if __name__ == "__main__":
    main()