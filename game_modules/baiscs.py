import json
import random

from game_modules.story_decoder import read_world_json


class Entity:
    """
    Represents the base stats and functionalities for all entities in the game.

    Attributes:
    - is_alive (bool): Indicates if the entity is alive.

    Methods:
    - get_health(): Abstract method to retrieve the health of the entity.
    - handle_death(): Abstract method to handle the death of the entity.
    - perform_attack(): Abstract method to perform an attack.
    - perform_defence(): Abstract method to perform a defense.
    - handle_abilities(): Abstract method to handle entity abilities.
    """
    is_alive = True
    
    def __init__(self):
        pass
    
    def get_health(self):
        pass
    
    def handle_death(self):
        pass
    
    def perform_attack(self):
        pass
    
    def perform_defence(self):
        pass
    
    def handle_abilities(self):
        pass


class Goblin(Entity):
    """
    Represents the Goblin entity.

    Attributes:
    - health (int): Health of the Goblin.
    - attack (int): Attack power of the Goblin.
    - defence (int): Defence power of the Goblin.
    - abilities (list): List of abilities of the Goblin.

    Methods:
    - get_health(): Retrieves the health of the Goblin.
    - handle_death(): Handles the death of the Goblin.
    - perform_attack(): Performs an attack.
    - perform_defence(): Performs a defense.
    - handle_abilities(): Handles the abilities of the Goblin.
    """
    health = 100
    attack = 10
    defence = 5
    abilities = ["Bite", "Scratch"]
    
    def __init__(self):
        pass
    
    def dodge(self):
        
        return "Goblin dodged the attack"
    
    def get_health(self):
        return self.health
    
    def handle_death(self):
        self.is_alive = False
        return "Goblin is dead"
    
    def perform_attack(self):
        print("Goblin attacked")
        return self.attack
    
    def perform_defence(self):
        print("Goblin defended")
        return self.defence
    
    def handle_abilities(self):
        
        return self.abilities

class WnRJson:
    """
    Reads JSON file and provides methods to retrieve and update stats.

    Parameters:
    - json_path (str): Path to the JSON file.

    Attributes:
    - json_data (dict): Parsed JSON data.

    Methods:
    - get_stats(): Retrieves stats from the JSON data.
    - set_stats(update): Updates stats based on the provided dictionary.
    """
    def __init__(self, json_path):
        with open(json_path, 'r') as json_file:
            self.json_data = json.load(json_file)

    def get_stats(self):
        health = self.json_data[1]['hp']
        attack = 11
        defence = self.json_data[1]['def']
        abilities = self.json_data[1]['skill']
        
        return {"health": health, "attack": attack, "defence": defence, "abilities": abilities}
    
    def set_stats(self, update):
        for key, value in update.items():
            if value != 0:
                pass
            

def read_player_and_enemy():
    player = read_world_json("story/stats.json")
    enemy = read_world_json("story/enemies.json")
    return player, enemy

def calculate_damage(player, enemy, damage_type):
    if random.randint(1, 10) >= 5:
        sum = player[0]["weapon"][damage_type] + player[0]["speed"] + player[0]["level"] / 4 + player[0]["Str"] / player[0]["weight"]
        if random.randint(1, player[0]["critical_hit"]) > (enemy[0]["luck"] + enemy[0]["level"] / 60):
            print("Critical Hit")
            sum += player[0]["critical_hit"]
        player[0]["health"] -= sum
        return player[0]["health"]
    else:
        return "missed" if damage_type == "Attack Power" else "Too slow"

def escape(player, enemy):
    return player[0]["level"] > enemy[0]["level"] or player[0]["luck"] > random.randrange(1, random.randint(9))

def weapon_switch(player, user_pick):
    if user_pick in player[0]["Item Slot"]:
        player[0]["Current Weapon"] = user_pick
    else:
        print("looks like luck's not on your side")

def CombatMechanic(attacker, receiver):
    player, enemy = read_player_and_enemy()
    attack_damage = calculate_damage(player, enemy, "Attack Power")
    defence_damage = calculate_damage(player, enemy, "Defence")
    can_escape = escape(player, enemy)
    weapon_switch(player, "Sword")  