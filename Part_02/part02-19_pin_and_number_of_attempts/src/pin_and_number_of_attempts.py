# Write your solution here
attempts = 1
while(True):
    p1 = int(input("PIN: "))
    if(p1 == 4321 and attempts != 1):
        print(f"Correct! It took you {attempts} attempts")
        break
    elif(p1 == 4321 and attempts == 1):
        print(f"Correct! It only took you one single attempt!")
        break
    else:
        attempts += 1
        print("Wrong")

