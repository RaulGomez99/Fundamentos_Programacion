# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:27:10 2020

@author: Raul
"""



def NumeroMayorYMenor(num1:int, num2:int)->int:
    if num1 > num2:
        maxim = num1
        minim = num2
    else:
        maxim = num2
        minim = num1
    return maxim, minim

def AcumDivisores(num:int)->int:
    acum = 0
    for i in range(1,num):
        if num % i == 0:
            acum += i
        
    return acum

def EsDefectivo(num:int)->bool:
    return AcumDivisores(num) < num

def EsPerfecto(num:int)->bool:
    return AcumDivisores(num) == num

def EsAbundante(num:int)->bool:
    return AcumDivisores(num) > num

def main():
    num1 = int(input("Introduce un número para que esté en el rango"))
    num2 = int(input("Introduce otro número para que esté en el rango"))
    maxim, minim = NumeroMayorYMenor(num1, num2)
    acum_defectivos = 0
    acum_abundantes = 0
    acum_perfectos = 0
    for i in range(minim, maxim):
        if EsDefectivo(i):
            acum_defectivos += i
        elif EsAbundante(i):
            acum_perfectos += i
        elif EsPerfecto(i):
            acum_abundantes += i
            
    print("Defectivos:", acum_defectivos)
    print("Abundantes:", acum_abundantes)
    print("Perfectos:", acum_perfectos)
    
if __name__ == "__main__":
    main()