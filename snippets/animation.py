import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))

def load_image(img):
	"loads an image"
	try:
		return pygame.image.load(img)
	except FileNotFoundError:
		print(f"file {img} not found")

def blit(image, x, y):
	return screen.blit(image, (x, y))

star = load_image("..\\img\\star.png")

def stop_game(loop):
	"How to quit the game"
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0
	pygame.display.update()
	return loop

def animations():
	blit(star, 100, 100)

def mainloop():
	"The games start here cheching for user input\
	and blitting images"
	loop = 1
	while loop:
			loop = stop_game(loop)
			animations()
	pygame.quit()
	sys.exit()

mainloop()