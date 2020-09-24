condiciones = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]    
]

def compruebaVictoria(tablero):
    for condicion in condiciones:
        if(tablero[condicion[0]] == tablero[condicion[1]] 
           and tablero[condicion[1]] == tablero[condicion[2]] 
           and tablero[condicion[0]]!= None):
            return tablero[condicion[0]];
    return False;    


def imprimeTablero(tablero):
    print("-------------")
    for i in range(0,3):
        for j in range(0,3):
            if(tablero[i*3+j]==None): print("|   ", end = '');
            else :
                print("| ", end = '');
                print(tablero[i*3+j]+" ", end = '');
            if j == 2: print("|")
        print("-------------")
     
casillasPreferentes = [4, 0, 2, 6, 8, 1, 3, 5, 7]

def compruebaPosibleVictoriaIA(tablero, letra):
    for i in range(0, 9):
        if tablero[i] == None:
            tablero[i] = letra;
            if compruebaVictoria(tablero) == letra: 
                tablero[i] = "O";
                return tablero;
            tablero[i] = None;
    return False;

def casillaPreferente(tablero):
    for coords in casillasPreferentes:
        if tablero[coords] == None:
            tablero[coords] = "O";
            return tablero;

#-------------------------------------

enPartida = True;
turnosJugados = 0;
turno =True; #True es X False es O
tablero = [None] * 9;
while enPartida:
    if turno: print("Turno de X");
    else: print("Turno de O");
    if turno:
        celdaValida = False;
        while not celdaValida:
            correctNum = False;
            while not correctNum:
                try:
                    fila = int(input("Escriba número de fila"));
                    if fila > 0 and fila <= 3: 
                        correctNum = True;
                    else:
                        print("Debe ser un número entre 1 y 3")
                except:
                    print("Debe ser un número");
            correctNum = False;
            while not correctNum:
                try:
                    columna = int(input("Escriba número de columna"));
                    if columna > 0 and columna <= 3: 
                        correctNum = True;
                    else:
                        print("Debe ser un número entre 1 y 3")
                except:
                    print("Debe ser un número");
            if tablero[((fila-1)*3+columna-1)] == None:
                celdaValida = True;
                print("Celda ya ocupada")
        tablero[((fila-1)*3+columna-1)] = "X";
    else:
        if not compruebaPosibleVictoriaIA(tablero, "O"):
            if not compruebaPosibleVictoriaIA(tablero, "X"):
                tablero = casillaPreferente(tablero)
    imprimeTablero(tablero)
    if compruebaVictoria(tablero):
        enPartida = False;
        print("Ha ganado "+compruebaVictoria(tablero))
    else:
        turno = not turno;
        turnosJugados+=1;
        if turnosJugados == 9 :
            enPartida = False;
            print("Empate")