# Write your solution here
def all_the_longest(a : list):
    new_list = []
    longest = ""
    for i in a:
        if(len(i) > len(longest)):
            new_list.clear()
            new_list.append(i)
            longest = i
        elif(len(i) == len(longest)):
            new_list.append(i)
    return new_list
