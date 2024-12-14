# Write your solution here
import random

def lottery_numbers(amount : int, lower : int, upper : int):
    l1 = list(range(lower,upper+1))
    random.shuffle(l1)
    return sorted(l1[:amount])