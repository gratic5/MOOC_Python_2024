# Write your solution here
# Remember the import statement
# from datetime import date

from datetime import date

def list_years(dates : list):
    l1 = [x.year for x in dates]
    l1.sort()
    return l1
