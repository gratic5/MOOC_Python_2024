# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename  :str, lower_limit : int):
    l1 = []
    with open(filename) as f:
        for i in f: 
            i = i.replace("\n","")
            j = i.split(" ")
            j1 = str.maketrans("","",string.punctuation)
            j2 = [j4.translate(j1) for j4 in j]
            for k in j2:
                l1.append(k)
    
    return {i1 : l1.count(i1) for i1 in l1 if l1.count(i1) >= lower_limit}

