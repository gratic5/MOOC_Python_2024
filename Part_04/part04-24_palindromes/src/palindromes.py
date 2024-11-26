# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(a :str) -> bool:
    flag = True
    for i in range(len(a)):
        if(a[i] != a[len(a) - 1 - i]):
            flag = False
    return flag

while(True):
    s1 = input("Please type in a palindrome: ")
    if(palindromes(s1)):
        print(f"{s1} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")