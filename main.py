# Quick and dirty clone of the pokemon battle system

import pokemon, sys, pygame, interface
from interface import ProgressBar
from graphics_routines import *
from pygame.locals import *

# Globals #
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

bar = ProgressBar(100, 75, True)

# Setting the background colour #
BGCOLOR = interface.WHITE

def main():
	init_graphics()
	while True:
		runGame()

def runGame():
	game_init()
	while True:
		#game_over = game_update()
		game_update()
		bar.update()
		game_render()
		#if game_over == True:
		#	return

def game_init():
	return

def game_update():
	bulbasaurMoves = ['Tackle', 'Growl', 'Razor Leaf']
	#bulbasaur = pokemon.Pokemon('bulbasaur', 15, pokemon.GRASS, 5, 5, bulbasaurMoves)
	
	# Handling events #
	for event in pygame.event.get():
		if event.type == QUIT:				# Quit by OS #
			terminate()
		elif event.type == KEYDOWN:
			if (event.key == K_ESCAPE):		# Quit by player #
				terminate()
			elif (event.key == K_z):
				bulbasaur.print_info()
	return False

def game_render():
	render_begin()
	
	# mix and match rendering routines from graphics_routines module to render the scene based on current game state.
	# this model is inspired by the immediate gui pattern.
	
	drawTest()
	render_end()

def terminate():
	pygame.quit()
	sys.exit()

# No idea what this does, but it was in the example so I'm throwing it in #
if __name__ == '__main__':
	main()
