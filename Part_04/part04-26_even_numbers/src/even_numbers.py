# Write your solution here
def even_numbers(list1 : list) -> list:
    even_list = []
    for i in list1:
        if(i % 2 == 0):
            even_list.append(i)
    return even_list