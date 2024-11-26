# Write your solution here
def no_vowels(a  :str)->str:
    list1= ["a","e","i","o","u"]
    string2 = ""
    for i in a:
        if(i not in list1):
            string2 += i
    return string2
