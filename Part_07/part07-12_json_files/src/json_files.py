# Write your solution here
import json

def print_persons(filename : str):
    with open(filename) as f:
        data = f.read()
    courses = json.loads(data)
    for i,j in enumerate(courses):
        hobbies = ""
        for k,l in enumerate(j["hobbies"]):
            hobbies += l +", "
        print(f"{j['name']} {j['age']} years ({hobbies[:-2]})")

