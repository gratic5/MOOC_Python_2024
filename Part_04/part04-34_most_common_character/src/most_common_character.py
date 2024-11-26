# Write your solution here
def most_common_character(a : str) -> str:
    count = 0
    word = ""
    for i in a:
        if(a.count(i) > count):
            count = a.count(i)
            word = i
    return word