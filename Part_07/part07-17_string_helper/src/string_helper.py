# Write your solution here
import string
def change_case(orig_string : str) -> str:
    new_string = ""
    for i in orig_string:
        if(i == i.lower()):
            new_string += i.upper()
        elif(i == i.upper()):
            new_string += i.lower()
    return new_string

def split_in_half(orig_string : str):
    string1 = orig_string[:len(orig_string)//2]
    string2 = orig_string[len(orig_string)//2:]

    return (string1,string2)

def remove_special_characters(orig_string: str) -> str:
    new_string = ""
    for i in orig_string:
        if(i in string.ascii_letters or i in string.digits or i in " "):
            new_string += i
    return new_string




