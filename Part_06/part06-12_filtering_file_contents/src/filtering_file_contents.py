# Write your solution here
def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv") as n:
        for i in n:
            x = i.split(";")
            y = [j.strip() for j in x]
            z = list(y[1])
            a = ""
            b = ""
            c = ""
            e = 0
            for o,k in enumerate(z):
                if(k not in "1234567890"):
                    e = o
                    c = k
                    break
                a += k
            for p in range(e+1,len(z)):
                b += z[p]
            d = 0
            if(c == "+"):
                d = int(a)+int(b)
            elif(c == "-"):
                d = int(a)-int(b)
            if(d == int(y[2])):
                correct.append(i.strip())
            else:
                incorrect.append(i.strip())
    with open("correct.csv","w") as c:
        for i in correct:
            c.write(i+"\n")
    with open("incorrect.csv","w") as i:
        for j in incorrect:
            i.write(j+"\n")

