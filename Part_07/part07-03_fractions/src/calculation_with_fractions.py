# Write your solution here
import fractions

def fractionate(amount : int):
    l1 = []
    for i in range(amount):
        l1.append(fractions.Fraction(1,amount))
    return l1
