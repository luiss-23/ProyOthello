import random 
import sys

#Creacion del tablero
Tablero = [ [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
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

