# Write your solution here
n1 = int(input("Please type in a year: "))
if(n1 % 4 == 0):
    if(n1 % 100 == 0):
        if(n1 % 400 == 0):
            print(f"That year is a leap year.")
        else:
            print(f"That year is not a leap year.")
    else:
        print(f"That year is a leap year.")
else:
    print(f"That year is not a leap year.")
