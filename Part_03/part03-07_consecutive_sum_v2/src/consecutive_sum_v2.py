# Write your solution here
n1 = int(input("Limit: "))
sum1 = 0
count = 0
counts = ""

while(sum1 < n1):
    count += 1
    sum1 += count
    counts += f"{count} + "

print(f"The consecutive sum: {counts[:-3]} = {sum1}")