# Write your solution here

while(True):
    n1 = int(input("Please type in a number: "))
    fact = 1
    if(n1 <= 0):
        print(f"Thanks and bye!")
        break
    else:
        for i in range(1,n1+1):
            fact *= i
    print(f"The factorial of the number {n1} is {fact}")
