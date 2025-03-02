
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    elif(len(my_string) == 1):
        if(my_string[0] == "(" or my_string[0]== ")" or my_string[0] == "[" or my_string[0] == "]"):
            return False
    if(my_string[0] == "(" and my_string[-1] == "]"):
        return False
    elif(my_string[0] == "[" and my_string[-1] == ")"):
        return False
    elif(my_string[0] == "(" and my_string[-1] != ")"):
        return balanced_brackets(my_string[:-1])
    elif(my_string[0] != "(" and my_string[-1] == ")"):
        return balanced_brackets(my_string[1:])
    elif(my_string[0] == "[" and my_string[-1] != "]"):
        return balanced_brackets(my_string[:-1])
    elif(my_string[0] != '[' and my_string[-1] == "]"):
        return balanced_brackets(my_string[1:])
    elif(my_string[0] != "(" and my_string[0] != "[" and my_string[-1] != ")" and my_string[-1] != "]"):
        return balanced_brackets(my_string[1:-1])
    
    # remove first and last character
    return balanced_brackets(my_string[1:-1])

