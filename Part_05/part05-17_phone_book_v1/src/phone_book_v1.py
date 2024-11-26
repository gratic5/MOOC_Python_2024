# Write your solution here

def search(d4):
    s1 = input("name: ")
    if(s1 in d4):
        print(d4[s1])
    else:
        print("no number")

def add(d3):
    s1 = input("name: ")
    s2 = input("number: ")
    d3[s1] = s2
    print("ok!")

def person_input(d2):
    while(True):
        n1 = int(input("command (1 search, 2 add, 3 quit): "))
        if(n1 == 3):
            print("quitting...")
            break
        elif(n1 == 2):
            add(d2)
        elif(n1 == 1):
            search(d2)

def start():
    d1 = {}
    person_input(d1)

start()