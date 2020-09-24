# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:04:27 2020

@author: Raul
"""

from tkinter import Frame

class Tablero(Frame):
      def __init__(self, master):
        Frame.__init__(self, master)
        self.parent = master;
    