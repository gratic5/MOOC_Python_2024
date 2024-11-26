# Write your solution here
def sum_of_positives(list1: list):
    sum1 = 0
    for i in list1:
        if(i > 0):
            sum1 += i
    return sum1