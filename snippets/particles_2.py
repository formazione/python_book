import pygame
import random

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

particles1 = []
particles2 = []
particles3 = []
def particles_run(particles, pos, color):
    particles.append([
    	[random.randint(0, 300), # it was centered at 150
    	0],
    	[random.randint(0, 20) / 10 - 1, 2],
    	random.randint(4,6)])
    for particle in particles[:]:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.005 # how fast circles shrinks
        particle[1][1] += 0.01 # circles speed
        if particle[2] <= 0:
            particles.remove(particle)
    for particle in particles:
        pygame.draw.circle(
            window, (color),
        (round(particle[0][0]), round(particle[0][1])),
         round(particle[2]))

p1 = 1
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            p1 += 100
    window.fill(0) 
    particles_run(particles1, 150, (255, 255, 0))
    particles_run(particles2, 50, (255, 0, 255))
    particles_run(particles3, 250, (0, 255, 255))
    pygame.display.flip()

pygame.quit()
exit()




























