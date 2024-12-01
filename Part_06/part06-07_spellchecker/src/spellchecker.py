# write your solution here

a = input("Write text: ")

b = a.split(" ")

words = []
with open("wordlist.txt") as w:
    for i in w:
        word = i.strip()
        words.append(word)

for i,j in enumerate(b):
    if(j.lower() not in words):
        b[i] = b[i].replace(b[i],"*"+b[i]+"*")
string1 = ""
for i,j in enumerate(b):
    string1 += j+" "
string1 = string1[:-1]
print(string1)

