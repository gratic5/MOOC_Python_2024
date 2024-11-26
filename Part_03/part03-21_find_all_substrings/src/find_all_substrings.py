# Write your solution here
s1 = input("Please type in a word: ")
s2 = input("Please type in a character: ")

while(len(s1) >= 3 and (len(s1) - 1 - s1.find(s2) >= 2)):
    if(s2 not in s1):
        break
    else:
        print(s1[s1.find(s2):s1.find(s2)+3])
    s1 = s1[s1.find(s2)+1:]