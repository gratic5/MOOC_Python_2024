# tee ratkaisu tänne


a = input("Student information: ")
b = input("Exercises completed: ")
c = input("Exam points: ")
d = input("Course information: ")

def student_info(student_file : str):
    l1 = []
    with open(student_file) as s:
        for i in s:
            d1 = {}
            x = i.split(";")
            y = [j.strip() for j in x]
            if(y[0] == "id"):
                continue
            d1["id"] = y[0]
            d1["First Name"] = y[1]
            d1["Last Name"] = y[2]
            l1.append(d1)
    return l1

def exercise_info(filename : str):
    list1 = student_info(a)
    with open(filename) as e:
        for i in e:
            x = i.split(";")
            y = [j.strip() for j in x]
            if(y[0] == "id"):
                continue
            for k,l in enumerate(list1):
                if(l["id"] == y[0]):
                    l["Exercises"] = []
                    l["Exercises"][:] = y[1:]
    return list1

def exam_info(filename : str):
    list1 = exercise_info(b)
    with open(filename) as ex:
        for i in ex:
            x = i.split(";")
            y = [j.strip() for j in x]
            if(y[0] == "id"):
                continue
            for k,l in enumerate(list1):
                if(l["id"] == y[0]):
                    l["examPoints"] = []
                    l["examPoints"][:] = y[1:]
    return list1
        
def results():
    l1 = exam_info(c)
    l2 = []
    for i,j in enumerate(l1):
        d1 = {}
        grade = 0
        d1["id"] = j["id"]
        d1["Name"] =  j["First Name"] +" "+ j["Last Name"]
        d1["exec_nbr"] = sum([int(o) for o in j["Exercises"]])
        d1["exec_pts."] = sum([int(o) for o in j["Exercises"]])//4
        d1["exm_pts."] = sum([int(o) for o in j["examPoints"]])
        d1["tot_pts."] = (sum([int(o) for o in j["Exercises"]])//4 + sum([int(o) for o in j["examPoints"]]))
        t1 = (sum([int(o) for o in j["Exercises"]])//4 + sum([int(o) for o in j["examPoints"]]))
        if(t1 < 15):
            grade = 0
        elif(t1 < 18):
            grade = 1
        elif(t1 < 21):
            grade = 2
        elif(t1 < 24):
            grade = 3
        elif(t1 < 28):
            grade = 4
        elif(t1 >= 28):
            grade = 5
        d1["grade"] = grade
        l2.append(d1)
    return l2

def results_print(fileName : str):
    l1 = results()
    l2 = []
    name = ""
    with open(fileName) as c:
        for i in c:
            x = i.split(":")
            y = [j.strip() for j in x]
            l2.append(y)
    name = l2[0][1] +", "+l2[1][1] + " credits"
    
    with open("results.txt","w") as n:
        n.write(name+"\n")
        n.write(f"{len(name)*'='}\n")
        n.write(f"{'name':30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n")
        for i,j in enumerate(l1):
            n.write(f"{j['Name']:30}{j['exec_nbr']:<10}{j['exec_pts.']:<10}{j['exm_pts.']:<10}{j['tot_pts.']:<10}{j['grade']:<10}\n")
    
    with open("results.csv","w") as r:
        for i,j in enumerate(l1):
            r.write(f"{j['id']};{j['Name']};{j['grade']}\n")
    print("Results written to files results.txt and results.csv")

results_print(d)

