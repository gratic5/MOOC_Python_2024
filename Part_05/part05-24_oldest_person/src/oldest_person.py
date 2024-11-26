# Write your solution here
def oldest_person(people : list):
    name = people[0][0]
    age = people[0][1]
    for i in people:
        if(i[1] < age):
            name = i[0]
            age = i[1]
    return name