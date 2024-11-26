# Write your solution here
def distinct_numbers(a : list) -> list:
    new_list = []
    for i in a:
        if(i not in new_list):
            new_list.append(i)
    return sorted(new_list)