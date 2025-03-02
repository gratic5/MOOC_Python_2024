# Write your solution here
import json

def search_for_player(a1 : list, name : str):
    for i in a1:
        if(i["name"] == name):
            return f"{i["name"]:21}{i["team"]:5}{i["goals"]:>2} + {i["assists"]:>2} = {(i["goals"]+i["assists"]):>3}"

def teams(a1 : list):
    return sorted(list(set(i["team"] for i in a1)))

def countries(a1 : list):
    return sorted(list(set(i["nationality"] for i in a1)))

def players_in_team(a1 : list, team : str):
    return sorted(list(i for i in a1 if i["team"] == team),key=lambda i : i["goals"] + i["assists"],reverse=True)

def players_from_a_country(a1 : list, country : str):
    return sorted(list(filter(lambda i : i["nationality"] == country,a1)),key=lambda i : i["goals"] + i["assists"],reverse=True)

def most_points(a1 : list, n1 : int):
    def sort_by_goals(item : dict):
        return (item["goals"] +item["assists"],item["goals"],item["assists"])
    return list(sorted(a1, key=sort_by_goals,reverse=True))[:n1]
    
def most_goals(a1 : list, n1 : int):
    def sort_by_games(item : dict):
        return (-item["goals"],item["games"])
    return list(sorted(a1,key=sort_by_games))[:n1]
    
def interactive_program():
    n1 = input("file name: ")
    with open(n1) as f:
        data = f.read()
    
    players = json.loads(data)
    print(f"read the data of {len(players)} players")
    while(True):
        print()
        print("""commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals""")
        print()

        n2 = int(input("command: " ))

        if(n2 == 0):
            break
        elif(n2 == 1):
            n3 = input("name: ")
            print()
            print(search_for_player(players,n3))
        elif(n2 == 2):
            n3 = teams(players)
            for i in n3:
                print(i)
        elif(n2 == 3):
            n3 = countries(players)
            for i in n3:
                print(i)
        elif(n2 == 4):
            n3 = input("name: ")
            print()
            n4 = players_in_team(players,n3)
            for i in n4:
                print(f"{i["name"]:21}{i["team"]:5}{i["goals"]:>2} + {i["assists"]:>2} = {(i["goals"]+i["assists"]):>3}")
        elif(n2 == 5):
            n3 = input("country: ")
            print()
            n4 = players_from_a_country(players,n3)
            for i in n4:
                print(f"{i["name"]:21}{i["team"]:5}{i["goals"]:>2} + {i["assists"]:>2} = {(i["goals"]+i["assists"]):>3}")
        elif(n2 == 6):
            n3 = int(input("how many: "))
            i = most_points(players,n3)
            for j in i:
                print(f"{j["name"]:21}{j["team"]:5}{j["goals"]:>2} + {j["assists"]:>2} = {(j["goals"]+j["assists"]):>3}")
        elif(n2 == 7):
            n3 = int(input("how many: "))
            i = most_goals(players,n3)
            for j in i:
                print(f"{j["name"]:21}{j["team"]:5}{j["goals"]:>2} + {j["assists"]:>2} = {(j["goals"]+j["assists"]):>3}")

interactive_program()