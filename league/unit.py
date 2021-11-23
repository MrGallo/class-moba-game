import pygame
from team import Team
from ability import Ability
from stats import Stats


class Unit:
    def __init__(self, base_health: int, base_damage: int, base_armor: int, base_range: int, base_speed: int, team: Team, enemy_team: Team) -> None:
        self._base_stats = Stats(base_health, base_damage, base_armor, base_range, base_speed)
        self._level = 1
        self._team = team
        self._enemy_team = enemy_team

    def apply_debuff(self, debuff: Ability):
        "Take an Ability object and stores the debuff"
        pass

    def implement_debuffs(self):
        "Applies the debuffs onto the unit"
        pass

    def update(self):
        "Updates the player's damage, movement, armor, health, etc..."
        pass

    def get_damage(self) -> int:
        "Gets the unit's damage"
        return self._base_stats.damage

    def get_health(self) -> int:
        "Gets the unit's health"
        return self._base_stats.health

    def get_armor(self) -> int:
        "Gets the unit's armor value"
        return self._base_stats.armor

    def get_range(self) -> int:
        "Gets the unit's range"
        return self._base_stats.range

    def get_speed(self) -> int:
        return self._base_stats.speed
    
    def get_level(self) -> int:
        return self._level
