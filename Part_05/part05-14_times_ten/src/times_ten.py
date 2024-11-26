# Write your solution here
def times_ten(start_index : int, end_index : int):
    d1 = {}
    for i in range(start_index,end_index+1):
        d1[i] = i*10
    return d1