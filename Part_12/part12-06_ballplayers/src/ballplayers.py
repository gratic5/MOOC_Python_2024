class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here

def most_goals(players : list):
    return max(players, key=lambda i: i.goals).name

def most_points(players : list):
    a1 =  max(players,key=lambda i: i.passes + i.goals)
    return (a1.name,a1.number)

def least_minutes(players : list):
    return min(players, key=lambda i: i.minutes)

