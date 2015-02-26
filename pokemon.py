# Pokemon class containing ATK, DEF, ACC stats; the name and type of the pokemon

import move
from move import *

# Possible types #
NORMAL = 1
FIRE = 2
GRASS = 3
WATER = 4

class Pokemon(object):
        name = 'NULL'
        health = 0
        elemType = 1		# Defaulting to normal type #
        attack = 0
        defence = 0
        accMod = 1			# Base accuracy modifier. >1 is increased accuracy while <1 is decreased #
        moves = [baseMove, baseMove, baseMove, baseMove]			# Array for the moves #
        timesDebuffed = 0	# Used to limit the amount of stat reductions #
        max_health = 0
        exp = 0
        
        def __init__(self, name_, health_, elemType_, attack_, defence_, moveNames_):
            self.health = health_	# No idea why python was complaining about indentation here #
            self.name = name_
            self.elemType = elemType_
            self.attack = attack_
            self.defence = defence_
            self.max_health = health_

            for index, move in enumerate(moveNames_):
                #print move
                if move == 'Growl': self.moves[index] = debuffGrowl()
                elif move == 'Tail Whip': self.moves[index] = debuffTailWhip()
                elif move == 'Scratch': self.moves[index] = attackScratch()
                elif move == 'Ember': self.moves[index] = attackEmber()
                elif move == 'Tackle': self.moves[index] = attackTackle()
                elif move == 'Razor Leaf': self.moves[index] = attackRazorLeaf()
                elif move == 'Water Gun': self.moves[index] = attackWaterGun()
                else: print('Something went wrong, move name not recognised!')

        def move_list(self):
			move_names = ["","","",""]
			for index, move in enumerate(self.moves):
				move_names[index] = move.Name
			return move_names

        def move_types(self):
			move_types = ["","","",""]
			for index in range(0,4):
				move_types[index] = typeString(self.moves[index].Type)
			return move_types

        def print_info(self):
            print(self.name)
            print(self.attack)
            print(self.defence)
            print(self.accMod)

