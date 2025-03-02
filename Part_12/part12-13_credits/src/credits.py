from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(course_attempts : list):
    return reduce(lambda reduced_sum, i : reduced_sum + i.credits,course_attempts,0)

def sum_of_passed_credits(course_attempts : list):
    return reduce(lambda reduced_sum, j : reduced_sum +j.credits,list(filter(lambda i : i.grade >= 1,course_attempts)),0)

def average(course_attempts : list):
    return reduce(lambda reduced_sum, j : j.grade + reduced_sum,(filter(lambda i : i.grade >= 1,course_attempts)),0)/len(list(filter(lambda i : i.grade >= 1,course_attempts)))