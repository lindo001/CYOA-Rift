import json
import time

from game_modules.baiscs import WnRJson
from game_modules.player_modifier import get_player_stats


def Infamy_detect()->bool:
    #load player data
    with open("story/stats.json", 'r') as json_file:
        player = json.load(json_file)
    infamy = player[0]["Infamy"]
    # print(infamy)
    if infamy > 0:
        print("You are infamouse")
        return True
    return False

def Modify_infamy(action:bool):
    with open("story/stats.json", 'r') as json_file:
        player = json.load(json_file)
    infamy = player[0]["Infamy"]
    if action:
        infamy += 1
    else: infamy -= 1
    
    player[0]["Infamy"] = infamy
    with open("story/stats.json", 'w') as json_file:
        json.dump(player, json_file, indent=4)
    return True

def wanted():
    is_wanted = Infamy_detect()
    
    if is_wanted:
        print("You are wanted")
        time.sleep(2)
        print("You are being hunted")
        player_chose = input("Press any key R to run or S to surrender: ")
        if player_chose == "R":
            print("You ran")
            Modify_infamy(True)
            
        elif player_chose == "S":
            print("You surrendered")
            Modify_infamy(False)
 
        if is_wanted == True:
            wanted()
        
            


def play_game():
    #load player data
    player = WnRJson("story/stats.json")
    
    print(player.get_stats())
    
    pass




# if __name__ == "__main__":
    # play_game()
    # Infamy_detect()
    # wanted()
    # player = get_player_stats()
    # print(player)