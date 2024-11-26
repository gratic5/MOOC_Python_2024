# Write your solution here
gp = int(input("How many points [0-100]: "))

if(gp > 100):
    print(f"Grade: impossible!")
elif(gp >= 90):
    print(f"Grade: 5")
elif(gp >= 80):
    print(f"Grade: 4")
elif(gp >= 70):
    print(f"Grade: 3")
elif(gp >= 60):
    print(f"Grade: 2")
elif(gp >= 50):
    print(f"Grade: 1")
elif(gp >= 0):
    print(f"Grade: fail")
elif(gp < 0):
    print(f"Grade: impossible!")
