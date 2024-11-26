# Write your solution here

def who_won(game_board : list):
    player_1 = 0
    player_2 = 0
    for i in game_board:
        for j in i:
            if(j == 1):
                player_1 += 1
            elif(j == 2):
                player_2 += 1
    if(player_1 == player_2):
        return 0
    elif(player_2 > player_1):
        return 2
    return 1
