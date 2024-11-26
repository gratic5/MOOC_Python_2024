# Write your solution here

s1 = input("Please type in a string: ")
if(len(s1) >= 20):
    print(s1[:20])
else:
    print(f"{(20-len(s1))*'*'}{s1}")