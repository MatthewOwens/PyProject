# Quick and dirty clone of the pokemon battle system

import sys, pygame
from graphics_routines import *
from pokemon import *
from pygame.locals import *
from state_manager import *
from action_selection_state import *

# Globals #
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
player_turn = True
msgbox_needs_refresh = True
current_move_index = 0

bulbasaurMoves = ['Tackle', 'Growl', 'Razor Leaf']
bulbasaur = Pokemon('Bulbasaur', 20, GRASS, 5, 5, bulbasaurMoves)

squirtleMoves = ['Scratch', 'Tail Whip', 'Water Gun']
squirtle = Pokemon('Squirtle', 20, WATER, 5, 5, squirtleMoves)

change_state(ActionSelectionState())

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

	currentGameState = get_state()
	

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
			else:
				currentGameState.handle_key_down(event.key)
				
	return False

def game_render():
	render_begin()
	
	currentGameState = get_state()
	
	# mix and match rendering routines from graphics_routines module to render the scene based on current game state.
	# this model is inspired by the immediate gui pattern.
	drawPokemonSprites()
	if player_turn == True:
		drawMoveMenu(current_move_index, bulbasaur.moves)
	drawPokeStats((200, 85), bulbasaur.name, 5, bulbasaur.health, bulbasaur.max_health, bulbasaur.exp, 100)
	drawPokeStats((30, 5), squirtle.name, 5, squirtle.health, squirtle.max_health, squirtle.exp, 100)
#	currentGameState.render()
	
	render_end()

def terminate():
	pygame.quit()
	sys.exit()

# No idea what this does, but it was in the example so I'm throwing it in #
if __name__ == '__main__':
	main()
