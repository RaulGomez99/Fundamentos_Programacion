# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:09:24 2020

@author: Ismael
"""

def main():
    fichero = input("Escriba el nombre del fichero para abrir:")
    print(fichero)
    try: 
        f = open(fichero, encoding="UTF-8")
    except:
        print("Ha habido un error abriendo el fichero nombrado")
    else: 
        i = 0
        numAprob = 0
        numSusp = 0
        for linea in f:
                if i %2==1:
                    if float(linea) >= 5: numAprob +=1  
                    else: numSusp +=1                           
                i+=1
        print(str(numAprob/(numAprob+numSusp)*100)+ "el % de  aprobados es")
        print(str(numSusp/(numAprob+numSusp)*100)+ "el % de  suspendidos es")
     
    
if __name__ == '__main__':
    main()