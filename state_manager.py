from gamestate import *

__currentGameState = GameState()

def change_state(newState):
	global __currentGameState
	__currentGameState = newState

def get_state():
	return __currentGameState
