# Pokemon class containing ATK, DEF, ACC stats; the name and type of the pokemon
import move

# Possible types #
NORMAL = 1
FIRE = 2
GRASS = 3
WATER = 4

class Pokemon:
	name = "NULL"
    health = 0
	elemType = 1	# Defaulting to normal type #
	attack = 0
	defence = 0
	accMod = 1		# Modifier for the accuracy	, Base accuracy multiplier accmod >1 is increase and < 1 is a decrease#
	moves = []		# Array for the moves #
    timesDebuffed = 0   #used to limit amount of times pokemon can have stats reduced
	
	def __init__(name_, health_, elemType_, attack_, defence_, accMod_, moveNames_):
		health = health_
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
