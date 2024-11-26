# Write your solution here
def no_shouting(a : list):
    b = []
    for i in a:
        if(not i.isupper()):
            b.append(i)
    return b