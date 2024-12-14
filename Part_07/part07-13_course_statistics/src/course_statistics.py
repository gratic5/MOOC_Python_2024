# Write your solution here
import json, urllib.request, math

def retrieve_all():
    f = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = f.read()
    final_data = json.loads(data)

    l1 = []
    for i,j in enumerate(final_data):
        t1 = ()
        if(j["enabled"]):
            t1 = (j["fullName"],j["name"],j["year"],sum(j["exercises"]))
            l1.append(t1)
    return l1

def retrieve_course(course_name : str):
    f = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    raw_data = f.read()
    final_data = json.loads(raw_data)

    d1 = {}
    d1["weeks"] = len(final_data)
    
    students = []
    hours = 0
    exercises = 0
    for k,v in final_data.items():
        students.append(v["students"])
        hours += v["hour_total"]
        exercises += v["exercise_total"]

    d1["students"] = max(students)
    d1["hours"] = hours
    d1["hours_average"] = math.floor(hours/max(students))
    d1["exercises"] = exercises
    d1["exercises_average"] = math.floor(exercises/max(students))

    return d1