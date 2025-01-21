# WRITE YOUR SOLUTION HERE:

class Car:

    def __init__(self):
        
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, km : int):
        if(km >= self.__petrol):
            self.__odometer += self.__petrol
            self.__petrol = 0
        
        elif(km < self.__petrol):
            self.__petrol -= km
            self.__odometer += km

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remainig {self.__petrol} litres"
