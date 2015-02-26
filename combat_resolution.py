#damage and combat resolution

import random, math, move, pokemon

#class resolveAttack:
def calculateDamage( attackMove, attackingPokemon, defendingPokemon):
    attackAccuracy = attackMove.accuracy * attackingPokemon.accMod #total accuracy of attack > 1 is a guaranteed hit 
        
    if attackMove.Type == move.NORMAL: #No bonus
        attkMod = 1
    elif attackMove.Type == move.FIRE & defendingPokemon.elemType == move.GRASS: #positive type mods
        attkMod = 1.5
    elif attackMove.Type == move.GRASS & defendingPokemon.elemType == move.WATER:
        attkMod = 1.5
    elif attackMove.Type == move.WATER & defendingPokemon.elemType == move.FIRE:
        attkMod = 1.5
    elif attackMove.Type == move.FIRE & defendingPokemon.elemType == move.WATER: #negative type mods
        attkMod = 0.5
    elif attackMove.Type == move.WATER & defendingPokemon.elemType == move.GRASS:
        attkMod = 0.5
    elif attackMove.Type == move.GRASS & defendingPokemon.elemType == move.FIRE:
        attkMod = 0.5
            
    #determining crits
    if random.random() <= 0.2:
        critMod = 1.5
    else:
        critMod = 1
       
    if attackAccuracy >= random.random():
        Mod = random.uniform( 0.85, 1 ) * attkMod * critMod #Random variance, type mod and crit
        return math.floor( ( ( 1 / 25 ) * ( attackingPokemon.attack / defendingPokemon.defence ) * attackMove.Power ) * Mod ) #Based on the damage formula from the game 
    else:
        return 0 #miss
    
def applyDebuff( debuffMove, defendingPokemon):
        
    if defendingPokemon.timesDebuffed < 6:
        defendingPokemon.timesDebuffed = defendingPokemon.timesDebuffed + 1
        defendingPokemon.attack * debuffMove.bonusAttack
        defendingPokemon.defence * debuffMove.bonusDefense
        defendingPokemon.accMod * debuffMove.bonusAccuracy
       
        return defendingPokemon.name + " was debuffed!"
    else:
        return defendingPokemon.name + " can't be debuffed!"
    
    
