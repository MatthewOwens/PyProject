#damage and combat resolution

import random, math

class resolveAttack:
    def calculateDamage( attackMove, attackingPokemon, defendingPokemon)
        attackAccuracy = attackMove.Accuracy * attackingPokemon.Accuracy
        
        if attackAccuracy >= random.random()
            Mod = random.uniform( 0.85, 1 ) #Random variance, Will need to expand for types and crits 
            return math.floor( ( ( 1 / 25 ) * ( attackingPokemon.attack / defendingPokemon.defence ) * attackMove.Power ) * Mod ) #Based on the damage formula from the game 
        else
            return 0 #miss
    
    def applyDebuff( debuffMove, defendingPokemon)
        defendingPokemon.Attack * attackMove.bonusAttack
        defendingPokemon.Defense * attackMove.bonusDefense
        defendingPokemon.Accuracy * attackMove.bonusAccuracy
    
    