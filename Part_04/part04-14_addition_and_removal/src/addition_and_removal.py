# Write your solution here
list1 = []
count = 1
while(True):
    print(f"The list is now {list1}")
    s1 = input("a(d)d, (r)emove or e(x)it: ")
    if(s1 == "x"):
        print("Bye!")
        break
    elif(s1 == "d"):
        list1.append(count)
        count += 1
    elif(s1 == "r" and list1):
        list1.pop(-1)
        count -= 1

