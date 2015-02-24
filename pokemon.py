# Pokemon class containing ATK, DEF, ACC stats; the name and type of the pokemon
import move

# Possible types #
NORMAL = 1
FIRE = 2
GRASS = 3
WATER = 4

class Pokemon:
	name = "NULL"
	elemType = 1	# Defaulting to normal type #
	attack = 0
	defence = 0
	accMod = 0		# Modifier for the accuracy	#
	moves = []		# Array for the moves #
	
	def __init__(name_, elemType_, attack_, defence_, accMod_, moveNames_):
		name = name_
		elemType = elemType_
		attack = attack_
		defence = defence_
		accMod = accMod_

		[(i, j) for i, j in enumerate(moveNames_)]
		if j == "Growl": moves[i] = debuffGrowl()
		elif j == "Tail Whip": moves[i] = debuffTailWhip()
		elif j == "Scratch": moves[i] = attackScratch()
		elif j == "Ember": moves[i] = attackEmber()
		elif j == "Tackle": moves[i] = attackScratch()
		elif j == "Razor Leaf": moves[i] = attackRazorLeaf()
		elif j == "Water Gun": moves[i] = attackWaterGun()
		#else print("Something went wrong, move name not recognised!")
