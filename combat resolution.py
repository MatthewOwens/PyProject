#damage and combat resolution

import random, math, move, pokemon

class resolveAttack:
    def calculateDamage( attackMove, attackingPokemon, defendingPokemon)
        attackAccuracy = attackMove.Accuracy * attackingPokemon.accMod #total accuracy of attack > 1 is a guaranteed hit 
        
        if attackMove.Type == NORMAL #No bonus
            attkMod = 1
        elif attackMove.Type == FIRE && defendingPokemon.elemType == GRASS #positive type mod
            attkMod = 1.5
        elif attackMove.Type == GRASS && defendingPokemon.elemType == WATER
            attkMod = 1.5
        elif attackMove.Type == WATER && defendingPokemon.elemType == FIRE
            attkMod = 1.5
        elif attackMove.Type == FIRE && defendingPokemon.elemType == WATER #negative type mod
            attkMod = 0.5
        elif attackMove.Type == WATER && defendingPokemon.elemType == GRASS
            attkMod = 0.5
        elif attackMove.Type == GRASS && defendingPokemon.elemType == FIRE
            attkMod = 0.5
            
        #determining crits
        if math.random() <= 0.2
            critMod = 1.5
        else 
            critMod = 1
        
        if attackAccuracy >= random.random()
            Mod = random.uniform( 0.85, 1 ) * attkMod * critMod #Random variance
            return math.floor( ( ( 1 / 25 ) * ( attackingPokemon.attack / defendingPokemon.defence ) * attackMove.Power ) * Mod ) #Based on the damage formula from the game 
        else
            return 0 #miss
    
    def applyDebuff( debuffMove, defendingPokemon)
        
        if defendingPokemon.timesDebuffed < 6
            defendingPokemon.timesDebuffed = defendingPokemon.timesDebuffed + 1
            defendingPokemon.attack * attackMove.bonusAttack
            defendingPokemon.defense * attackMove.bonusDefense
            defendingPokemon.accMod * attackMove.bonusAccuracy
           
            return "This Pokemon has had its attributes reduced"
        else
            return "This Pokemon's attributes can't be reduced any further"
    
    