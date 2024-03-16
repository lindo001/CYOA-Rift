
import json
import random



class Entity:
    """
    Represents the base stats and functionalities for all entities in the game.

    Attributes:
    - isAlive (bool): Indicates if the entity is alive.

    Methods:
    - health(): Abstract method to retrieve the health of the entity.
    - death(): Abstract method to handle the death of the entity.
    - attack(): Abstract method to perform an attack.
    - defence(): Abstract method to perform a defense.
    - abilities(): Abstract method to handle entity abilities.
    """
    isAlive = True
    
    def __init__(self) -> None:pass
    
    def health(self):pass
    def death(self):pass
    
    def attack(self):pass
    def defence(self):pass
    def abilities(self): pass


class WnRJson:

    """
    Reads JSON file and provides methods to retrieve and update stats.

    Parameters:
    - Jpath (str): Path to the JSON file.

    Attributes:
    - jsonpath (dict): Parsed JSON data.

    Methods:
    - get_stats(): Retrieves stats from the JSON data.
    - set_stats(update): Updates stats based on the provided dictionary.

    """
    def __init__(self,Jpath) -> None:
        with open(Jpath,'r') as jFile:
            self.jsonpath = json.load(jFile)

    
    def get_stats(self) -> dict:
        self.health = self.jsonpath[1]['hp']
        self.attack = 11
        self.defence = self.jsonpath[1]['def']
        self.abiliy = self.jsonpath[1]['skill']
        
        return {"health":self.health,"attack":self.attack,"defence":self.defence,"abilities":self.abiliy}
        
    
    def set_stats(self,update):
        for i in update:
            if i != 0:
                pass
            

class Combat_Mechanic:
    """
    Implements combat mechanics.

    Methods:
    - combat(attacker, receiver): Simulates combat between attacker and receiver.
    - defence(player, enemy): Calculates enemy's damage received by the player during defense.
    """
    def __init__(self) -> None:
        pass
    
    def combat(self,attacker,receiver):
        if random.randint(1,10)>= 5:
            return attacker - receiver
        else:
            return "missed"
        
    def defence(self,player,enemy):
        return enemy - player
    

    


