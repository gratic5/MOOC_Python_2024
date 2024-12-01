# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
d1 = {}
with open(student_info) as a1:
    for i in a1:
        n1 = [x.strip() for x in i.split(";")]
        if(n1[0] == "id"):
            continue
        d1[n1[0]] = [n1[1]+" "+n1[2]]

with open(exercise_data) as a2:
    for i in a2:
        n1 = [x.strip() for x in i.split(";")]
        if(n1[0] == "id"):
            continue
        d1[n1[0]][1:8] = n1[1:8]
d2 = {}
for i,j in d1.items():
    sum1 = 0
    name = d1[i][0]
    for k,l in enumerate(j):
        if(k == 0):
            continue
        sum1 += int(l)
    d2[name] = sum1

for i,j in d2.items():
    print(f"{i} {j}")




