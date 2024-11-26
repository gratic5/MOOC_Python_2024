from math import sqrt
# Write your solution here

while(True):
    n1 = int(input("Please type in a number: "))
    if(n1 > 0):
        print(f"{sqrt(n1)}")
    elif(n1 < 0):
        print(f"Invalid number")
    elif(n1 == 0):
        print(f"Exiting...")
        break