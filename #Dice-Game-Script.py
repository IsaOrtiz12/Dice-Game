#Dice Game Script
#Possible bonus features include "Demon Dice" wherein you roll three six’s and you roll demon die, whatever number
# you roll will subtract from your score and that will be your score. 


import random
def roll_dice(num_dice) :
    """
    Roll a specified number of dice and return a list of reults
    """
    return [random.randint(1,6) for _ in range(num_dice)]
def rank(score):
    """
    Determine the player's rank based on their final score.
    """
    if score <= 7:
        return "Noob Rank"
    elif 8 <= score <=14:
        return "Nonchalant Rank"
    elif 15 <= score <= 17:
        return "Expert Rank"
    else:
        return "LEGEND RANK"

def play_turn():
    """
    This is the players turn where they roll die
    """
    dice = roll_dice(3)
    print(f"initial roll: {dice}")

    while True:
        #tuple out?
        if len(set(dice)) == 1:
            if dice[0] ==6: #DEMON DIE 
                print("You rolled three sixes! DEMON DIE MODE")
                demon_die = random.randint(1,6)
                print(f"DEMON DIE rolled: {demon_die}")
                return 18 - demon_die
            print(f"Tuple out! You rolled three {dice[0]}'s! No points for this round")
            return 0
        elif dice.count (1) == 3: #bonus die
            print("you rolled three ones! BONUS DIE MODE")
            bonus_die = random.randint(1,6)
            print(f"Bonus die rolled: {bonus_die}")
            return 3 * bonus_die
        
        fixed_dice = [d for d in dice if dice.count(d) > 1]
        if fixed_dice:
            print(f"fixed dice: {fixed_dice}")

        free_dice = len(dice) - len(fixed_dice)
        if free_dice > 0: 
            reroll = input("do you want to re-rolla free dice? (yes/no) TYPE CAREFULLY OR PROGRAM WILL IMPLODE").lower()       
