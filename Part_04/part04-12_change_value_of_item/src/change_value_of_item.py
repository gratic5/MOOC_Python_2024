# Write your solution here

list1 = [1,2,3,4,5]

while(True):
    n1 = int(input("Index: "))
    if(n1 == -1):
        break
    else:
        n2 = int(input("New value: "))
        list1[n1] = n2
        print(list1)