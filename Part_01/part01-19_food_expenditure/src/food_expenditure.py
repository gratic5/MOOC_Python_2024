# Write your solution here
n1 = int(input("How many times a week do you eat at the student cafeteria? "))
n2 = float(input("The price of a typical student lunch? "))
n3 = float(input("How much money do you spend on groceries in a week? "))
print("")
print(f"Average food expenditure:")
print(f"Daily: {((n1*n2)+n3)/7} euros")
print(f"Weekly: {(n1*n2)+n3} euros")