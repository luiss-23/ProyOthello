import random 
import sys


#Creacion del tablero
Tablero = [ [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [2, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0] ]
            
print(Tablero)


#Nombres Jugadores
nombreJugador1 = input("Ingrese el nombre del jugador 1: ")
nombreJugador2 = input("Ingrese el nombre del jugador 2: ")

#Variables
fichas = 64
movimientos = 0 

#Eleccion del primer jugador
Jugadores = [1,2]
Turno = random.choice(Jugadores)
print('El primer jugador es: ' +str(Turno))

F = int(input('Introduza la fila donde se hara el movimiento: '))
C = int(input('Introduza la columna donde se hara el movimiento: '))

def cambiarJugador(turn:int) -> 'void':
    if turn==1:
        turn=2
    elif turn==2:
        turn=1
    return turn


def reflejarJugada( A: [int], i: int, j: int, turno: int) -> 'void':
    A[i][j] = turno

def consumoVertical(A:[int], i:int, j:int, turno:int) -> 'void':
    for i in range(0,8):
        if ( A[i][j] == turno ):
            if ( A[i+1][j] != 0 and A[i+1][j] != turno ):
                A[i+1][j] = turno
                consumoVertical(A, i + 1, j, turno)
            elif ( A[i-1][j] != 0 and A[i-1][j] != turno ):
                A[i-1][j] == turno
                consumoVertical(A, i - 1, j, turno)
            elif ( A[i+1][j] == 0 or A[i+1][j] == turno ):
                break
            elif ( A[i-1][j] == 0 or A[i-1][j] == turno):
                break
        else:
            pass

def consumoHorizontal(A:[int], i:int, j:int, turno:int) -> 'void':
    for j in range(0,8):
        if ( A[i][j] == turno ):
            if ( A[i][j+1] != 0 and A[i][j+1] != turno ):
                A[i][j+1] = turno
                consumoHorizontal(A, i, j+1, turno)
            elif ( A[i][j-1] != 0 and A[i][j-1] != turno ):
                A[i][j-1] == turno
                consumoHorizontal(A, i, j-1, turno)
            elif ( A[i][j+1] == 0 or A[i][j+1] == turno ):
                break
            elif ( A[i][j-1] == 0 or A[i][j-1] == turno):
                break
        else:
            pass

reflejarJugada(Tablero, F, C, Turno)
consumoVertical(Tablero, F, C, Turno)
consumoHorizontal(Tablero, F, C, Turno)
print(Tablero)