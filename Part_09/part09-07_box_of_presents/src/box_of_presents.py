# WRITE YOUR SOLUTION HERE:

class Present:

    def __init__(self, name : str, weight : int):
        
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"The name of the present: {self.name}\nThe weight of the present: {self.weight}\nPresent: {self.name} ({self.weight})"
    
class Box:

    def __init__(self):
        self.items = []

    def add_present(self, present : Present):
        self.items.append(present)

    def total_weight(self):
        return sum(i.weight for i in self.items)
    