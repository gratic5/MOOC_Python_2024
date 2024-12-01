# write your solution here
def largest():
    largest1 = 0
    with open("numbers.txt") as new_file:
        for i in new_file:
            i = i.replace("\n","")
            if(int(i) > largest1):
                largest1 = int(i)
    return largest1