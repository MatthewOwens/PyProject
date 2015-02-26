# Quick and dirty clone of the pokemon battle system

import sys, pygame
from graphics_routines import *
from pokemon import *
from combat_resolution import *
from pygame.locals import *
from states import States
from state_manager import *
from action_selection_state import *

# Globals #
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
move_index = 0
action_index = 0
current_state = States.start
msgbox_text = ""

#bulbasaurMoves = ['Tackle', 'Growl', 'Razor Leaf', 'Tail Whip']
#bulbasaur = Pokemon('Bulbasaur', 20, GRASS, 5, 5, bulbasaurMoves)
bulbasaur = Pokemon('Bulbasaur', 20, GRASS, 5, 5, ['Tackle', 'Growl', 'Razor Leaf', 'Tail Whip'])

#squirtleMoves = ['Scratch', 'Tail Whip', 'Water Gun']
squirtle = Pokemon('Squirtle', 20, WATER, 5, 5, ['Scratch', 'Tail Whip', 'Water Gun', 'Growl'])

#change_state(ActionSelectionState())
for index in range (0,4):
	print(bulbasaur.moves[index].Name)

print("----------")

for index in range(0,4):
	print(squirtle.moves[index].Name)

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
	global move_index
	global current_state

	currentGameState = get_state()
	

	# Handling events #
	for event in pygame.event.get():
		if event.type == QUIT:				# Quit by OS #
			terminate()
		elif event.type == KEYDOWN:
			if (event.key == K_ESCAPE):		# Quit by player #
				terminate()
			if current_state == States.start:		# Moving to the next state if anything is pressed #
				current_state = States.move_select
			elif current_state == States.move_select:
				if event.key == K_UP:
					if move_index > 0: move_index -= 1
				if event.key == K_DOWN:
					if move_index < 3: move_index += 1
				if event.key == K_z:
					playerAttack()
			else:
				currentGameState.handle_key_down(event.key)
				
	return False

def playerAttack():
	global current_state
	global msgbox_text
	global bulbasaur
	global squirtle

	if bulbasaur.moves[move_index].Type < 1:
		msgbox_text = applyDebuff(bulbasaur.moves[move_index], squirtle)
	else:
		damage = calculateDamage(bulbasaur.moves[move_index], bulbasaur, squirtle)
		if damage == 0:
			msgbox_text = bulbasaur.moves[move_index].Name + " missed!"
		else:
			msgbox_text = bulbasaur.moves[move_index].Name + " hit for " + str(damage) + " damage!"
	current_state = States.player_move

def game_render():
	render_begin()
	currentGameState = get_state()
	
	# mix and match rendering routines from graphics_routines module to render the scene based on current game state.
	# this model is inspired by the immediate gui pattern.

	if current_state != States.start:
		# Drawing the interface items that will be there regardless of state #
		drawPokemonSprites()
		drawPokeStats((200, 85), bulbasaur.name, 5, bulbasaur.health, bulbasaur.max_health, bulbasaur.exp, 100)
		drawPokeStats((30, 5), squirtle.name, 5, squirtle.health, squirtle.max_health, squirtle.exp, 100)
	else: drawText("Press any key to begin!", (kScreenWidth / 2 - 85, kScreenHeight / 2))

	if current_state == States.move_select:
		drawMoveMenu(move_index, bulbasaur.moves)
	elif current_state == States.player_move:
		drawMessageBox(msgbox_text, "", "")
	
#	currentGameState.render()
	
	render_end()

def terminate():
	pygame.quit()
	sys.exit()

# No idea what this does, but it was in the example so I'm throwing it in #
if __name__ == '__main__':
	main()
