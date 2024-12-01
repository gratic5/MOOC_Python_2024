# Write your solution here

def add_to_dictionary():
     with open("dictionary.txt","a") as d:
         s2 = input("The word in Finnish: ")
         s3 = input("The word in English: ")
         d.write(f"{s2} - {s3}\n")

def search_dictionary(string1 : str):
    d1 = {}
    l1 = []
    with open("dictionary.txt") as l:
        for i in l:
            x = i.split("-")
            y = [j.strip() for j in x]
            d1[y[0]] = y[1]
    l2 = []
    for p,q in d1.items():
        if(string1 in q or (string1 in p)):
            l2.append(f"{p} - {q}")
    return l2


def dictionary1():
    while(True):
        print("1 - Add word, 2 - Search, 3 - Quit")
        s1 = input("Function: ")
        if(s1 == "1"):
            add_to_dictionary()
            print("Dictionary entry added")
        elif(s1 == "2"):
            s4 = input("Search term: ")
            s5 = search_dictionary(s4)
            for i in s5:
                print(i)
        elif(s1 == "3"):
            print("Bye")
            break

dictionary1()