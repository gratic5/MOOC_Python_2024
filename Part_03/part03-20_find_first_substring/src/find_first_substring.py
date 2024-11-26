# Write your solution here
s1 = input("Please type in a word: ")
s2 = input("Please type in a character: ")
if(s1.find(s2) != -1 and ((len(s1) - s1.find(s2) - 1)>=3)):
    print(s1[s1.find(s2):s1.find(s2)+3])

