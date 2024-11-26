# Write your solution here
n1 = int(input("Please type in a number: "))
for i in range(1,n1+1):
    for j in range(1,n1+1):
        print(f"{i} x {j} = {i*j}")