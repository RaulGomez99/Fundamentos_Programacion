# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:23:58 2020

@author: Raul
"""

def main():
    x = float(input("Escriba el valor para x"));
    y = float(input("Escriba el valor para y"));
    
    print(x, " + 3", y," = ",x+3*y);
    print(x, "² + ", y, "²/7 = ",x**2+y**2/7);
    print(x, "² * ", y, "²/",x , "³ + ",y, "³ = ",(x**2 * y**2)/(x**3 + y**3))

if __name__ == "__main__":
    main();