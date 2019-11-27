import pygame
import sys
import random

pygame.display.set_caption("Reversi")
pygame.init()
position=()
width = 400
height = 400
red=(255,0,0)
white=(255,255,255)
turno=0
clock = pygame.time.Clock()
window = pygame.display.set_mode((width, height))
Jugadores = [1,2]

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

#Nombres Jugadores
nombreJugador1 = input("Ingrese el nombre del jugador 1(Rojo): ")
nombreJugador2 = input("Ingrese el nombre del jugador 2(Blanco): ")
Turno = random.choice(Jugadores)
print('El primer jugador es: ' +str(Turno))

#Variables
fichas = 60
movimientos = 0 

def boardPos (mouseX, mouseY):
    if (mouseY < 50):
        row = 0
    elif (mouseY < 100):
        row = 1
    elif (mouseY <150):
        row = 2
    elif (mouseY < 200):
        row = 3
    elif (mouseY <250):
        row = 4    
    elif (mouseY <300):
        row = 5
    elif (mouseY <350):
        row = 6
    elif (mouseY < 400):
        row = 7
    if (mouseX < 50):
        col = 0
    elif (mouseX < 100):
        col = 1
    elif (mouseX <150):
        col = 2
    elif (mouseX < 200):
        col = 3
    elif (mouseX <250):
        col = 4    
    elif (mouseX <300):
        col = 5
    elif (mouseX <350):
        col = 6
    elif (mouseX < 400):
        col = 7
    return (row, col)

def esValida(A:[int],B:[int],i:int,j:int,turneto:int)->bool:
    Valida=False
    if A[i][j]!=0:
        pass
    elif A[i][j] == 0:
        for a in range (0,8):
            for b in range (0,8):
                B[a][b]=A[a][b]
        consumo(B, i, j,turneto)
        reflejarJugada(B,i,j,turneto)
        for a in range (0,8):
            for b in range (0,8):
                if a==i and b==j:
                    pass
                elif a!=i or b!=j:
                    if A[a][b]==B[a][b]:
                        pass
                    elif A[a][b]!=B[a][b]:
                        Valida=True 
    return Valida

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
        while i <7 and j <7:
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
    if F-R==0:
        quedan=False
    elif F-R!=0:
        quedan=True
    return quedan

def consumo(A:[int], i:int, j:int, turno:int) -> 'void':
    consumoDiagonal(A, i, j, Turno)
    consumoHorizontal(A, i, j, Turno)
    consumoVertical(A, i, j, Turno)

def QuedanJugadas(A:[int],B:[int],turno:int)->bool:
    Quedan=False
    for x in range(0,8):
        for y in range (0,8):
            if A[x][y]==0:
                if esValida(A,B,x,y,turno):
                    Quedan=True
                else:
                    pass
            elif A[x][y]==1 or A[x][y]==2:
                pass
    return Quedan
    
game_over = False

pygame.draw.line(window, (255,255,255),(50,400),(50,0),2)
pygame.draw.line(window, (255,255,255),(100,400),(100,0),2)
pygame.draw.line(window, (255,255,255),(150,400),(150,0),2)
pygame.draw.line(window, (255,255,255),(200,400),(200,0),2)
pygame.draw.line(window, (255,255,255),(250,400),(250,0),2)
pygame.draw.line(window, (255,255,255),(300,400),(300,0),2)
pygame.draw.line(window, (255,255,255),(350,400),(350,0),2)
pygame.draw.line(window, (255,255,255),(0,50),(400,50),2)
pygame.draw.line(window, (255,255,255),(0,100),(400,100),2)
pygame.draw.line(window, (255,255,255),(0,150),(400,150),2)
pygame.draw.line(window, (255,255,255),(0,200),(400,200),2)
pygame.draw.line(window, (255,255,255),(0,250),(400,250),2)
pygame.draw.line(window, (255,255,255),(0,300),(400,300),2)
pygame.draw.line(window, (255,255,255),(0,350),(400,350),2)
pygame.draw.circle(window,red,(175,225),20)
pygame.draw.circle(window,red,(225,175),20)
pygame.draw.circle(window,white,(175,175),20)
pygame.draw.circle(window,white,(225,225),20)

while not game_over:
	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if quedanFichas(fichas, movimientos) == True and (QuedanJugadas(Tablero,Copia,1)==True or QuedanJugadas(Tablero,Copia,2)==True):
                if QuedanJugadas(Tablero,Copia,Turno):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (mouseX, mouseY) = pygame.mouse.get_pos()
                        (row, col) = boardPos (mouseX, mouseY)
                        F=row
                        C=col
                        centerX = ((col) * 50)+25
                        centerY = ((row) * 50)+25

                        if Turno==1:
                            color=red

                        elif Turno==2:
                            color=white

                        if esValida(Tablero,Copia,F,C,Turno)==True:
                                pygame.draw.circle(window,color,(centerX,centerY),20)
                                consumo(Tablero, F, C, Turno)
                                reflejarJugada(Tablero, F, C, Turno)
                                Turno = cambiarJugador(Turno)
                                print("El turno es del jugador:", Turno)
                                for i in range (0,8):
                                    for j in range(0,8):
                                        if Tablero[i][j]==1:
                                            color=red
                                            row=i
                                            col=j
                                            centerX = ((col) * 50)+25
                                            centerY = ((row) * 50)+25
                                            pygame.draw.circle(window,color,(centerX,centerY),20)
                                        elif Tablero[i][j]==2:
                                            color=white
                                            row=i
                                            col=j
                                            centerX = ((col) * 50)+25
                                            centerY = ((row) * 50)+25
                                            pygame.draw.circle(window,color,(centerX,centerY),20)
                                        else: pass
                        elif esValida(Tablero,Copia,F,C,Turno)==False:
                            print("La jugada introducida no es valida.")
                            print("Para que una jugada sea valida, la casilla no debe estar ocupada por una ficha y se deben consumir almenos una ficha.")
                else: 
                    Ext=Turno
                    Turno = cambiarJugador(Turno)
                    print("El jugador", Ext, "no pude hacer movimientos.")
                    print("El turno es del jugador", Turno)            
            else: 
                print("Se termina el juego porque no se pueden colocar mas fichas")
                sys.exit()
                
            pygame.display.update()

	clock.tick(10)
				
	

			



	
	