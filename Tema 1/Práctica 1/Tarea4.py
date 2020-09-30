# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:47:28 2020

@author: Raul
Es un ejercicio en la que pasas unos datos y te los escribe por pantalla
"""


def main():
    nombre = input("Dame nombre:");
    apellidos = input("Dame apellidos:");
    anyoNacimiento = input("Dame año de nacimiento:");
    
    print("\nFicha");
    print("*" * 30);
    print("Nombre:", nombre);
    print("Apellidos:", apellidos);
    print("Año:", anyoNacimiento);
    print("*" * 30);

if __name__ == "__main__":
    main();