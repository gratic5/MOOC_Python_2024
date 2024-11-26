# Write your solution here
def length_of_longest(a : list):
    length1 = len(a[0])
    for i in a:
        if(len(i) > length1):
            length1 = len(i)
    return length1