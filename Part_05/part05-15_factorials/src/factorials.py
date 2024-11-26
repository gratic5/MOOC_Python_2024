# Write your solution here
def factorials(n : int):
    d1 = {}
    f = 1
    for i in range(1,n+1):
        f *= i
        d1[i] = f
    return d1
       