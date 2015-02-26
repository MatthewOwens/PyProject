# Quick and dirty clone of the pokemon battle system

import pokemon, sys, pygame
from pygame.locals import *

# Globals #
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
TICKER = 0

# Colours #
#				R    G    B
WHITE		= (255, 255, 255)
BLUE 		= (015, 140, 246)
GREEN		= (022, 170, 012)
YELLOW		= (255, 167, 000)
RED			= (252, 002, 000)
BGCOLOR = WHITE

def main():
	init()
	while True:
		runGame()

def init():
	global FPSCLOCK, DISPLAYSURF, BASICFONT

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('Pokemon')

def runGame():
	game_init()
	while True:
		game_over = game_update()
		game_render()
		if game_over == True:
			return

def game_init():
	global TICKER
	TICKER = 1

def game_update():
	global TICKER
	
	bulbasaurMoves = ['Tackle', 'Growl', 'Razor Leaf']
	bulbasaur = pokemon.Pokemon('bulbasaur', 15, pokemon.GRASS, 5, 5, bulbasaurMoves)
	# Handling events #
	for event in pygame.event.get():
		if event.type == QUIT:				# Quit by OS #
			terminate()
		elif event.type == KEYDOWN:
			if (event.key == K_ESCAPE):		# Quit by player #
				terminate()
			elif (event.key == K_z):
				bulbasaur.print_info()
	
	TICKER = TICKER + 1
	#print(TICKER)

	if TICKER > 29:
		return True
	else:
		return False

def game_render():
	DISPLAYSURF.fill(BGCOLOR)
	pygame.display.update()
	FPSCLOCK.tick(FPS)

def terminate():
	pygame.quit()
	sys.exit()

# No idea what this does, but it was in the example so I'm throwing it in #
if __name__ == '__main__':
	main()
