# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:37:30 2020

@author: Raul
"""

PRECIO_INGENIERO = 5000;
PIES_TO_MILLAS = 5280;

def main():
    print("Prueba 1:");
    pies = float(input("Cuantos pies mide la carretera?"));
    millas = pies/PIES_TO_MILLAS;
    
    print("El ingeniero cobra:"+millas * PRECIO_INGENIERO)
    
    print("Prueba 2:");
    pies = float(input("Cuantos pies mide la carretera?"));
    millas = pies/PIES_TO_MILLAS;
    
    print("El ingeniero cobra:"+millas * PRECIO_INGENIERO)
    
    print("Prueba 3:");
    pies = float(input("Cuantos pies mide la carretera?"));
    millas = pies/PIES_TO_MILLAS;
    
    print("El ingeniero cobra:"+millas * PRECIO_INGENIERO)

if __name__ == "__main__":
    main();