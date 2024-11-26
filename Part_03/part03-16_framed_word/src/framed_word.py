# Write your solution here
s1 = input("Word: ")
print(30*"*")

if(len(s1) % 2 == 0):
    print(f"*{((28-len(s1))//2)*' '}{s1}{((28-len(s1))//2)*' '}*")
else:
    print(f"*{((28-len(s1))//2)*' '}{s1}{(((28-len(s1))//2)+1)*' '}*")
print(30*'*')