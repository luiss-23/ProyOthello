import pygame
import sys

pygame.init()

width = 800
height = 800

window = pygame.display.set_mode((width, height))

game_over = False

while not game_over:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

	pygame.draw.rect(window, (255,0,0), (400, 400, 50, 50))

	pygame.display.update()