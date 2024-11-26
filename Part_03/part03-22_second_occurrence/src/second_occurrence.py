s1 = input("Please type in a string: ")
s2 = input("Please type in a substring: ")
s3 = s1
index = 0

if s2 in s3:
    index = s3.find(s2)
    s3 = s3[s3.find(s2)+len(s2):]
    if(s2 in s3):
        index += s3.find(s2)
        print(f"The second occurrence of the substring is at index {index+len(s2)}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")