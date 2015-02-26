# Quick and dirty clone of the pokemon battle system

import pokemon, sys, pygame, interface
from interface import ProgressBar
from graphics_routines import *
from pygame.locals import *
from state_manager import *
from action_selection_state import *

# Globals #
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

bar = ProgressBar(100, 75, True)
change_state(ActionSelectionState())

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
	
	currentGameState = get_state()
	
	# Handling events #
	for event in pygame.event.get():
		if event.type == QUIT:				# Quit by OS #
			terminate()
		elif event.type == KEYDOWN:
			if (event.key == K_ESCAPE):		# Quit by player #
				terminate()
			else:
				currentGameState.handle_key_down(event.key)
				
	return False
	
def game_render():
	render_begin()
	
	currentGameState = get_state()
	
	# mix and match rendering routines from graphics_routines module to render the scene based on current game state.
	# this model is inspired by the immediate gui pattern.
	drawPokemonSprites()
	drawPokeStats((200, 85), "Squirtle", 5, 20, 20, 0, 100)
	drawPokeStats((30, 5), "Bulbasaur", 5, 20, 20, 10, 100)
	currentGameState.render()
	
	render_end()

def terminate():
	pygame.quit()
	sys.exit()

# No idea what this does, but it was in the example so I'm throwing it in #
if __name__ == '__main__':
	main()
