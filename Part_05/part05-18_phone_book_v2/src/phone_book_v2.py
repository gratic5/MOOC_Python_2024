# Write your solution here
def search(d1):
    n1 = input("name: ")
    if(n1 not in d1):
        print("no number")
    elif(n1 in d1):
        for i in d1[n1]:
            print(i)

def add(d1):
    n1 = input("name: ")
    n2 = input("number: ")
    l1 = []
    if(n1 not in d1):
        d1[n1] = []
        d1[n1].append(n2)
    elif(n1 in d1):
        d1[n1].append(n2)
    print("ok!")

def person_input():
    phoneBook = {}
    while(True):
        n1 = int(input("command (1 search, 2 add, 3 quit): "))
        if(n1 == 1):
            search(phoneBook)
        elif(n1 == 2):
            add(phoneBook)
        elif(n1 == 3):
            print("quitting...")
            break

person_input()