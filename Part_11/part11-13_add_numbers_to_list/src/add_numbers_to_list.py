# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers : list):
    n1 = numbers[-1]+1

    if(len(numbers) % 5 == 0):
        return numbers
    numbers.append(n1)
    add_numbers_to_list(numbers)
