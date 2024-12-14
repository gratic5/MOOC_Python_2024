# Write your solution here
import datetime

d1 = int(input("Day: "))
m1 = int(input("Month: "))
y1 = int(input("Year: "))

difference = datetime.datetime(y1,m1,d1) - datetime.datetime(1999,12,31)
if(difference.days < 0):
    print(f"You were {abs(difference.days)} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")