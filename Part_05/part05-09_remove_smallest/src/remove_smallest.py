# Write your solution here
def remove_smallest(numbers : list):
    smallest = numbers[0]
    for i in numbers:
        if(smallest > i):
            smallest = i
    numbers.remove(smallest)