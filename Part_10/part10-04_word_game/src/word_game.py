# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):

    def __init__(self, rounds : int):
        super().__init__(rounds)

    def round_winner(self, player1_word : str, player2_word : str):
        if(len(player1_word) > len(player2_word)):
            return 1
        elif(len(player1_word) < len(player2_word)):
            return 2
        else:
            return 3

class MostVowels(WordGame):

    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        if(self.__vowel_counter(player1_word) > self.__vowel_counter(player2_word)):
            return 1
        elif(self.__vowel_counter(player1_word) < self.__vowel_counter(player2_word)):
            return 2
        else:
            return 3
    
    @staticmethod
    def __vowel_counter(word : str):
        vowels = "aeiou"
        count1 = 0
        for i in word:
            if(i.lower() in vowels):
                count1 += 1

        return count1

class RockPaperScissors(WordGame):
    def __init__(self, rounds : int):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        if(RockPaperScissors.__check(player1_word, player2_word) == 1):
            return 1
        elif(RockPaperScissors.__check(player1_word, player2_word) == 2):
            return 2
        else:
            return 3

    @staticmethod
    def __check(player1_word, player2_word):
        t1 = ("rock","paper","scissors")
        if(player1_word.lower() not in t1 and player2_word.lower() not in t1):
            return 0
        elif(player1_word.lower() not in t1):
            return 2
        elif(player2_word.lower() not in t1):
            return 1
        elif(player1_word.lower() == "paper" and player2_word.lower() == "rock"):
            return 1
        elif(player1_word.lower() == "paper" and player2_word.lower() == "paper"):
            return 0
        elif(player1_word.lower() == "paper" and player2_word.lower() == "scissors"):
            return 2
        elif(player1_word.lower() == "rock" and player2_word.lower() == "rock"):
            return 0
        elif(player1_word.lower() == "rock" and player2_word.lower() == "paper"):
            return 2
        elif(player1_word.lower() == "rock" and player2_word.lower() == "scissors"):
            return 1
        elif(player1_word.lower() == "scissors" and player2_word.lower() == "rock"):
            return 2
        elif(player1_word.lower() == "scissors" and player2_word.lower() == "paper"):
            return 1
        elif(player1_word.lower() == "scissors" and player2_word.lower() == "scissors"):
            return 0

        
    
            
