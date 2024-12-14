# Write your solution here
import string

def separate_characters(my_string : str):
    s1 = ""
    s2 = ""
    s3 = ""
    for i in my_string:
        if(i in string.ascii_letters):
            s1 += i
        elif(i in string.punctuation):
            s2 += i
        else:
            s3 += i
    return (s1,s2,s3)
