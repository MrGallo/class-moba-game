import copy
class Stats:
    def __init__(self, 
                 health: int = 0, 
                 damage: int = 0, 
                 armor: int = 0, 
                 range: int = 0, 
                 speed: int = 0):

        self.health = health
        self.damage = damage
        self.armor = armor
        self.range = range
        self.speed = speed
    
    def __add__(self, other):
        return Stats(self.health + other.health, 
                     self.damage + other.damage, 
                     self.armor + other.armor, 
                     self.range + other.range, 
                     self.speed + other.speed)
    
    def __str__(self):
        return f"heath:{self.health} damage:{self.damage} armor:{self.armor} range:{self.range} speed:{self.speed}"
    
    def copy_stats(stats):
        return copy.copy(stats)