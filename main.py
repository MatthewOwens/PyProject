# Quick and dirty clone of the pokemon battle system

import sys, pygame
from graphics_routines import *
from pokemon import *
from pygame.locals import *

# Globals #
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
player_turn = True
current_move_index = 0

bulbasaurMoves = ['Tackle', 'Growl', 'Razor Leaf']
bulbasaur = Pokemon('Bulbasaur', 20, GRASS, 5, 5, bulbasaurMoves)

squirtleMoves = ['Scratch', 'Tail Whip', 'Water Gun']
squirtle = Pokemon('Squirtle', 20, WATER, 5, 5, squirtleMoves)

# Setting the background colour #
BGCOLOR = kColourWhite

def main():
	init_graphics()
	while True:
		runGame()

def runGame():
	game_init()
	while True:
		#game_over = game_update()
		game_update()
		game_render()
		#if game_over == True:
		#	return

def game_init():
	return

def game_update():
	global current_move_index

	# Handling events #
	for event in pygame.event.get():
		if event.type == QUIT:				# Quit by OS #
			terminate()
		elif event.type == KEYDOWN:
			if (event.key == K_ESCAPE):		# Quit by player #
				terminate()
			if player_turn == True:
				if event.key == K_UP:
					if current_move_index > 0: current_move_index -= 1
				if event.key == K_DOWN:
					if current_move_index < 3: current_move_index += 1
	return False

def game_render():
	render_begin()
	
	# mix and match rendering routines from graphics_routines module to render the scene based on current game state.
	# this model is inspired by the immediate gui pattern.
	
	drawTest(bulbasaur, squirtle, current_move_index)
	render_end()

def terminate():
	pygame.quit()
	sys.exit()

# No idea what this does, but it was in the example so I'm throwing it in #
if __name__ == '__main__':
	main()
