from PIL import Image
import pygame
import glob
import os
from random import choice
import tkinter as tk
from tkinter import messagebox
#from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("PyDraw - Press h for help")
clock = pygame.time.Clock()

w = 10
loop = True
press = False
color = "white"
cnt = 0

def delete_images():
    root = tk.Tk()
    root.withdraw()
    x = messagebox.askquestion("Do you want to delete all the images?")
    if x == "yes":
        [os.remove(png) for png in glob.glob("*png")]

BLACK = (0, 0, 0)
blue = (0,0,255)
yellow = (0,255,0)
red = (255,0,0)
color = (255,255,255)
#pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
pygame.mouse.set_cursor((16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1, 128))
#mouse_cursor = pygame.image.load('brush.png')
drawing = False
last_pos = None
while loop:
    # screen.fill(pygame.Color(0, 0, 0))
    try:
        #pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    color = blue
                elif event.key == pygame.K_y:
                    color = yellow
                elif event.key == pygame.K_e:
                    delete_images()
                elif event.key == pygame.K_UP:
                    w += 3
                elif event.key == pygame.K_DOWN:
                    w -= 3
                elif event.key == pygame.K_h:
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Help","""
Use themousewheel to have a bigger or smaller trace\n
Use 'e' to erase all the images you saved\n
Press b, y or r w for colors
\nd to delete the screes
\ns to save screen and g to make a gif
""")
                elif event.key == pygame.K_r:
                    color = red
                elif event.key == pygame.K_r:
                    color = red
                elif event.key == pygame.K_w:
                    color = (255,255,255)
                elif event.key == pygame.K_d:
                    screen.fill(pygame.Color(0, 0, 0))
                elif event.key == pygame.K_s:
                    if cnt < 10:
                        pygame.image.save(screen, f"screenshot0{cnt}.png")
                    else:
                        pygame.image.save(screen, f"screenshot{cnt}.png")
                    cnt += 1
                elif event.key == pygame.K_g:
                        frames = []
                        imgs = glob.glob("*.png")
                        for i in imgs:
                            new_frame = Image.open(i)
                            frames.append(new_frame)

                        # Save into a GIF file that loops forever
                        frames[0].save('animated.gif', format='GIF',
                                       append_images=frames[1:],
                                       save_all=True,
                                       duration=300, loop=0)
                        os.startfile("animated.gif")

    
        # px, py = pygame.mouse.get_pos()
        # first button of the mouse pressed
        if event.type == pygame.MOUSEMOTION:
            if (drawing):
                mouse_position = pygame.mouse.get_pos()
                if last_pos is not None:
                    pygame.draw.line(screen, color, last_pos, mouse_position, w)
                last_pos = mouse_position
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = (0, 0)
            drawing = False
            last_pos = None
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        if event.type == 6:
            if event.button == 4:
                if w < 20:
                    w += 1 
                print(event.type)
            elif event.button == 5:
                if w > 10:
                    w -= 1

        #screen.blit(mouse_cursor, pygame.mouse.get_pos())
        pygame.display.update()

        clock.tick(200)
    except Exception as e:
        print(e)
        pygame.quit()
        
pygame.quit()