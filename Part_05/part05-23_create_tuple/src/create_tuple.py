# Write your solution here
def create_tuple(x : int, y : int, z : int):
    smallest = 0
    sum1 = x + y + z
    greatest = 0
    if(x < y and x < z):
        smallest = x
    elif(y > z):
        smallest = z
    else:
        smallest = y

    if(x > y and x > z):
        greatest = x
    elif(y > z):
        greatest = y
    else:
        greatest = z
    return (smallest,greatest,sum1)