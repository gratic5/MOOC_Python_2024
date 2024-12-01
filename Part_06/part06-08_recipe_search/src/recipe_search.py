# Write your solution here
def recipe_call(file_name :str):
    l1 = []
    with open(file_name) as r:
        for i in r:
            l1.append(i.strip())

    l2 = []
    start = True
    for i,j in enumerate(l1):
        if(start and j):
            l2.append([j])
            start = False
        elif(j):
            l2[-1].append(j)
        else:
            start = True
    l3 = []
    for i,j in enumerate(l2):
        d1 = {}
        d1["Name"] = j[0]
        d1["Time"] = j[1]
        d1["Ingredients"] = []
        d1["Ingredients"][:] = j[2:]
        l3.append(d1)
    return l3


def search_by_name(filename : str, word : str):
    list1 = []
    recipe_lists = recipe_call(filename)
    for i,j in enumerate(recipe_lists):
        if(word.lower() in j["Name"].lower()):
            list1.append(j["Name"])
    return list1

def search_by_time(filename : str, prep_time : int):
    l4 = []
    recipe_lists = recipe_call(filename)
    for i,j in enumerate(recipe_lists):
        if(prep_time >= int(j["Time"])):
            l4.append(f"{j["Name"]}, preparation time {j["Time"]} min")
    return l4

def search_by_ingredient(filename: str, ingredient: str):
    recipe_lists = recipe_call(filename)
    l4 = []
    for i,j in enumerate(recipe_lists):
        for k,l in enumerate(j["Ingredients"]):
            if(ingredient.lower() == l.lower()):
                l4.append(f"{j["Name"]}, preparation time {j["Time"]} min")
    return l4
