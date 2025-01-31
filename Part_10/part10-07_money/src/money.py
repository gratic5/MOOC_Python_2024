# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if(self.__cents <= 9):
            return f"{self.__euros}.0{self.__cents} eur"
        return f"{self.__euros}.{self.__cents} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __gt__(self, another):
        return self.__euros*100+self.__cents > another.__euros*100+another.__cents
    
    def __lt__(self,another):
        return self.__euros*100+self.__cents < another.__euros*100+another.__cents
    
    def __ne__(self, another):
        return self.__euros*100+self.__cents != another.__euros*100+another.__cents
    
    def __add__(self, another):
        cents = self.__cents + another.__cents
        euros = self.__euros + another.__euros

        if(cents >= 100):
            return Money(euros + 1,cents - 100)
        return Money(euros, cents)
    
    def __sub__(self, another):
        money1 = self.__euros*100+self.__cents - (another.__euros*100+another.__cents)
        if(money1 < 0):
            raise ValueError
        else:
            return Money(money1//100,money1%100)
        