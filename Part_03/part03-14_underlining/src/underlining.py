# Write your solution here
flag = True
while(flag):
    s1 = input("Please type in a string: ")
    if(s1 == ""):
        flag = False
    else:
        print(f"{s1}\n{len(s1)*'-'}")