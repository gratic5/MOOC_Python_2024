# Write your solution here
n1 = int(input("How many students on the course? "))
n2 = int(input("Desired group size? "))

if(n1 % n2 == 0):
    print(f"Number of groups formed: {n1/n2}")
else:
    print(f"Number of groups formed: {n1//n2+1}")