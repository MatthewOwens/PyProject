#Base Move class, containing name, type, power, accuracy

DEBUFF = -1
BUFF = 0
NORMAL = 1
FIRE = 2
GRASS = 3
WATER = 4

def typeString(Type):
	if Type == 1: return "NORMAL"
	elif Type == 2: return "FIRE"
	elif Type == 3: return "GRASS"
	elif Type == 4: return "WATER"
	elif Type == 0: return "NORMAL"
	elif Type == -1: return "NORMAL"
	else: return "???"

# Base class for all moves. Using this as a move should deal no damage and give no effects
class baseMove:
    Name = " "
    #Type = NORMAL
    Type = -2
    Power = 0
    accuracy = 0
    bonusAttack = 1
    bonusDefense = 1
    bonusAccuracy = 1
    currentPP = 0
    maxPP = 0

#       DEBUFFS       #

#Growl
class debuffGrowl(baseMove):
    Name = "Growl"
    Type = DEBUFF
    bonusAttack = 0.9
    currentPP = maxPP = 25

#Tail whip
class debuffTailWhip(baseMove):
    Name = "Tail Whip"
    Type = DEBUFF
    bonusDefense = 0.9
    currentPP = maxPP = 25


#       ATTACKS       #

# Scratch
class attackScratch(baseMove):
    Name = "Scratch"
    Type = NORMAL
    Power = 40
    accuracy = 100
    currentPP = maxPP = 25


#Ember
class attackEmber(baseMove):
    Name = "Ember"
    Type = FIRE
    Power = 40
    accuracy = 100
    currentPP = maxPP = 10


#Tackle
class attackTackle(baseMove):
    Name = "Tackle"
    Type = NORMAL
    Power = 50
    accuracy = 100
    currentPP = maxPP = 10

#Razor Leaf
class attackRazorLeaf(baseMove):
    Name = "Razor Leaf"
    Type = GRASS
    Power = 55
    Accuracy = 95
    currentPP = maxPP = 10

#Water Gun
class attackWaterGun(baseMove):
    Name = "Water Gun"
    Type = WATER
    Power = 40
    Accuracy = 100
    currentPP = maxPP = 10



