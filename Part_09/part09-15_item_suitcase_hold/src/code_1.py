# Write your solution here:
class Item:

    def __init__(self, name : str, weight : int):
        self._name = name
        self._weight = weight

    def name(self):
        return self._name

    def weight(self):
        return self._weight

    def __str__(self):
        return f"{self._name} ({self._weight} kg)"
    
class Suitcase:

    def __init__(self, max_weight : int):
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item):
        if(self.max_weight >= self.__total_weight() + item.weight()):
            self.items.append(item)

    def __total_weight(self):
        return sum(item.weight() for item in self.items)
    
    def __str__(self):
        if(len(self.items) == 1):
            return f"{len(self.items)} item ({self.__total_weight()} kg)"
        return f"{len(self.items)} items ({self.__total_weight()} kg)"
    
    def print_items(self):
      for i in self.items:
          print(i)

    def weight(self):
        return self.__total_weight()
    
    def heaviest_item(self):
        heaviest = self.items[0]
        for i in self.items:
            if(i.weight() > heaviest.weight()):
                heaviest = i
        return heaviest

class CargoHold:

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.cargoHold = []

    def add_suitcase(self, suitcase : Suitcase):
        if(suitcase.weight() + self.__cargoHold_current_weight() <= self.max_weight):
            self.cargoHold.append(suitcase)
    
    def __cargoHold_current_weight(self):
       return sum(i.weight() for i in self.cargoHold)

    def __str__(self):
        if(len(self.cargoHold) == 1):
            return f"{len(self.cargoHold)} suitcase, space for {self.max_weight - self.__cargoHold_current_weight()} kg"
        return f"{len(self.cargoHold)} suitcases, space for {self.max_weight - self.__cargoHold_current_weight()} kg"
    
    def print_items(self):
        for i in self.cargoHold:
            i.print_items()
