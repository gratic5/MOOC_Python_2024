# Write your solution here

def prime_numbers():
    number = 2
    while(True):
        flag = True
        for i in range(2,number):
            if(number % i == 0):
                flag = False
        if(flag):
            yield number
        number += 1