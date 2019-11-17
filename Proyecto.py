import random 
import sys


#Creacion del tablero
Tablero = [ [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 2, 2, 1, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0],
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
    k=int
    k=i
    if i!=7:
        while i<7:
            if A[i+1][j]!=turno and A[i+1][j]!=0:
                i=i+1
            elif A[i+1][j]==0:
                i=7
            elif A[i+1][j]==turno:
                for t in range (k,i+1):
                    A[t][j]=turno  
                i=7        
    elif i==7:
        pass
    i=k
    if i!=0:
        while i>0:
            if A[i-1][j]!=turno and A[i-1][j]!=0:
                i=i-1
            elif A[i-1][j]==0:
                i=0
            elif A[i-1][j]==turno:
                for z in range (i-1,k):
                    A[z][j]=turno
                i=0
    elif i==0:
        pass 

def consumoHorizontal(A:[int], i:int, j:int, turno:int) -> 'void':
    k=int
    k=j
    if j!=7:
        while j<7:
            if A[i][j+1]!=turno and A[i][j+1]!=0:
                j=j+1
            elif A[i][j+1]==0:
                j=7
            elif A[i][j+1]==turno:
                for t in range (k,j+1):
                    A[i][t]=turno  
                j=7        
    elif j==7:
        pass
    j=k
    if j!=0:
        while j>0:
            if A[i][j-1]!=turno and A[i][j-1]!=0:
                j=j-1
            elif A[i][j-1]==0:
                j=0
            elif A[i][j-1]==turno:
                for z in range (j-1,k):
                    A[i][z]=turno
                j=0
    elif j==0:
        pass 

def consumoDiagonal(A:[int], i:int, j:int, turno:int) -> 'void':
    k = i
    l = j
    if i != 0 and j != 7:
        while i > 0 or j < 7:
            if A[i-1][j+1] != turno and A[i-1][j+1] != 0:
                i = i - 1
                j = j + 1
            elif A[i-1][j+1] == 0:
                i = 0
            elif A[i-1][j+1] == turno:
                i = k
                for r in range(l,j+1):
                    A[i][r] = turno
                    i = i - 1
                i = 0
    elif i == 0 and j == 7:
        pass
    i = k

reflejarJugada(Tablero, F, C, Turno)
consumoDiagonal(Tablero, F, C, Turno)

print(Tablero)