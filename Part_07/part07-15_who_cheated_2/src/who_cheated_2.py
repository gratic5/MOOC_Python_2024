# Write your solution here
import datetime

def final_points():
    l1 = []
    with open("start_times.csv") as s:
        for i in s:
            j = i.split(";")
            k = [x.strip() for x in j]
            d1 = {}
            d1["Name"] = k[0]
            hours = k[1][:2]
            minutes = k[1][3:]
            if(k[1][0] == "0"):
                hours = k[1][1]
            if(k[1][3] == "0"):
                minutes = k[1][4]
            d1["Starting Time"] = datetime.datetime(2001,1,1,int(hours),int(minutes))
            l1.append(d1)
    
    with open("submissions.csv") as b:
        for i1 in b:
            j1 = i1.split(";")
            k1 = [x1.strip() for x1 in j1]
            hours = k1[3][:2]
            minutes = k1[3][3:]
            if(k1[3][0] == "0"):
                hours = k1[3][1]
            if(k1[3][3] == "0"):
                minutes = k1[3][4]
            for i2,j2 in enumerate(l1):
                if(k1[0] == j2["Name"]):
                    if(f"task {k1[1]}" in j2):
                        if(datetime.datetime(2001,1,1,int(hours),int(minutes)) - j2["Starting Time"] < datetime.timedelta(hours=3)):
                            if(j2[f"task {k1[1]}"][1] < k1[2]):
                                j2[f"task {k1[1]}"] = ((datetime.datetime(2001,1,1,int(hours),int(minutes))),k1[2])
                    else:
                        if(datetime.datetime(2001,1,1,int(hours),int(minutes)) - j2["Starting Time"] < datetime.timedelta(hours=3)):
                            j2[f"task {k1[1]}"] = ((datetime.datetime(2001,1,1,int(hours),int(minutes))),k1[2])
    d3 = {}
    for i4,j4 in enumerate(l1):
        sum1 = 0
        for k2,v2 in j4.items():
            if(k2 != "Name" and k2 != "Starting Time"):
                sum1 += int(v2[1])
        d3[j4["Name"]] = sum1

    return d3
