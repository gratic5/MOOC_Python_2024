# Write your solution here
import random,string

def words(n : int, beginning : str):
    
    list1 = []
    with open("words.txt") as w:  
        for i in w:
            i = i.strip()
            if(i.startswith(beginning)):
                list1.append(i)
    
    if(len(list1) < n):
        raise ValueError
    
    random.shuffle(list1)
    return list1[:n]
