from typing import List, Tuple
from unit import Hero, Tower, Nexus, Minion


class Team:
    def __init__(self, heroes: List[Hero], nexus_point: Tuple[int, int], tower_points: List[Tuple[int, int]]) -> None:
        self.heroes = heroes
        self.nexus = None
        # self._towers = None
        # self.minions = None
        # self._minions: List[Minion] = []
        # self._towers : List[Tower] = []
    def get_towers(self) -> List[Tower]:
        return self.towers
    
    def get_nexus(self) -> Nexus:
       return self.nexus
    
    def get_all(self): #Concatonate lists
        all = self._towers + self.heroes + self.nexus
        return all
    
    def _spawn_towers(tower_points :List[Tuple[int, int]]):
        pass

    def _spawn_minions()-> None:
        pass

    @staticmethod
    def create_blue_team(heroes: List[Hero]) -> "Team":
        pass
    
    @staticmethod
    def create_red_team(heroes: List[Hero]) -> "Team":
        pass


