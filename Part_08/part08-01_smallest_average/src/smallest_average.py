# Write your solution here

def smallest_average(person1 : dict, person2 : dict, person3 : dict):
    
    average1 = 0
    average2 = 0
    average3 = 0
    for i in range(1,4):
        average1 += person1[f"result{i}"]
        average2 += person2[f"result{i}"]
        average3 += person3[f"result{i}"]
    
    if(average1 < average2 and average1 < average3):
        return person1
    elif(average2 < average3):
        return person2
    else:
        return person3

