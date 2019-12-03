import pygame
import sys
import random

clock = pygame.time.Clock() #Para ver los eventos a velocidad normal

#Inicializacion de pygame
pygame.init()

position = ()

#Tamano de la ventana de juego
width = 1000
height = 1000

#Colores de las fichas y del fondo del tablero de juego
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FOREST_GREEN = (34, 139, 34)


#Nombre de la ventana de juego
pygame.display.set_caption("Othello")
#Inicializacion de la ventana de juego
window = pygame.display.set_mode((width, height))

#Matriz asociada al tablero de juego
Tablero = [ [0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 2, 1, 0, 0, 0],
			[0, 0, 0, 1, 2, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0] ]

#Matriz copia usada para la funcion esValida
Copia =   [ [0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0] ]

#Fichas y movimientos
fichas = 60
movimientos = 0
puntaje_1 = 0
puntaje_2 = 0 

#Funciones para poder jugar
def boardPos(mouseX, mouseY):
	#Numero de fila dado por la posicion de click
	if (mouseY < 100):
		row = -1 
	elif (mouseY < 200):
		row = 0
	elif (mouseY < 300):
		row = 1
	elif (mouseY < 400):
		row = 2
	elif (mouseY < 500):
		row = 3
	elif (mouseY < 600):
		row = 4
	elif (mouseY < 700):
		row = 5
	elif (mouseY < 800):
		row = 6
	elif (mouseY < 900):
		row = 7 
	elif (mouseY < 1000):
		row = -1

	#Numero de columna dado por la posicion de click
	if (mouseX < 100):
		col = -1
	elif (mouseX < 200):
		col = 0
	elif (mouseX < 300):
		col = 1
	elif (mouseX < 400):
		col = 2
	elif (mouseX < 500):
		col = 3
	elif (mouseX < 600):
		col = 4
	elif (mouseX < 700):
		col = 5
	elif (mouseX < 800):
		col = 6
	elif (mouseX < 900):
		col = 7 
	elif (mouseX<1000):
		col = -1
	return (row, col)

def esValida(A:[int], B:[int], i:int, j:int, turneto:int) -> bool:
	Valida = False
	if A[i][j] != 0:
		pass
	elif A[i][j] == 0:
		for a in range (0,8):
			for b in range (0,8):
				B[a][b] = A[a][b]
		consumo(B, i, j,turneto)
		reflejarJugada(B, i, j, turneto)
		for a in range (0,8):
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
				i = 7        
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
				i = 0
	elif i == 0:
		pass 

def consumoHorizontal(A:[int], i:int, j:int, turno:int) -> 'void':
	k = int
	k = j
	if j != 7:
		while j < 7:
			if A[i][j+1] != turno and A[i][j+1] != 0:
				j = j+1
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

def QuedanJugadas(A:[int],B:[int],turno:int) -> bool:
	Quedan = False
	for i in range(0,8):
		for j in range (0,8):
			if A[i][j] == 0:
				if esValida(A, B, i, j, turno):
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


#Nombres de Jugadores
nombreJugador1 = input("Ingrese el nombre de uno de los jugadores:")
nombreJugador2 = input("Ingrese el nombre del otro jugador:")
Nombres=[nombreJugador1,nombreJugador2]

#Eleccion del primer y segundo jugador 

Turno = 1
p1=(random.choice(Nombres))
print( 'El jugador que tiene el primer movimiento (Jugador 1, Fichas negras) es: ' +str(p1))

if p1==Nombres[0]:
	p2=Nombres[1]
elif p1==Nombres[1]:
	p2=Nombres[0]

game_over = False

#Dibujo de fondo del tablero
pygame.draw.rect(window, FOREST_GREEN, (100,100, 800,800))

#Dibujo de lineas del tablero, horizontales y verticales
pygame.draw.line(window, (0,0,0), (200,900), (200,100), 2)
pygame.draw.line(window, (0,0,0), (300,900), (300,100), 2)
pygame.draw.line(window, (0,0,0), (400,900), (400,100), 2)
pygame.draw.line(window, (0,0,0), (500,900), (500,100), 2)
pygame.draw.line(window, (0,0,0), (600,900), (600,100), 2)
pygame.draw.line(window, (0,0,0), (700,900), (700,100), 2)
pygame.draw.line(window, (0,0,0), (800,900), (800,100), 2)

pygame.draw.line(window, (0,0,0), (100,200), (900,200), 2)
pygame.draw.line(window, (0,0,0), (100,300), (900,300), 2)
pygame.draw.line(window, (0,0,0), (100,400), (900,400), 2)
pygame.draw.line(window, (0,0,0), (100,500), (900,500), 2)
pygame.draw.line(window, (0,0,0), (100,600), (900,600), 2)
pygame.draw.line(window, (0,0,0), (100,700), (900,700), 2)
pygame.draw.line(window, (0,0,0), (100,800), (900,800), 2)

#Dibujo de las fichas iniciales del juego
pygame.draw.circle(window, WHITE, (450,450), 40)
pygame.draw.circle(window, WHITE, (550,550), 40)
pygame.draw.circle(window, BLACK, (450,550), 40)
pygame.draw.circle(window, BLACK, (550,450), 40)

while not game_over:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

		if quedanFichas(fichas, movimientos) == True and (QuedanJugadas(Tablero,Copia,1)==True or QuedanJugadas(Tablero,Copia,2)==True):
			if QuedanJugadas(Tablero, Copia, Turno) == True:
				if event.type == pygame.MOUSEBUTTONDOWN:
					(mouseX, mouseY) = pygame.mouse.get_pos()
					(row, col) = boardPos(mouseX, mouseY)
					if row == -1 or col == -1:
						print("Debe seleccionar una casilla dentro del tablero")
					elif row != -1 and col != -1:
						F, C = row, col 
						centerX = ((col) * 100) + 150
						centerY = ((row) * 100) + 150

					if Turno == 1:
						color = BLACK
					elif Turno == 2:
						color = WHITE

					if esValida(Tablero, Copia, F, C, Turno):
						pygame.draw.circle(window, color, (centerX,centerY), 40)
						consumo(Tablero, F, C, Turno)
						reflejarJugada(Tablero, F, C, Turno)
						puntaje_1 = puntaje1(Tablero, puntaje_1, F, C)
						puntaje_2 = puntaje2(Tablero, puntaje_2, F, C)
						print("El jugador",p1," tiene acumulados:"  +str(puntaje_1) + " puntos.")
						print("El jugador",p2," tiene acumulados:"  +str(puntaje_2) + " puntos.")
						puntaje_1 = 0
						puntaje_2 = 0 
						Turno = cambiarJugador(Turno)
						if Turno == 1:
							prox= p1
						elif Turno == 2:
							prox = p2
						print('El siguiente jugador es: ' +str(prox))
						for i in range(0,8):
							for j in range(0,8):
								if Tablero[i][j] == 1:
									color = BLACK
									row = i 
									col = j
									centerX = ((col) * 100) + 150
									centerY = ((row) * 100) + 150
									pygame.draw.circle(window, color, (centerX,centerY), 40)
								elif Tablero[i][j] == 2:
									color = WHITE
									row = i 
									col = j
									centerX = ((col) * 100) + 150
									centerY = ((row) * 100) + 150
									pygame.draw.circle(window, color, (centerX,centerY), 40)
								else: 
									pass
					else:
						print('La jugada introducida no es valida, intente nuevamente')
			else:
				if Turno == 1:
					ant= p1
					prox= p2
				elif Turno == 2:
					ant= p2
					prox = p1
				Turno = cambiarJugador(Turno)
				print('El jugador: ' +str(ant) +' no tiene jugadas, el turno del jugador: ' +str(prox))
		else: 
			if quedanFichas(fichas, movimientos) == False:
				print('No quedan fichas para jugar, se termina el juego')
				puntaje_1 = puntaje1(Tablero, puntaje_1, F, C)
				puntaje_2 = puntaje2(Tablero, puntaje_2, F, C)
				if puntaje_1 > puntaje2:
					print("El ganador es:",p1,"Felicidades.")
				else:
					print("El ganador es:",p2,"Felicidades.")
				sys.exit()
			elif ( QuedanJugadas(Tablero,Copia,1) == False and QuedanJugadas(Tablero,Copia,2) == False ):
				print('El juego ha acabado porque ningun jugador tiene movimientos validos para hacer.')
				puntaje_1 = puntaje1(Tablero, puntaje_1, F, C)
				puntaje_2 = puntaje2(Tablero, puntaje_2, F, C)
				if puntaje_1 > puntaje2:
					print("El ganador es:",p1,"Felicidades.")
				else:
					print("El ganador es:",p2,"Felicidades.")
				sys.exit()

		pygame.display.update()

	clock.tick(5)