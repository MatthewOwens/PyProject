# Quick and dirty clone of the pokemon battle system

import sys, pygame, random
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
bulbasaur = Pokemon('Bulbasaur', 20, GRASS, 5, 5, ['Tackle', 'Growl', 'Razor Leaf', 'Tail Whip'])

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
		game_update()
		game_render()

def game_init():
	return

def game_update():
	global move_index, current_state

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
			elif current_state == States.player_move:
				if event.key == K_z:
					current_state = States.enemy_move
			elif current_state == States.enemy_move:
				if event.key == K_z:
					enemyAttack()
			else:							# Win or Lose state #
				if event.key == K_z:
					reset()
	return False

def playerAttack():
	global current_state, msgbox_text, bulbasaur, squirtle

	if bulbasaur.moves[move_index].Type < 1:
		msgbox_text = applyDebuff(bulbasaur.moves[move_index], squirtle)
	else:
		damage = calculateDamage(bulbasaur.moves[move_index], bulbasaur, squirtle)
		squirtle.health -= damage
		if damage == 0:
			msgbox_text = bulbasaur.moves[move_index].Name + " missed!"
		else:
			msgbox_text = bulbasaur.moves[move_index].Name + " hit for " + str(damage) + " damage!"

	if squirtle.health <= 0:
		squirtle.health = 0
		current_state = States.win
	else: current_state = States.player_move

def enemyAttack():
	global current_state, msgbox_text, bulbasaur, squirtle

	index = random.randint(0,3)
	if squirtle.moves[index].Type < 1:
		msgbox_text = applyDebuff(squirtle.moves[index], bulbasaur)
	else:
		damage = calculateDamage(squirtle.moves[index], squirtle, bulbasaur)
		bulbasaur.health -= damage
		if damage == 0:
			msgbox_text = squirtle.moves[index].Name + " missed!"
		else:
			msgbox_text = squirtle.moves[index].Name + " hit for " + str(damage) + " damage!"

	if bulbasaur.health <= 0:
		bulbasaur.health = 0
		current_state = States.lose
	else:
		current_state = States.move_select

def reset():
	global current_state, bulbasaur, squirtle
	#bulbasaur = Pokemon('Bulbasaur', 20, GRASS, 5, 5, ['Tackle', 'Growl', 'Razor Leaf', 'Tail Whip'])
	squirtle = Pokemon('Squirtle', 20, WATER, 5, 5, ['Scratch', 'Tail Whip', 'Water Gun', 'Growl'])
	bulbasaur = Pokemon('Bulbasaur', 20, GRASS, 5, 5, ['Tackle', 'Growl', 'Razor Leaf', 'Tail Whip'])
	current_state = States.move_select

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
	elif current_state == States.player_move or current_state == States.enemy_move:
		drawMessageBox(msgbox_text, "", "")
	elif current_state == States.win:
		render_begin()		# Clearing the screen #
		drawText("You win! Press Z to reset or ESC to quit.", (10, kScreenHeight / 2))
	elif current_state == States.lose:
		render_begin()		# Clearing the screen #
		drawText("You lose! Press Z to reset or ESC to quit.", (8, kScreenHeight / 2))
	
	render_end()

def terminate():
	pygame.quit()
	sys.exit()

# No idea what this does, but it was in the example so I'm throwing it in #
if __name__ == '__main__':
	main()
