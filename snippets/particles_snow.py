# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Pygame swap text with another text
# https://stackoverflow.com/questions/60944070/pygame-swap-text-with-another-text/60953697#60953697
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Particles
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame
import random

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

particles = []

def starting_point():
	" to make a flame like particles [150, 20] # flame"
	return random.randint(0, 300)
	# return 150

snow = pygame.image.load("img/snow.png")

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # it adds particles untile they are removed
    # if the size - [2] - is smaller than 0
    particles.append([
    	[starting_point(), 0],
    	[random.randint(0, 20) / 10 - 1, 2],
    	random.randint(4, 6)])
    for particle in particles[:]:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.005 # how fast circles shrinks
        particle[1][1] += 0.01 # circles speed
        if particle[2] <= 0:
            particles.remove(particle)

    window.blit(snow, (0,0)) 
    for particle in particles:
        pygame.draw.circle(
        	window,
        	(255, 255, 255),
        	(
        		round(particle[0][0]),
        		round(particle[0][1])),
        		round(particle[2]))
    pygame.display.flip()

pygame.quit()
exit()
