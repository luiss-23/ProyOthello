import random 
import sys


#Creacion del tablero
Tablero = [ [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0] ]

Copia =   [ [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0] ]

for i in range(len(Tablero)):
    for j in range(len(Tablero[i])):
        print(Tablero[i][j], end=' ')
    print()


#Nombres Jugadores
nombreJugador1 = input("Ingrese el nombre del jugador 1: ")
nombreJugador2 = input("Ingrese el nombre del jugador 2: ")

#Variables
fichas = 60
movimientos = 0 
puntaje_1 = 0
puntaje_2 = 0

#Eleccion del primer jugador
Jugadores = [1,2]

def esValida(A:[int],B:[int],i:int,j:int,turneto:int)->bool:
    Valida = False
    if A[i][j] != 0:
        pass
    elif A[i][j] == 0:
        for a in range(0,8):
            for b in range(0,8):
                B[a][b] = A[a][b]
        consumo(B, i, j,turneto)
        reflejarJugada(B,i,j,turneto)
        for a in range(0,8):
            for b in range (0,8):
                if a == i and b == j:
                    pass
                elif a != i or b != j:
                    if A[a][b] == B[a][b]:
                        pass
                    elif A[a][b] != B[a][b]:
                        Valida = True 
    return Valida

def cambiarJugador(turn:int) -> 'void':
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    return turn


def reflejarJugada( A: [int], i: int, j: int, turno: int) -> 'void':
    A[i][j] = turno

def consumoVertical(A:[int], i:int, j:int, turno:int) -> 'void':
    k = int
    k = i
    if i != 7:
        while i < 7:
            if A[i+1][j] != turno and A[i+1][j] != 0:
                i = i + 1
            elif A[i+1][j] == 0:
                i = 7
            elif A[i+1][j] == turno:
                for t in range(k,i+1):
                    A[t][j] = turno  
                i=7        
    elif i == 7:
        pass
    i = k
    if i != 0:
        while i > 0:
            if A[i-1][j] != turno and A[i-1][j] != 0:
                i = i - 1
            elif A[i-1][j] == 0:
                i = 0
            elif A[i-1][j] == turno:
                for z in range(i-1,k):
                    A[z][j] = turno
                i=0
    elif i == 0:
        pass 

def consumoHorizontal(A:[int], i:int, j:int, turno:int) -> 'void':
    k = int
    k = j
    if j != 7:
        while j < 7:
            if A[i][j+1] != turno and A[i][j+1] != 0:
                j = j + 1
            elif A[i][j+1] == 0:
                j = 7
            elif A[i][j+1] == turno:
                for t in range(k,j+1):
                    A[i][t] = turno  
                j = 7        
    elif j == 7:
        pass
    j = k
    if j != 0:
        while j > 0:
            if A[i][j-1] != turno and A[i][j-1] != 0:
                j = j - 1
            elif A[i][j-1] == 0:
                j = 0
            elif A[i][j-1] == turno:
                for z in range(j-1,k):
                    A[i][z] = turno
                j = 0
    elif j == 0:
        pass 

def consumoDiagonal(A:[int], i:int, j:int, turno:int) -> 'void':
    k = i
    l = j
    if i != 0 and j != 7:
        while i > 0 and j < 7:
            if A[i-1][j+1] != turno and A[i-1][j+1] != 0:
                i = i - 1
                j = j + 1
            elif A[i-1][j+1] == 0:
                i = 0
                j = 7
            elif A[i-1][j+1] == turno:
                i = k
                for r in range(l,j+1):
                    A[i][r] = turno
                    i = i - 1
                i = 0
                j = 7
    elif i == 0 or j == 7:
        pass
    
    i = k
    j = l

    if i != 7 and j != 7:
        while i < 7 and j < 7:
            if A[i+1][j+1] != turno and A[i+1][j+1] != 0:
                i = i + 1
                j = j + 1
            elif A[i+1][j+1] == 0:
                i = 7
                j = 7
            elif A[i+1][j+1] == turno:
                i = k
                for r in range(l,j+1):
                    A[i][r] = turno
                    i = i + 1
                i = 7
                j = 7
    elif i == 7 or j == 7:
        pass
    
    i=k
    j=l

    if i != 7 and j != 0:
        while i < 7 and j > 0:
            if A[i+1][j-1] != turno and A[i+1][j-1] != 0:
                i = i + 1
                j = j - 1
            elif A[i+1][j-1] == 0:
                i = 7
                j = 0
            elif A[i+1][j-1] == turno:
                j = l
                for r in range(k,i+1):
                    A[r][j] = turno
                    j = j - 1
                i = 7
                j = 0
    elif i == 7 or j == 0:
        pass
    
    i=k
    j=l

    if i != 0 and j != 0:
        while i > 0 and j > 0:
            if A[i-1][j-1] != turno and A[i-1][j-1] != 0:
                i = i - 1
                j = j - 1
            elif A[i-1][j-1] == 0:
                i = 0
                j = 0
            elif A[i-1][j-1] == turno:
                for r in range(i-1,k):
                    A[r][j-1] = turno
                    j = j + 1
                i = 0
                j = 0
    elif i == 0 or j == 0:
        pass

def quedanFichas(F:int,R:int)->bool:
    if F - R == 0:
        quedan = False
    elif F - R != 0:
        quedan = True
    return quedan

def consumo(A:[int], i:int, j:int, turno:int) -> 'void':
    consumoDiagonal(A, i, j, turno)
    consumoHorizontal(A, i, j, turno)
    consumoVertical(A, i, j, turno)

def QuedanJugadas(A:[int],B:[int],turno:int)->bool:
    Quedan = False
    for i in range(0,8):
        for j in range (0,8):
            if A[i][j] == 0:
                if esValida(A,B,i,j,turno):
                    Quedan = True
                else:
                    pass
            elif A[i][j] == 1 or A[i][j] == 2:
                pass
    return Quedan

def puntaje1(A: [int], p1:int, i: int, j: int) -> int:
    for i in range(0,8):
        for j in range(0,8):
                if A[i][j] == 0:
                    pass
                elif A[i][j] == 2:
                    pass
                elif A[i][j] == 1:
                    p1 = p1 + 1

    return p1

def puntaje2(A: [int], p2:int, i: int, j: int) -> int:
    for i in range(0,8):
        for j in range(0,8):
                if A[i][j] == 0:
                    pass
                elif A[i][j] == 1:
                    pass
                elif A[i][j] == 2:
                    p2 = p2 + 1

    return p2

Turno = random.choice(Jugadores)
print('El primer jugador es: ' +str(Turno))

while quedanFichas(fichas, movimientos) and (QuedanJugadas(Tablero,Copia,1) or QuedanJugadas(Tablero,Copia,2)):
    if  QuedanJugadas(Tablero, Copia, Turno) == True :
        F = int(input('Introduza la fila donde se hara el movimiento: '))
        C = int(input('Introduza la columna donde se hara el movimiento: '))
        if esValida(Tablero,Copia,F,C,Turno):
            consumo(Tablero, F, C, Turno)
            reflejarJugada(Tablero, F, C, Turno)
            puntaje_1 = puntaje1(Tablero, puntaje_1, F, C)
            puntaje_2 = puntaje2(Tablero, puntaje_2, F, C)
            for i in range(len(Tablero)):
                for j in range(len(Tablero[i])):
                    print(Tablero[i][j], end=' ')
                print()
            print('El jugador 1, lleva: ' +str(puntaje_1))
            print('El jugador 2, lleva: ' +str(puntaje_2))
            puntaje_1 = 0
            puntaje_2 = 0 
            Turno = cambiarJugador(Turno)
            print('El siguiente jugador es: ' +str(Turno))
            movimientos = movimientos + 1
        else:
            print("La jugada introducida no es valida.")
            print("Para que una jugada sea valida, la casilla no debe estar ocupada por una ficha y se deben consumir almenos una ficha.")
    else:
        print("EL jugador", Turno,"no tiene jugadas disponibles.")
        Turno = cambiarJugador(Turno)
        print('El turno es para el jugador: ' +str(Turno))
if QuedanJugadas(Tablero,Copia,1)==False and QuedanJugadas(Tablero,Copia,2)==False:
    print("El juego ha acabado porque ningun jugador tiene movimientos.")
elif quedanFichas(fichas,movimientos)==False:
    print("El juego ha terminado, no quedan fichas para jugar en el tablero.")