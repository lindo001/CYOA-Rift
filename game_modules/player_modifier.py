import json




def get_player_stats():
    with open("story/stats.json", 'r') as json_file:
        player = json.load(json_file)
    name = player[0]["Name"]
    age = player[0]["Age"]
    class_type = player[0]["Class"]
    health = player[0]["Health"]
    level = player[0]["Level"]
    infamy = player[0]["Infamy"]
    
    return {"name": name, "age": age, "class": class_type, "health": health, "level": level, "infamy": infamy}


def modify_health(damage_taken: int) -> None:
    with open("story/stats.json", 'r') as json_file:
        player = json.load(json_file)
    health = player[0]["Health"]
    health -= damage_taken
    player[0]["Health"] = health
    
    if is_player_alive(health):
        with open("story/stats.json", 'w') as json_file:
            json.dump(player, json_file, indent=4)
        return False
    print("You are dead")
    return True


def is_player_alive(player) -> bool:
    health = player
    if health <= 0:
        return True
    return False
