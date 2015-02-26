from graphics_routines import *
from gamestate import *
from state_manager import *

class ActionSelectionState(GameState):
	currentSelectedRow = 0
	currentSelectedColumn = 0
	
	def __init__(self):
		self.currentSelectedColumn = 0
		self.currentSelectedRow = 0

	def handle_key_down(self, key):
		if (key == K_RIGHT and self.currentSelectedColumn <= 0):
			self.currentSelectedColumn = self.currentSelectedColumn + 1
		if (key == K_LEFT and self.currentSelectedColumn > 0):
			self.currentSelectedColumn = self.currentSelectedColumn - 1
		if (key == K_DOWN and self.currentSelectedRow <= 0):
			self.currentSelectedRow = self.currentSelectedRow + 1
		if (key == K_UP and self.currentSelectedRow > 0):
			self.currentSelectedRow = self.currentSelectedRow - 1
		if (key == K_SPACE):
			if (self.currentSelectedColumn == 0 and self.currentSelectedRow == 0):
				change_state(MoveSelectionState())
			
		return
	
	def update(self):
		return
			
	def render(self):
		drawMessageBox("", "", "") # empty message box
		drawActionBox(self.currentSelectedColumn, self.currentSelectedRow)
		return
		
from move_selection_state import *