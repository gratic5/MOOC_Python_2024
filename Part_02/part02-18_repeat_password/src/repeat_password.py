# Write your solution here
p1 = input("Password: ")
while(True):
    p2 = input("Repeat password: ")
    if(p1 == p2):
        print(f"User account created!")
        break
    elif(p1 != p2):
        print("They do not match!")