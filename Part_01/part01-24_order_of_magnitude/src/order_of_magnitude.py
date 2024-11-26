# Write your solution here
n1 = int(input("Please type in a number: "))
if(n1 < 1000):
    print("This number is smaller than 1000")
    if(n1 < 100):
        print(f"This number is smaller than 100")
        if(n1 < 10):
            print(f"This number is smaller than 10")
            print(f"Thank you!")
        else:
            print("Thank you!")
    else:
        print(f"Thank you!")
else:
    print(f"Thank you!")
