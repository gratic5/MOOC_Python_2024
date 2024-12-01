# wwite your solution here

a = input("Student information: ")
b = input("Exercises completed: ")
c = input("Exam points: ")

l1 = []

with open(a) as n1:
    for i in n1:
        d2 = {}
        n2 = [x.strip() for x in i.split(";")]
        if(n2[0] == "id"):
            continue
        d2["id"] = n2[0]
        d2["First Name"] = n2[1]
        d2["Last Name"] = n2[2]
        l1.append(d2)

with open(b) as n2:
    for i in n2:
        l2 = []
        n3 = [x.strip() for x in i.split(";")]
        for j,k in enumerate(l1):
            if(k["id"] == n3[0]):
                l2 = n3[1:]
                l1[j]["Exercise"] = l2

with open(c) as n:
    for i in n:
        n1 = [x.strip() for x in i.split(";")]
        l2 = []
        for j,k in enumerate(l1):
            if(k["id"] == n1[0]):
                l2 = n1[1:]
                l1[j]["Exam"] = l2

d3 = {}
for i,j in enumerate(l1):
    name = l1[i]["First Name"] +" "+l1[i]["Last Name"]
    Exercises = [int(x) for x in l1[i]["Exercise"]]
    exam_points = [int(y) for y in l1[i]["Exam"]]
    d3[name] = []
    d3[name].append(sum(Exercises))
    d3[name].append(sum(exam_points))


for i,j in d3.items():
    name = i
    exercise_points = j[0]//4
    exam_score = j[1]
    if(exam_score + exercise_points < 15):
        print(f"{name} 0")
    elif(exam_score + exercise_points < 18):
        print(f"{name} 1")
    elif(exam_score + exercise_points < 21):
        print(f"{name} 2")
    elif(exam_score + exercise_points < 24):
        print(f"{name} 3")
    elif(exam_score + exercise_points < 28):
        print(f"{name} 4")
    elif(exam_score + exercise_points >= 28):
        print(f"{name} 5")
        