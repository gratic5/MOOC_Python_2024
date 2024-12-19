# Write your solution here:

class Clock:

    def __init__(self, n1 : int, n2 : int, n3 : int):
        
        self.hours = n1
        self.minutes = n2
        self.seconds = n3

    def set(self,n1=0,n2=0,n3=0):
        self.hours = n1
        self.minutes = n2
        self.seconds = n3

    def tick(self):
        self.seconds += 1

        if(self.seconds == 60):
            self.seconds = 0
            self.minutes += 1

            if(self.minutes == 60):
                self.hours += 1
                self.minutes = 0

                if(self.hours == 24):
                    self.hours = 0


    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    
    


