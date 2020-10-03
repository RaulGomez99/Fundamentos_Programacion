# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:23:17 2020

@author: Raul
"""

def main():
    horas = int(input("Escriba número de horas"));
    minutos = int(input("Escriba número de minutos"));
    segundos = int(input("Escriba número de segundos"));
    
    segundosIncrementar = int(input("Escriba número de segundos que quieras incrementar"));
    segundos+= segundosIncrementar;
    minutos+=segundos//60;
    segundos%=60;
    horas+=minutos//60;
    minutos%=60;
    print(str(horas)+":"+str(minutos)+":"+str(segundos));
    
    
if __name__ == "__main__":
    main();