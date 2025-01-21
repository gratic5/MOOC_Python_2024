# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:

    def __init__(self):
        self.people = []

    def add(self, person : Person):
        self.people.append(person)
    
    def is_empty(self):
        return not bool(self.people)
    
    def print_contents(self):
        print(f"There are {len(self.people)} persons in the room, and their combined height is {sum(i.height for i in self.people)} cm")
        for i in self.people:
            print(f"{i.name} ({i.height})")
    
    def shortest(self):
        if(self.people == []):
            return None
        else:
            shortest2 = self.people[0]
            shortest1 = self.people[0].height
            for i in range(1,len(self.people)):
                if(shortest1 > self.people[i].height):
                    shortest1 = self.people[i].height
                    shortest2 = self.people[i]
            return shortest2
    
    def remove_shortest(self):
        shortest_peron = self.shortest()

        if(shortest_peron is None):
            return None

        i = self.people.index(shortest_peron)
        j = self.people.pop(i)

        return j



