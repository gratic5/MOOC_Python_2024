# Write your solution here

import csv, json, datetime

def cheaters():
    l1 = []
    reference_date1 = datetime.datetime(2001,1,1)
    with open("start_times.csv") as c:
        for i in c:
            d1 = {}
            kw = i.split(";")
            j = [x.strip() for x in kw]
            d1["Name"] = j[0]
            d1["Start Time"] = datetime.time(int(j[1][:2]),int(j[1][3:]))
            l1.append(d1) 

    with open("submissions.csv") as s:
        for i1 in s:
            j1 = i1.split(";")
            l = [x.strip() for x in j1]
            for i2,j2 in enumerate(l1):
                if(j2["Name"] == l[0]):
                    if(f"task{l[1]}" in j2):
                        if(datetime.datetime(2001,1,1,int(l[3][:2]),int(l[3][3:])) > datetime.datetime.combine(reference_date1,j2[f"task{l[1]}"][0])):
                            j2[f"task{l[1]}"] = (datetime.time(int(l[3][:2]),int(l[3][3:])),l[2])
                    else:
                        j2[f"task{l[1]}"] = (datetime.time(int(l[3][:2]),int(l[3][3:])),l[2])

    l3 = []
    l4 = []
    l5 = []
    l6 = []
    for i3,j3 in enumerate(l1):
        flag = True
        for i4,j4 in j3.items():
            if(i4 != "Name" and i4 != "Start Time"):
                if(datetime.datetime.combine(reference_date1,j4[0]) - datetime.datetime.combine(reference_date1,j3["Start Time"]) > datetime.timedelta(hours=3)):
                    flag = False
        if(flag):
            l3.append(j3)
        elif(not flag):
            l5.append(j3)

    print(l1)    
    for i6,j6 in enumerate(l3):
        l4.append(j6["Name"])

    for i7,j7 in enumerate(l5):
        l6.append(j7["Name"])
    return l6



