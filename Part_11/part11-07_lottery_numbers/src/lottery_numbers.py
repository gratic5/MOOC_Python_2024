# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:

    def __init__(self, day : int, number_list : list):
        self.__day = day
        self.__lottery_numbers = number_list

    def number_of_hits(self, numbers : list):
        return len([i for i in numbers if i in self.__lottery_numbers])

    def hits_in_place(self, numbers):
        return [i if i in self.__lottery_numbers else -1 for i in numbers]
    