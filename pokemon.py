# Pokemon class containing ATK, DEF, ACC stats; the name and type of the pokemon
import move
from move import *

# Possible types #
NORMAL = 1
FIRE = 2
GRASS = 3
WATER = 4

class Pokemon:
	name = 'NULL'
	health = 0
	elemType = 1		# Defaulting to normal type #
	attack = 0
	defence = 0
	accMod = 1			# Base accuracy modifier. >1 is increased accuracy while <1 is decreased #
	moves = []			# Array for the moves #
	timesDebuffed = 0	# Used to limit the amount of stat reductions #
	
	def __init__(self, name_, health_, elemType_, attack_, defence_, moveNames_):
		self.health = health_	# No idea why python was complaining about indentation here #
		self.name = name_
		self.elemType = elemType_
		self.attack = attack_
		self.defence = defence_

		[(i, j) for i, j in enumerate(moveNames_)]
		print(i, j)
		if j == 'Growl': self.moves[i] = debuffGrowl()
		elif j == 'Tail Whip': self.moves[i] = debuffTailWhip()
		elif j == 'Scratch': self.moves[i] = attackScratch()
		elif j == 'Ember': self.moves[i] = attackEmber()
		elif j == 'Tackle': self.moves[i] = attackTackle()
		elif j == 'Razor Leaf': self.moves[i] = attackRazorLeaf()
		elif j == 'Water Gun': self.moves[i] = attackWaterGun()
		else: print('Something went wrong, move name not recognised!')

	def print_info(self):
		print(self.name)
		print(self.attack)
		print(self.defence)
		print(self.accMod)
