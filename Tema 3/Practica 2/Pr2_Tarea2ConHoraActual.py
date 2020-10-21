# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:41:27 2020

@author: Raul
"""
from datetime import datetime
def main():
    segundosAumentar = int(input("Escriba el número de segundos"))
    horaActual = datetime.now();
    segundosActuales = horaActual.second + segundosAumentar;
    minutosActuales = horaActual.minute + segundosActuales // 60;
    segundosActuales %= 60;
    horasActuales = horaActual.hour + minutosActuales//60;
    minutosActuales %= 60;
    horasActuales %= 24;
    print("La hora actual es:",horaActual)
    print("La hora actual pasado",segundosAumentar," segundos es:"
          ,str(horasActuales)+":"+str(minutosActuales)+":"+str(segundosActuales))
if __name__ == "__main__":
    main()