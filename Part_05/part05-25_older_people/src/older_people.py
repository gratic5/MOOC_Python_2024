# Write your solution here
def older_people(people : list, year: int):
    l1 = []
    for i in people:
        if(i[1] < year):
            l1.append(i[0])
    return l1