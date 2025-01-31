# WRITE YOUR SOLUTION HERE:

class SimpleDate:

    def __init__(self, date : int, month : int, year : int):

        self.__date = date
        self.__month = month
        self.__year = year

    def __eq__(self, value):
        return self.__date == value.__date and self.__month == value.__month and self.__year == value.__year
    
    def __ne__(self, value):
        return self.__date != value.__date or self.__month != value.__month or self.__year != value.__year
    
    def __gt__(self, value):
        if(self.__year > value.__year):
            return True
        elif(self.__year == value.__year):
            if(self.__month > value.__month):
                return True
            elif(self.__month == value.__month):
                if(self.__date > value.__date):
                    return True
        return False
        
    def __lt__(self,value):
        if(self.__year < value.__year):
            return True
        elif(self.__year == value.__year):
            if(self.__month < value.__month):
                return True
            elif(self.__month == value.__month):
                if(self.__date < value.__date):
                    return True
        return False
        
    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"
    
    
    def __add__(self, value):
        new_value = value
        new_date = self.__date
        new_month = self.__month
        new_year = self.__year

        while(new_value > 0):
            new_date += 1
            new_value -= 1
            if(new_date == 31):
                new_date = 1
                new_month +=1
                if(new_month == 13):
                    new_month = 1
                    new_year += 1

        return SimpleDate(new_date, new_month, new_year)

    def __sub__(self, value):
        count = 0
        if(self > value):
            while(value < self):
                value += 1
                count += 1
        else:
            while(value > self):
                self += 1
                count += 1
        return count




