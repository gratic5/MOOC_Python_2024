# Write your solution here
while(True):
    print("1 - add an entry, 2 - read entries, 0 - quit")
    s1 = input("Function: ")
    if(s1 == "1"):
        s2 = input("Diary entry: ")
        with open("diary.txt","a") as d:
            d.write(s2+"\n")
    elif(s1 == "0"):
        print("Bye now!")
        break
    elif(s1 == "2"):
        with open("diary.txt") as d:
            for i in d:
                print(i.strip())
