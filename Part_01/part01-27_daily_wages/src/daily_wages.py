# Write your solution here
n1 = float(input("Hourly wage: "))
n2 = int(input("Hours worked: "))
n3 = input("Day of the week: ")

if(n3 == "Sunday"):
    print(f"Daily wages: {n1*n2*2} euros")
else:
    print(f"Daily wages: {n1*n2} euros")