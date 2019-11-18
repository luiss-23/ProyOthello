import pygame, sys
from pygame.locals import *

SaddleBrown = (139, 69, 19)
SandyBrown = (244, 164, 96)
FONDO = (24, 25, 30)


#Creacion de la ventana y titulo de la ventana 
venta = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("SKEREEEEEEEE")


#Dibujar tablero
def dibujarTablero(screen, dimension):
	color = 0 
	for i in range(8):
		for j in range(8):
			x, y = i * dimension, j * dimension
			if color % 2 == 0:
				pygame.draw.rect(screen, SaddleBrown, [x, y, dimension, dimension], 0)
			else:
				pygame.draw.rect(screen, SandyBrown, [x, y, dimension, dimension], 0)
			color += 1
		color += 1

pygame.init()
#Comenzamos el juego
while True:
    venta.fill(FONDO)
    dibujarTablero(venta, 100)
    pygame.display.flip
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update

