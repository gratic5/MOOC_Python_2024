# Write your solution here
n1 = int(input("Please type in a number: "))
i = 1
if( n1 % 2 == 0):
    while(i <= n1):
        if(i % 2 == 0):
            print(i - 1)
        else:
            print(i+1)
        i +=1
else:
    while(i <= n1 -1):
        if(i % 2 == 0):
            print(i - 1)
        else:
            print(i+1)
        i +=1
    print(n1)
