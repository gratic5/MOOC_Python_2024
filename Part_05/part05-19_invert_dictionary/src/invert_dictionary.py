# Write your solution here
def invert(dictionary : dict):
    new_dictionary = {}
    for i,j in dictionary.items():
        new_dictionary[j] = i
    for i,j in new_dictionary.items():
        if(j in dictionary):
            del(dictionary[j])
    for i,j in new_dictionary.items():
            dictionary[i] = j
            