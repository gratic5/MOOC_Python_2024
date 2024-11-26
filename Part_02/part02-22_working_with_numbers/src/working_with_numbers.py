# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
sum1 = 0
count = 0
positive = 0
negative = 0
while(True):
    n1 = int(input("Number: "))
    if(n1 == 0):
        break
    sum1 += n1
    count += 1
    mean = sum1/count
    if(n1 > 0):
        positive += 1
    else:
        negative += 1

print(f"Numbers typed in {count}\nThe sum of the numbers is {sum1}\nThe mean of the numbers is {sum1/count}\nPositive numbers {positive}\nNegative numbers {negative}")

    
    

