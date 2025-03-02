# Write your solution here
def even_numbers(beginning : int, maximum : int):
    number = beginning
    while(number <= maximum):
        yield number
        number += 2