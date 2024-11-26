# Write your solution here
def shortest(a : list):
    length1 = len(a[0])
    name = a[0]
    for i in a:
        if(len(i) < length1):
            length1 = len(i)
            name = i
    return name