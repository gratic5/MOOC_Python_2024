# write your solution here
def matrix_sum():
    sum1 = 0
    with open("matrix.txt") as n1:
        for i in n1:
            i = i.replace("\n","")
            n2 = [int(x) for x in i.split(",")]
            for j in n2:
                sum1 += j
    return sum1

def matrix_max():
    max_digit = 0
    with open("matrix.txt") as n1:
        for i in n1:
            i = i.replace("\n","")
            n2 = [int(x) for x in i.split(",")]
            for j in n2:
                if(j > max_digit):
                    max_digit = j
    return max_digit

def row_sums():
    row_totals = []
    with open("matrix.txt") as n1:
        for i in n1:
            row_sum = 0
            i = i.replace("\n","")
            n2 = [int(x) for x in i.split(",")]
            for j in n2:
                row_sum += j
            row_totals.append(row_sum)
    return row_totals
