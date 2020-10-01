# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:20:51 2020

@author: Raul
"""

from tkinter import Button, messagebox;

class BotonBuscaMinas(Button):
    
    num, estado = 0, 0;
    i, j, esMina = None, None, None;
    
    def __init__(self, master=None, cnf={}, **kw):
        Button.__init__(self, master=None, cnf={}, **kw);
        self.config(command = self.clicked, bg = "gray");
        self.bind('<Button-3>', self.rightClick)

    def clicked(self):
        if (self.estado != 0 and self.estado != 1) or not self.master.enPartida: return;
        if self.estado == 1 :
            self.master.pulsarBotonesAlrededorSelecc(self.i, self.j);
            return;
        if not self.esMina:
            self.configure(text="  "+str(self.num)+"  ");
            if self.num == 0:
                self.estado = 1;
                self.master.pulsarBotonesAlrededor(self.i, self.j);  
            self.master.fichasJugadas += 1;
            if self.master.fichasJugadas >= 54:
                self.master.acabar();
                messagebox.showinfo("Victoria", "Ehnorabuena ganaste!!!!")
                self.master.enPartida = False;
                main = self.master.main;
                self.master.destroy();
                main();
        else:
            self.master.enPartida = False;
            self.configure(bg="red");
            self.master.acabar();
            messagebox.showinfo("Derrota", "Perdiste intentelo otro ía")
            main = self.master.main;
            self.master.destroy();
            main();
            
        self.estado = 1;
        
    def rightClick(self, event):
        if self.estado != 1 and self.master.enPartida:
            if self.estado == 0:
                self.estado = 3;
                self.configure(bg="blue");
            else:
                self.estado = 0;
                self.configure(bg="gray");
        
    def iniciacion(self, esMina, num):
        self.esMina = esMina;
        self.num = num;
        
    def mostrar(self):
        if self.esMina: self.configure(bg="red");
        else:
            self.configure(text="  "+str(self.num)+"  ", bg="gray");            
            