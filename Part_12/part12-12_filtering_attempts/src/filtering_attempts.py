class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts : list):
    return list(filter(lambda i : i.grade >= 1 ,attempts))

def attempts_with_grade(attempts : list, grade : int):
    return list(filter(lambda i : i.grade == grade,attempts))

def passed_students(attempts : list, course : str):
    return sorted(list(map(lambda k : k.student_name,filter(lambda i : i.grade > 0 and i.course_name == course,attempts))))