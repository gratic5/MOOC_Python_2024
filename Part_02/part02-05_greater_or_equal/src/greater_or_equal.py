# Write your solution here
n1 = int(input("Please type in the first number: "))
n2 = int(input("Please type in another number: "))
if(n1 > n2):
    print(f"The greater number was: {n1}")
elif(n2 > n1):
    print(f"The greater number was: {n2}")
else:
    print(f"The numbers are equal!")