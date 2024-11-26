# Write your solution here

n1 = int(input("Value of gift: "))
if(n1 >= 1000_000):
    print(f"Amount of tax: {142100+((n1-1000000)*0.17)} euros")
elif(n1 >= 200000):
    print(f"Amount of tax: {22100+((n1-200000)*0.15)} euros")
elif(n1 >= 55000):
    print(f"Amount of tax: {4700+((n1-55000)*0.12)} euros")
elif(n1 >= 25000):
    print(f"Amount of tax: {1700+((n1-25000)*0.10)} euros")
elif(n1 >= 5000):
    print(f"Amount of tax: {100+((n1-5000)*0.08)} euros")
else:
    print(f"No tax!")
