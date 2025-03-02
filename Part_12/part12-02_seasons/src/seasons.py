# Write your solution here:

def sort_by_seasons(items : list):

    def tv_show_number(item : dict):
        return item["seasons"]
    
    return sorted(items, key=tv_show_number)
