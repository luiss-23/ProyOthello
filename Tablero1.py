import pygame
import sys

pygame.display.set_caption("Reversi")
pygame.init()
position=()
width = 400
height = 400
red=(255,0,0)
white=(255,255,255)

window = pygame.display.set_mode((width, height))

game_over = False

while not game_over:

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
	
	turno=0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if turno%2==0:
			color=red
			turno=turno+1
		elif turno%2!=0:
			color=white
			turno=turno+1
		if event.type == pygame.MOUSEBUTTONDOWN:
			position = pygame.mouse.get_pos()
			pygame.draw.circle(window,color,position,20)
	

			



	print(event)
	print(position)
	pygame.display.update()