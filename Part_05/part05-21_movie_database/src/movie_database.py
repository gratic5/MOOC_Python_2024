# Write your solution here
def add_movie(database : list, name : str, director : str, year : int, runtime : int):
    d1 = {"name" : name, "director" : director, "year" : year, "runtime" : runtime}
    database.append(d1)
