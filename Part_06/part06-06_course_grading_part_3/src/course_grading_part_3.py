# tee ratkaisu tänne
if True:
    a = input("Student information: ")
    b = input("Exercises completed: ")
    c = input("Exam points: ")

l1 = []

with open(a) as n:
    for i in n:
        d1 = {}
        y = i.split(";")
        y = [x.strip() for x in y]
        if(y[0] == "id"):
            continue
        d1["id"] = y[0]
        d1["First Name"] = y[1]
        d1["Last Name"] = y[2]
        l1.append(d1)

with open(b) as n:
    for i in n:
        l2 = []
        y = i.split(";")
        y = [x.strip() for x in y]
        if(y[0] == "id"):
            continue
        l2[:] = y[1:8]
        for j,k in enumerate(l1):
            if(l1[j]["id"] == y[0]):
                l1[j]["Exercises"] = l2

with open(c) as n:
    for i in n:
        l2 = []
        y = i.split(";")
        y = [x.strip() for x in y]
        if(y[0] == "id"):
            continue
        l2[:] = y[1:4]
        for j,k in enumerate(l1):
            if(l1[j]["id"] == y[0]):
                l1[j]["Exam"] = l2


l2 = []
for i,j in enumerate(l1):
    d2 = {}
    name = l1[i]["First Name"] + " "+ l1[i]["Last Name"]
    x = [int(j) for j in l1[i]["Exercises"]]
    exercises = sum(x)
    y = [int(j) for j in l1[i]["Exam"]]
    exam = sum(y)
    d2[name] = []
    d2[name].append(exercises)
    d2[name].append(exam)
    l2.append(d2)
print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
for i,j in enumerate(l2):
    for k,l in j.items():
        name = k
        exercises = l[0]
        exam_points = l[1]
        grade = 0
        if(exercises//4  +exam_points < 15):
            grade = 0
        elif(exercises//4 + exam_points < 18):
            grade = 1
        elif(exercises//4 + exam_points < 21):
            grade = 2
        elif(exercises//4 + exam_points < 24):
            grade = 3
        elif(exercises//4 + exam_points < 28):
            grade = 4
        elif(exercises//4 + exam_points >= 28):
            grade = 5
        print(f"{k:30}{exercises:<10}{(exercises//4):<10}{exam_points:<10}{(exercises//4)+exam_points:<10}{grade:<10}")
