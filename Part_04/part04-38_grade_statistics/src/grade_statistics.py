# Write your solution here
def student_input():
    l1 = []
    while(True):
        n1 = input("Exam points and exercises completed: ")
        if(n1 == ""):
            break
        l2 = [int(i) for i in n1.split(" ")]
        l1.append(l2)

    print("Statistics:")
    return l1

def points_average(a : list):
    sum1 = 0
    for i in a:
        sum1 += i[0] + (i[1]//10)
    print(f"Points average: {sum1/len(a)}")

def Pass_Percentage(a : list):
    fail = 0
    for i in a:
        if(i[0] < 10):
            fail += 1
        elif(i[0] + (i[1]//10) < 15):
            fail += 1
    print(f"Pass percentage: {(((len(a) - fail)/len(a))*100):.1f}")

def Grade_distribution(a : list):
    print("Grade distribution:")
    
    n5 = 0
    n4 = 0
    n3 = 0
    n2 = 0
    n1 = 0
    n0 = 0

    for i in a:
        if(i[0] < 10):
            n0 += 1
        elif((i[0] + i[1]//10) < 15):
            n0 += 1
        elif(i[0] + i[1]//10 < 18):
            n1 += 1
        elif(i[0] + i[1]//10 < 21):
            n2 += 1
        elif(i[0] + i[1]//10 < 24):
            n3 += 1
        elif(i[0] + i[1]//10 < 28):
            n4 += 1
        elif(i[0] + i[1]//10 < 31):
            n5 += 1
    print(f"5: {n5*"*"}\n4: {n4*"*"}\n3: {n3*"*"}\n2: {n2*"*"}\n1: {n1*"*"}\n0: {n0*"*"}")

b = student_input()
points_average(b)
Pass_Percentage(b)
Grade_distribution(b)