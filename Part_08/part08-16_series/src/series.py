# Write your solution here:

class Series:

    def __init__(self,title : str, total_seasons : int, genre : list):
        self.title = title
        self.total_seasons = total_seasons
        self.genre = genre
        self.rating = None

    def __str__(self):
        str1 = f"{self.title} ({self.total_seasons} seasons)\ngenres: {", ".join(self.genre)}"

        if(self.rating):
            str1 += f"\n{len(self.rating)} ratings, average {(sum(self.rating)/len(self.rating)):.1f} points"
        
        else:
            str1 += f"\nno ratings"

        return str1
    
    def rate(self, rating : int):
        if(self.rating):
            self.rating.append(rating)
        else:
            self.rating = []
            self.rating.append(rating)

def minimum_grade(rating : float, series_list : list):
    
    l1 = []
    for i in series_list:
        if((sum(i.rating)/len(i.rating)) >= rating):
            l1.append(i)
    
    return l1

def includes_genre(genre : str, series_list : list):
    
    l1 = []
    for i in series_list:
        if(genre in i.genre):
            l1.append(i)
    
    return l1
