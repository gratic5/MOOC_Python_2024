# TEE RATKAISUSI TÄHÄN:
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games
    
class GameMuseum(GameWarehouse):

    def __init__(self):
        super().__init__()

    def list_games(self):
        game_list = super().list_games()
        old_games = []
        for i in game_list:
            if(i.year < 1990):
                old_games.append(i)
        
        return old_games

