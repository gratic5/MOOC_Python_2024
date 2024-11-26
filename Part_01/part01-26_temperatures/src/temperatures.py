# Write your solution here
n1 = int(input("Please type in a temperature (F): "))
if((((n1 -32)*5)/9) < 0):
    print(f"{n1} degrees Fahrenheit equals {(((n1 -32)*5)/9)} degrees Celsius")
    print(f"Brr! It's cold in here!")
else:
    print(f"{n1} degrees Fahrenheit equals {(((n1 -32)*5)/9)} degrees Celsius")