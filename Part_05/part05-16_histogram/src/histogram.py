# Write your solution here
def histogram(a : str):
    d1 = {}
    for i in a:
        if(i not in d1):
            d1[i] = 0
        d1[i] += 1
    for i,j in d1.items():
        print(f"{i} {j*'*'}")