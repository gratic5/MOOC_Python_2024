# Write your solution here
list1 = []

while(True):
    n1 = int(input("New item: "))
    if(n1 == 0):
        print("Bye!")
        break
    list1.append(n1)
    print(f"The list now: {list1}")
    print(f"The list in order: {sorted(list1)}")
