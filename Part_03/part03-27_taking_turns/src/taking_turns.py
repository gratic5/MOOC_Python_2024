# Write your solution here

n1 = int(input("Please type in a number: "))
i = 1
if(n1 % 2 == 0):
    while(i <= (n1//2)):
        print(i)
        print(n1 - i + 1)
        i += 1
else:
    while(i <= (n1//2)):
        print(i)
        print(n1 - i + 1)
        i += 1
    print((n1//2)+1)
    
    