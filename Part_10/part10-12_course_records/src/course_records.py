# tee ratkaisusi tänne

class Course:

    def __init__(self, name : str):
        self.name = name
        self.grade = None
        self.credits = None

    def add_grade(self, grade : str):
        if(self.grade == None or grade > self.grade):
            self.grade = grade

    def add_credits(self, credits : str):
        if(self.credits == None):
            self.credits = credits
    
     

class CourseList:

    def __init__(self):
        self.__course_list = []

    def add_course(self, name : str, grade : str, credits : str):
        flag = False
        for i in self.__course_list:
            if(i.name == name):
                i.add_credits(credits)
                i.add_grade(grade)
                flag = True
        if(flag == False):
            c1 = Course(name)
            c1.add_credits(credits)
            c1.add_grade(grade)
            self.__course_list.append(c1)

    def __get_course(self, name):
        for i in self.__course_list:
            if(i.name == name):
                return i
        return None
    
    def get_course_data(self, n1):
        course1 = self.__get_course(n1)
        if(course1 == None):
            print("no entry for this course")
        else:
            print(f"{course1.name} ({course1.credits} cr) grade {course1.grade}")

    def __grade_distribution(self):
        five_stars = 0
        four_stars = 0
        three_stars = 0
        two_stars = 0
        one_star = 0
        for i in self.__course_list:
            if(i.grade == "5"):
                five_stars += 1
            elif(i.grade == "4"):
                four_stars += 1
            elif(i.grade == "3"):
                three_stars += 1
            elif(i.grade == "2"):
                two_stars += 1
            elif(i.grade == "1"):
                one_star += 1

        print(f"5: {five_stars*'x'}\n4: {four_stars*'x'}\n3: {three_stars*'x'}\n2: {two_stars*'x'}\n1: {one_star*'x'}")



    def get_statistics(self):
        total_grades = sum(int(i.grade) for i in self.__course_list)
        total_credits = sum(int(i.credits) for i in self.__course_list)
        print(f"{len(self.__course_list)} completed courses, a total of {total_credits} credits")
        print(f"mean {total_grades/len(self.__course_list):.1f}")
        print("grade distribution")
        self.__grade_distribution()


class CourseInterface:

    def __init__(self):
        self.interface = CourseList()

    def execute(self):
        print(f"1 add course\n2 get course data\n3 statistics\n0 exit")
        while(True):
            print()
            i1 = input("command: ")

            if(i1 == "0"):
                break
            elif(i1 == "1"):
                n1 = input("course: ")
                g1 = input("grade: ")
                c1 = input("credits: ")
                self.interface.add_course(n1, g1, c1)

            elif(i1 == "2"):
                n1 = input("course: ")
                self.interface.get_course_data(n1)

            elif(i1 == "3"):
                self.interface.get_statistics()


c1 = CourseInterface()
c1.execute()