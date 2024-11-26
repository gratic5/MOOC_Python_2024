# Write your solution here
y1 = int(input("Year: "))
y2 = y1


while(True):
    y2 += 1
    if(y2 % 4 == 0):
        if(y2 % 100 == 0):
            if(y2 % 400 == 0):
                print(f"The next leap year after {y1} is {y2}")
                break
        else:
            print(f"The next leap year after {y1} is {y2}")
            break



