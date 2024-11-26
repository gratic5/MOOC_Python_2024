# Write your solution here
def everything_reversed(a : list) -> list:
    new_list = []
    for i in range(len(a)-1,-1,-1):
        new_list.append(a[i][::-1])
    return new_list
