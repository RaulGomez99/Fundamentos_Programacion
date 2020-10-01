# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:00:16 2020

@author: Raul
"""

from tkinter import Tk;
from botonMina import BotonBuscaMinas;
import random;


w, h = 10, 10;
botones = [[0 for x in range(w)] for y in range(h)] 
 
#Aquí esta el main
def main():
    print("Creando tablero");
    #Creando tablero
    tablero = Tk();
    tablero.title("Buscaminas 0.1");
    tablero.pulsarBotonesAlrededor = pulsarBotonesAlrededor;
    tablero.pulsarBotonesAlrededorSelecc = pulsarBotonesAlrededorSelecc;
    tablero.enPartida = True;
    tablero.fichasJugadas = 0;
    tablero.acabar = acabar;
    tablero.main = main;
    tablero.geometry("230x208");

    
    #Crear minas
    minas = [None] * 10;
    for i in range(0,10):
        boolean = False;
        while not boolean:
            boolean = False;
            number = random.randint(0, 63);
            if number not in minas:
                minas[i] = number;
                print(number//8, number%8);
                boolean = True;
    
    #Creando botones
   
    
    for i in range(0, 8):
        for j in range(0, 8): 
            botones[i][j] = BotonBuscaMinas(tablero, text = "      ");
            botones[i][j].esMina = i*8+j in minas;
            botones[i][j].i = i;
            botones[i][j].j = j;
            if not botones[i][j].esMina:    
                botones[i][j].num = minasAlrededor(i, j, minas);
            botones[i][j].grid(row=i, column=j);
    
    tablero.mainloop();
  
    
def minasAlrededor(i, j, minas):
    minasNum = 0;
    for mina in minas:
        if abs(mina//8 - i) <= 1 and abs(mina%8 - j) <= 1:
            minasNum += 1;
    return minasNum;

def pulsarBotonesAlrededor(i, j):
    if i > 0 and j > 0: 
        if botones[i-1][j-1].estado == 0:
            botones[i-1][j-1].clicked();
    if i > 0 : 
        if botones[i-1][j].estado == 0:
            botones[i-1][j].clicked();
    if i > 0 and j < 7:
        if botones[i-1][j+1].estado == 0:
            botones[i-1][j+1].clicked();
    if j > 0 : 
        if botones[i][j-1].estado == 0:
            botones[i][j-1].clicked();
    if j < 7 :
        if botones[i][j+1].estado == 0:
            botones[i][j+1].clicked();
    if i < 7 and j > 0:
        if botones[i+1][j-1].estado == 0:
            botones[i+1][j-1].clicked();
    if i < 7 :
        if botones[i+1][j].estado == 0:
            botones[i+1][j].clicked();
    if i < 7 and j < 7:
        if botones[i+1][j+1].estado == 0:
            botones[i+1][j+1].clicked();
            
def pulsarBotonesAlrededorSelecc(i, j):
    acum = 0;
    if i > 0 and j > 0: 
        if botones[i-1][j-1].estado == 3:
            acum+=1;
    if i > 0 : 
        if botones[i-1][j].estado == 3:
            acum+=1;
    if i > 0 and j < 7:
        if botones[i-1][j+1].estado == 3:
            acum+=1;
    if j > 0 : 
        if botones[i][j-1].estado == 3:
            acum+=1;
    if j < 7 :
        if botones[i][j+1].estado == 3:
            acum+=1;
    if i < 7 and j > 0:
        if botones[i+1][j-1].estado == 3:
            acum+=1;
    if i < 7 :
        if botones[i+1][j].estado == 3:
            acum+=1;
    if i < 7 and j < 7:
        if botones[i+1][j+1].estado == 3:
            acum+=1;
    if botones[i][j].num == acum:
        pulsarBotonesAlrededor(i, j);
            
def acabar():
    for i in range(8):
        for j in range(8):
            botones[i][j].mostrar();
            
      
    
if __name__ == "__main__":
    main();