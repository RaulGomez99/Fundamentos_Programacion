# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:23:14 2020
Este programa calcula el peso de un atomo a partir del peso atomico de un elemento químico
@author: Iker & Raul
@Fecha: 21/10/2020

"""

NUM_AVOGADRO = 6.022 * 10**23

def main():
    print(__doc__)
    
    #ENTRADA DE DATOS
    x=int(input("Dime sustancia: "))
    p_a=float(input("Dime su peso atómico: ")) 
    
    #CALCULO 
    gr=p_a/NUM_AVOGADRO
    
    #SALIDA DE RESULTADOS
    print('El peso de un atomo de la sustancia %d es %1.5e gramos'%(x,gr))
    
if __name__ == "__main__":
    main()

