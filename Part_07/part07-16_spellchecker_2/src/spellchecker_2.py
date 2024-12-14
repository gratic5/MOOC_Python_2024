# Write your solution here

import difflib

l1 = []
with open("wordlist.txt") as w:
    for i in w:
        j = i.strip()
        l1.append(j)

input1 = input("write text: ")

k = input1.split(" ")

wrong_words = []
for i,j in enumerate(k):
    if(j.lower() in l1):
        continue
    else:
        wrong_words.append(j)
        k[i] = f"*{k[i]}*"


string1 = ""
for i,j in enumerate(k):
    string1 += j +" "

string1 = string1[:-1]

l2 = []
for k,l in enumerate(wrong_words):
    d1 = {}
    d1[l] = []
    d1[l][:] = difflib.get_close_matches(l,l1)[:]
    l2.append(d1)

print(string1)
print("suggestions:")
for i,j in enumerate(l2):
    for k,v in j.items():
        string2 = ""
        for i1,j1 in enumerate(v):
            string2 += j1 + ", "
        print(f"{k}: {string2[:-2]}")



