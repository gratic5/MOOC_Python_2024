# Write your solution here
list1 = []

while(True):
    s1 = input("Word: ")
    if(s1 in list1):
        print(f"You typed in {len(list1)} different words")
        break
    list1.append(s1)
