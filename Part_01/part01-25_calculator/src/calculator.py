# Write your solution here
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = input("Operation: ")

if(n3 == "multiply"):
    print(f"{n1} * {n2} = {n1*n2}")
elif(n3 == "subtract"): 
    print(f"{n1} - {n2} = {n1-n2}")
elif(n3 == "add"):
    print(f"{n1} + {n2} = {n1+n2}")
