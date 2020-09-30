# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:37:30 2020

@author: Raul

Es una práctica en la que dado un número de pies
y un número de precio por milla saldrá lo que cobrará el ingeniero por construirla
"""

PRECIO_INGENIERO = 5000;
PIES_TO_MILLAS = 5280;

def main():
    pies = float(input("¿Cuántos pies mide la carretera?"));
    millas = pies/PIES_TO_MILLAS;
    
    print("El ingeniero cobra:",millas * PRECIO_INGENIERO)


if __name__ == "__main__":
    main();
