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


enPartida = True;
turnosJugados = 0;
turno =True; #True es X False es O
tablero = [None] * 9;
while enPartida:
    if turno: print("Turno de X");
    else: print("Turno de O");
    
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
    if turno: tablero[((fila-1)*3+columna-1)] = "X";
    else : tablero[((fila-1)*3+columna-1)] = "O";
    imprimeTablero(tablero)
    if compruebaVictoria(tablero) != False:
        enPartida = False;
        print("Ha ganado "+compruebaVictoria(tablero))
    else:
        turno = not turno;
        turnosJugados+=1;
        if turnosJugados == 9 :
            enPartida = False;
            print("Empate")
    
    
    