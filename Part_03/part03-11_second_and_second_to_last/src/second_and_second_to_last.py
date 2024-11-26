# Write your solution here
s1 = input("Please type in a string: ")
if(s1[1] == s1[-2]):
    print(f"The second and the second to last characters are {s1[-2]}")
else:
    print("The second and the second to last characters are different")