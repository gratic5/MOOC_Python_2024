# Write your solution here
word = ""
while(True):
    i1 = input("Please type in a word: ")
    if(i1 == "end"):
        break
    if(word != ""):
        i2 = word.split(" ")
        i2 = i2[:-1]
        if i1 == i2[-1]:
            word = word[:-1]
            break
    word += i1 +" "

print(word)
