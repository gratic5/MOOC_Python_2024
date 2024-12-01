# Write your solution here
s1 = input("Whom should I sign this to: ")
s2 = input("Where shall I save it: ")

with open(s2,"w") as n:
    n.write(f"Hi {s1}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")