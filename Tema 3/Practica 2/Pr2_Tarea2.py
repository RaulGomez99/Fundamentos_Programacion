# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:41:27 2020

@author: Raul
"""
from datetime import datetime
def main():
    segundosAumentar = int(input("Escriba el número de segundos"))
    horasActuales = int(input("Escribe el número de horas actuales"))
    minutosActuales = int(input("Escribe el número de minutos actuales"))
    segundosActuales = int(input("Escribe el número de segundos actuales"))
    segundosActuales += segundosAumentar;
    minutosActuales += segundosActuales // 60;
    segundosActuales %= 60;
    horasActuales += minutosActuales//60;
    minutosActuales %= 60;
    horasActuales %= 24;
    print("La hora actual pasado",segundosAumentar," segundos es:"
          ,str(horasActuales)+":"+str(minutosActuales)+":"+str(segundosActuales))
if __name__ == "__main__":
    main()