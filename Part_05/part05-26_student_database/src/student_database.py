# Write your solution here
def add_student(students : dict, name : str):
    l1 = []
    students[name] = l1

def print_student(students : dict, name : str):
    if(name in students):
        print(f"{name}:")
        if(not students[name]):
            print(" no completed courses")
        else:
            sum1 = 0
            total_courses = 0
            print(f" {len(students[name])} completed courses:")
            for j in students[name]:
                sum1 += j[1]
                print(f"  {j[0]} {j[1]}")
            print(f" average grade {sum1/len(students[name])}")
    else:
        print(f"{name.title()}: no such person in the database")
    
def add_course(students : dict, name : str, a : tuple):
    if(a[1] == 0):
        return
    for h,i in enumerate(students[name]):
        if(a[0] == i[0] and(a[1] < i[1])):
            return
        elif(a[0] == i[0] and(a[1] > i[1])):
            students[name][h] = a
            return
    students[name].append(a)

def summary(students : dict):
    total = 0
    current_courses_name = ""
    current_courses = 0
    most_courses = 0
    most_courses_name = ""
    best_average_grade_name = ""
    best_average_grade = 0
    for i,j in students.items():
        total += 1
        current_courses_name = i
        current_courses = 0
        current_average_grade_name = i
        current_average_grade = 0
        for k in students[i]:
            current_courses += 1
            current_average_grade += k[1]
        if(best_average_grade < current_average_grade/current_courses):
            best_average_grade = current_average_grade/current_courses
            best_average_grade_name = current_average_grade_name
        if(most_courses < current_courses):
            most_courses = current_courses
            most_courses_name = current_courses_name 
    print(f"students {total}\nmost courses completed {most_courses} {most_courses_name}\nbest average grade {best_average_grade} {best_average_grade_name}")
