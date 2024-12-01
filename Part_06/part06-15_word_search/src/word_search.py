# Write your solution here
def get_wordList():
    l1 = []
    with open("words.txt") as a:
        for i in a:
            x = i.strip()
            l1.append(x)
    return l1

def find_words(search_term : str):
    l2 = get_wordList()
    l3 = []
    if("." in search_term):
        for i,j in enumerate(l2):
            if(len(j) != len(search_term)):
                continue
            flag = True
            for k in range(len(j)):
                if(search_term[k] != "." and j[k] != search_term[k]):
                    flag = False
            if(flag):
                l3.append(j)
    elif("*" not in search_term and "." not in search_term):
        for i,j in enumerate(l2):
            if(search_term == j):
                l3.append(j)
    elif("*" in search_term):
        if(search_term.startswith("*")):
            for i,j in enumerate(l2):
                if(j.endswith(search_term[1:])):
                    l3.append(j)
        elif(search_term.endswith("*")):
            for i,j in enumerate(l2):
                if(j.startswith(search_term[:-1])):
                    l3.append(j)
    return l3
              




        
