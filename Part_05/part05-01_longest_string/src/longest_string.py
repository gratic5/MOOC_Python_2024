# Write your solution here
def longest(strings : list):
    word = strings[0]
    for i in strings:
        if(len(word) < len(i)):
            word = i
    return word