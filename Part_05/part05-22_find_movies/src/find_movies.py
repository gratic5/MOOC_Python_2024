# Write your solution here
def find_movies(database : list, search_term : str):
    new_db = []
    for i in database:
        if(search_term.lower() in (i["name"]).lower()):
            new_db.append(i)
    return new_db
