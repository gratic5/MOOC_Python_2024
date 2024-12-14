# Write your solution here
import string
def run(program):
    dict1 = {}
    l1 = []
    i = 0
    for i1 in string.ascii_uppercase:
        dict1[i1] = 0
    while(i < len(program)):
        k = program[i].split(" ")

        if(k[0]) == "MOV":
            if(k[2].isdigit()):
                dict1[k[1]] = int(k[2])
                i += 1
            elif(k[2] in string.ascii_uppercase):
                dict1[k[1]] = dict1[k[2]]
                i += 1
        elif(k[0] == "ADD"):
            if(k[2] in string.ascii_uppercase):
                dict1[k[1]] = dict1[k[1]]+dict1[k[2]]
                i += 1
            elif(k[2] in string.digits):
                dict1[k[1]] = dict1[k[1]]+int(k[2])
                i += 1
        elif(k[0] == "SUB"):
            if(k[2] in string.ascii_uppercase):
                dict1[k[1]] = dict1[k[1]]-dict1[k[2]]
                i += 1
            elif(k[2] in string.digits):
                dict1[k[1]] = dict1[k[1]]-int(k[2])
                i += 1
        elif(k[0] == "MUL"):
            if(k[2] in string.ascii_uppercase):
                dict1[k[1]] = dict1[k[1]]*dict1[k[2]]
                i += 1
            elif(k[2] in string.digits):
                dict1[k[1]] = dict1[k[1]]*int(k[2])
                i += 1
        elif(k[0] == "PRINT"):
            if(k[1] in string.ascii_uppercase):
                l1.append(dict1[k[1]])
                i += 1
            elif(k[1].isdigit()):
                l1.append(int(k[1]))
                i += 1
        elif(k[0] == "END"):
            break
        elif(k[0] == "JUMP"):
            i = program.index(f"{k[1]}:")

        elif(k[0] == "IF"):
            if k[2] == "==":
                if(k[3] in string.ascii_uppercase):
                    if dict1[k[1]] == dict1[k[3]]:
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
                elif(k[3].isdigit()):
                    if dict1[k[1]] == int(k[3]):
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1

            elif k[2] == "!=":
                if(k[3] in string.ascii_uppercase):
                    if dict1[k[1]] != dict1[k[3]]:
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
                elif(k[3].isdigit()):
                    if dict1[k[1]] != int(k[3]):
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
            
            elif k[2] == ">=":
                if(k[3] in string.ascii_uppercase):
                    if dict1[k[1]] >= dict1[k[3]]:
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
                elif(k[3].isdigit()):
                    if dict1[k[1]] >= int(k[3]):
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1

            elif k[2] == "<=":
                if(k[3] in string.ascii_uppercase):
                    if dict1[k[1]] <= dict1[k[3]]:
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
                elif(k[3].isdigit()):
                    if dict1[k[1]] <= int(k[3]):
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
            
            elif k[2] == "<":
                if(k[3] in string.ascii_uppercase):
                    if dict1[k[1]] < dict1[k[3]]:
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
                elif(k[3].isdigit()):
                    if dict1[k[1]] < int(k[3]):
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
            
            elif k[2] == ">":
                if(k[3] in string.ascii_uppercase):
                    if dict1[k[1]] > dict1[k[3]]:
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1

                elif(k[3].isdigit()):
                    if dict1[k[1]] > int(k[3]):
                        i = program.index(f"{k[5]}:")
                    else:
                        i += 1
                    
        else:
            i += 1

    return l1





