# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []
        self.count = 0

    def add_number(self, number:int):
        self.numbers.append(number)
        self.count += 1

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        if self.count == 0:
            return 0
        return sum(self.numbers)
    
    def average(self):
        if(self.get_sum() == 0):
            return 0
        return self.get_sum()/self.count




def main():
    print("Please type in integer numbers:")
    n1 = NumberStats()
    n2 = NumberStats()
    n3 = NumberStats()
    while(True):
        input1 = int(input())
        if(input1 == -1):
            break
        n1.add_number(input1)
        if(input1 % 2 == 0):
            n2.add_number(input1)
        else:
            n3.add_number(input1)

    print(f"Numbers added: {n1.count_numbers()}")
    print(f"Sum of numbers: {n1.get_sum()}")
    print(f"Mean of numbers: {n1.average()}")
    print(f"Sum of even numbers: {n2.get_sum()}")
    print(f"Sum of odd numbers: {n3.get_sum()}")



main()