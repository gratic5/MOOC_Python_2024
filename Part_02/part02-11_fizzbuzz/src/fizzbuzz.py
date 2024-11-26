# Write your solution here
n1 = int(input("Number: "))

if(n1 % 5 == 0 and n1 % 3 == 0):
    print("FizzBuzz")
elif(n1 % 5 == 0):
    print("Buzz")
elif(n1 % 3 == 0):
    print("Fizz")
    
