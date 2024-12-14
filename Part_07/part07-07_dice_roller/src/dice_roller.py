# Write your solution here
import random, string

def roll(die : str):
    if(die == "A"):
        return int(random.choice("333336"))
    elif(die == "B"):
        return int(random.choice("222555"))
    elif(die == "C"):
        return int(random.choice("144444"))
    
def play(die1 : str, die2 : str, times : int):
    die1_won = 0
    die2_won = 0
    ties = 0

    for i in range(times):
        a = roll(die1)
        b = roll(die2)

        if(a > b):
            die1_won += 1
        elif(a < b):
            die2_won += 1
        else:
            ties += 1
    
    return (die1_won,die2_won,ties)
