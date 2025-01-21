# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed
        
    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# WRITE YOUR SOLUTION HERE:

def fastest_car(cars : list):
    top_speed = cars[0].top_speed
    make = cars[0].make
    for i in cars:
        if i.top_speed > top_speed:
            top_speed = i.top_speed
            make = i.make
    return make
