# Write your solution here
def filter_incorrect():
    with open("correct_numbers.csv","w") as my_file:
        pass
    count = 0
    y = []
    with open("lottery_numbers.csv") as a:
        for i in a:
            count += 1
            flag = True
            x = i.split(";")
            z = [j.strip() for j in x]
            if (not y):
                y.append(z[0])
            else:
                y[0] = z[0]
            w = z[1].split(",")
            if(len(w) != 7):
                continue
            y[1:] = w[:]
            if(y[0] != f"week {count}"):
                flag = False
            elif(not y[1].isdigit() or not y[2].isdigit() or not y[3].isdigit() or not y[4].isdigit() or not y[5].isdigit() or not y[6].isdigit() or not y[7].isdigit()):
                flag = False
            elif((int(y[1]) > 39  or int(y[1]) < 1) or (int(y[2]) > 39  or int(y[2]) < 1) or (int(y[3]) > 39  or int(y[3]) < 1) or (int(y[4]) > 39  or int(y[4]) < 1) or (int(y[5]) > 39  or int(y[5]) < 1) or (int(y[6]) > 39  or int(y[6]) < 1) or (int(y[7]) > 39  or int(y[7]) < 1)):
                flag = False
            for p,q in enumerate(w):
                for r in range(p,len(w)):
                    if(w[p] == w[r] and p != r):
                        flag = False
            with open("correct_numbers.csv","a") as c:
                if(flag):
                    c.write(i)
