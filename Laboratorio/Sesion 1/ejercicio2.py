# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:48:55 2020

Es un programa que nos calcula el precio y la cantidad de cubos de una empresa

@author: Raúl e Iker
"""

PRECIO_CUBO_PINTURA = 19.95
LITROS_BARNIZ_METRO_CUADRADO = 0.5
BANCOS_TIPO_1_ALTURA = 100
BANCOS_TIPO_1_ANCHURA = 50
BANCOS_TIPO_2_ALTURA = 50
BANCOS_TIPO_2_ANCHURA = 50
MANOS_POR_TABLERO = 2
TAMANYO_CUBOS_BARNIZ = 5

def main():
    #ENTRADA DE DATOS
    numeroDeBancosTipo1 = int(input("Escriba número de bancos tipo 1"));
    numeroDeBancosTipo2 = int(input("Escriba número de bancos tipo 2"));
    
    #PROCESAMIENTO DE DATOS
    metrosCuadradosTotal1 = ((numeroDeBancosTipo1 * BANCOS_TIPO_1_ALTURA * BANCOS_TIPO_1_ANCHURA) * 2) / 100;
    metrosCuadradosTotal2 = ((numeroDeBancosTipo2 * BANCOS_TIPO_2_ALTURA * BANCOS_TIPO_2_ANCHURA) * 2) / 100;
    metrosCuadradosTotal = (metrosCuadradosTotal1 + metrosCuadradosTotal2) * MANOS_POR_TABLERO; 
    
    litrosBarnizNecesario = metrosCuadradosTotal * LITROS_BARNIZ_METRO_CUADRADO;
    
    cubosNecesarios = litrosBarnizNecesario / TAMANYO_CUBOS_BARNIZ;
    
    
    precioCubos = cubosNecesarios * PRECIO_CUBO_PINTURA;
    
    #SALIDA DE DATOS
    print("Cubos necesarios para pintar", numeroDeBancosTipo1, "bancos de tipo 1 y", numeroDeBancosTipo2, "bancos de tipo 2:", cubosNecesarios);
    print("El precio de", cubosNecesarios, "es de:", precioCubos)
    

    
if __name__ == "__main__":
    main();