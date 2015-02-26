from graphics_routines import *
from gamestate import *
from state_manager import *

class MoveSelectionState(GameState):
	currentSelectedMove = 0
	
	def __init__(self):
		self.currentSelectedMove = 0

	def handle_key_down(self, key):
		if (key == K_DOWN and self.currentSelectedMove <= 2):
			self.currentSelectedMove = self.currentSelectedMove + 1
		if (key == K_UP and self.currentSelectedMove > 0):
			self.currentSelectedMove = self.currentSelectedMove - 1
		if (key == K_RETURN):
			change_state(ActionSelectionState())
		#if (key == K_SPACE):
			#change_state(ExecuteMoveState())
		return
	
	def update(self):
		return
			
	def render(self):
		drawMessageBox("", "", "") # empty message box
		drawMoveMenu(self.currentSelectedMove, []) # add moves info
		return
		
from action_selection_state import *