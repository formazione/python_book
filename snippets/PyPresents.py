import pygame
import sys


'''
big_screeb_code
	palette         definition the colors used in the game 24.1.2021


'''

text_for_slides = """Educazione civica
La Costituzione
legge fondamentale dello Stato
Si trova al vertice #del sistema legislativo
Referendum del 2 giugno 1946:# si vota per scegliere: #Monarchia o Repubblica#Vince la Repubblica#
Si vota finalmente#a Suffragio universale # Votano tutti i cittadini maggiorenni#comprese le  donne
Al Sud la maggioranza vota:# monarchia#Al Nord votano:# Repubblica# ............ #Prevale il voto alla Repubblica
Ã¨ composta da 139 articoli
1-12 principi fondamentali
1#L'Italia è una repubblica #democratica fondata sul #lavoro.##La sovranitÃ  appartiene#al popolo che la#esercita nelle forme#e nei limiti della#Costituzione.
""".splitlines()

pygame.init()
class Game:
	def __init__(self, text):
		self.screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()
		self.title_font_size = 64
		self.font_init(text)
		self.slides_counter = 0
		self.mainloop()

	def increase_font(self):
		self.title_font_size += 1

	def mainloop(self):
		"This runs until you quit or escape"
		self.game = 1 # bool that if 1 the game goes on
		while self.game:
			for event in pygame.event.get():
				self.game = self.check_exit(event) # quit or escape
				self.keypressed(event)
			# self.update_screen()
			pygame.display.update()
			self.clock.tick(60)
		self.quit() # exit from the game

	def update_screen(self):
		self.screen.blit(self.title_surface, (30, 50))
		# self.fx_title_grow()

	def quit(self):
		"Exit from the game"
		pygame.quit()
		sys.exit()

	def check_exit(self, event):
		"Check if user presses quit or escape"
		quit = event.type == pygame.QUIT
		exit = event.type == pygame.KEYDOWN  and event.key == pygame.K_ESCAPE
		if quit or exit:
			self.game = 0
		return self.game

	def keypressed(self, event):
		"Makes the slides go on with right, back with left"
		if event.type == pygame.KEYDOWN:

			#                 RIGHT    KEY

			if event.key == pygame.K_RIGHT:
				self.screen.fill((0, 0, 0))
				if self.slides_counter < len(text_for_slides) - 1:
					self.slides_counter += 1
					print("RIGHT")


			#                 LEFT     KEY

			if event.key == pygame.K_LEFT:
				if self.slides_counter > 0:
					self.slides_counter -= 1
				self.screen.fill((0, 0, 0))
			
			if event.key == pygame.K_d:
				self.screen 
				self.screen.fill((0, 0, 0))

			self.font_init(text_for_slides[self.slides_counter])

			#     MOUSE WHEEL  ==>    INCREASE SIZE OF THE LETTERS / DECREASE

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:
				self.title_font_size += 6
			else:
				self.title_font_size -= 6

			self.font_init(text_for_slides[self.slides_counter])

	def font_init(self, text):
		"Show text in different rows if there is a #"
		self.text = text
		self.title_font = pygame.font.SysFont("Arial", self.title_font_size)
		self.win_w, self.win_h = pygame.display.get_surface().get_size()
		self.title_surface = pygame.Surface((self.win_w, self.win_h))
		space = 0
		for row in text.split("#"):
			row = self.title_font.render(row, 0, (255, 255, 255))
			self.title_surface.blit(row, (0, 0 + space))
			space += self.title_font_size


		self.screen.blit(self.title_surface, (30, 50))


	def fx_title_grow(self):
		"FX: the title grows"
		if self.title_font_size < 100:
			if self.title_font_size % 3 == 0:
				self.title_surface = self.title_font.render(self.text, 0, pygame.Color("Coral"))
			else:
				self.title_surface = self.title_font.render(self.text, 0, pygame.Color("Black"))

			self.title_font_size += 5
			self.title_font = pygame.font.SysFont("Arial", self.title_font_size)
			# self.font_init()
		else:
			self.title_surface = self.title_font.render(self.text, 0, pygame.Color("White"))



Game("""Usa le frecce per scorrere il testo#Con il mouse puoi ridimensionare il testo
""")



