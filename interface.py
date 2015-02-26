import pygame
from pygame import draw

# Defining colours for the UI RGB #
WHITE		= (255, 255, 255)
BLUE		= (015, 140, 246)
GREEN		= (022, 170, 012)
YELLOW		= (255, 167, 000)
RED			= (252, 002, 000)
WHITE		= (255, 255, 255)
BLACK		= (000, 000, 000)

class ProgressBar:
	max_value = 0
	current_value = 0	
	is_health_bar = False
	colour = WHITE
	
	def __init__(self, max_value_, current_value_, is_health_bar_):
		self.max_value = max_value_
		self.current_value = current_value_
		self.is_health_bar = is_health_bar_

	def update(self):
		if self.is_health_bar == True:
			if self.current_value > self.max_value / 2:
				self.colour = GREEN
			elif self.current_value > self.max_value / 4:
				self.colour = YELLOW
			else: self.colour = RED
		else: self.colour = BLUE

	def draw(self, SURFACE, start_x, start_y, length):
		end_x = (float(self.current_value) / float(self.max_value)) * 100 + start_x
		pygame.draw.line(SURFACE, self.colour, (start_x, start_y), (end_x, start_y), 10)
		print("startX: ", start_x)
		print("endX:   ", end_x)

class Button:
	text = ""
	rect = pygame.Rect(0,0,0,0)
	
	def __init__(self, text, x, y, width, height):
		self.text = text
		self.rect.left = x
		self.rect.top = y
		self.rect.width = width
		self.rect.height = height

	def update(self, mouseX, mouseY):	# Update method, called on mouseclick #
		if mouseX > self.rect.left & mouseX < self.rect.left + self.rect.width & mouseY > self.rect.top & mouseY < self.rect.top + self.rect.width:
			return True
		else: return False

	def draw(self, SURFACE, FONT):
		pygame.draw.rect(SURFACE, BLACK, self.rect, 5)
		textSurf =  FONT.render(self.text, True, BLACK)
		SURFACE.blit(textSurf, self.rect)
