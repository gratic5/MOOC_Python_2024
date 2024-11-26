# Write your solution here
while(True):
    s1 = input("Editor: ")
    if(s1.lower() == "visual studio code"):
        print("an excellent choice!")
        break
    elif(s1.lower() == "word" or s1.lower() == "notepad"):
        print("awful")
    else:
        print("not good")
