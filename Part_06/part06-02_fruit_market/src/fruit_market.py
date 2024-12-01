# write your solution here
def read_fruits():
    d1 = {}
    with open("fruits.csv") as n1:
        for i in n1:
            i = i.replace("\n","")
            n2 = i.split(";")
            d1[n2[0]] = float(n2[1])
    return d1