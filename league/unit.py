import pygame
from pygame.locals import K_w, K_a, K_s, K_d

from .team import Team
from .ability import Ability
from .stats import Stats

from typing import Sequence


class Unit:
    def __init__(self, base_health: int, base_damage: int, base_armor: int, base_range: int, base_speed: int, team: Team, enemy_team: Team, rect: pygame.Rect) -> None:
        self._base_stats = Stats(base_health, base_damage, base_armor, base_range, base_speed)
        self._level = 1
        self._team = team
        self._enemy_team = enemy_team
        self._rect = rect

    def apply_debuff(self, debuff: Ability):
        "Take an Ability object and stores the debuff"
        pass

    def implement_debuffs(self):
        "Applies the debuffs onto the unit"
        pass

    def update(self, screen: pygame.Surface, keys_pressed: Sequence[bool]=None):
        "Updates the player's damage, movement, armor, health, etc..."

        if keys_pressed:

            # CURRENT SYSTEM: CHANGE WITH MASKING
            color_top_left = screen.get_at((self._rect.x - 1, self._rect.y))
            color_top_right = screen.get_at((self._rect.x + self._rect.width + 1, self._rect.y))
            color_bot_left = screen.get_at((self._rect.x, self._rect.y + self._rect.height + 1))
            color_bot_right = screen.get_at((self._rect.x + self._rect.width + 1, self._rect.y + self._rect.height + 1))

            colors = [color_top_left, color_top_right, color_bot_left, color_bot_right]

            if keys_pressed[K_d]:
                # color = screen.get_at((self._rect.x + self._rect.width + 1, self._rect.y))
                if colors[1] == ((255,255,255,255)) and colors[3] == ((255,255,255,255)):
                    self._rect.x += self._base_stats.speed
            
            if keys_pressed[K_a]:
                # color = screen.get_at((self._rect.x - 1, self._rect.y))
                if colors[0] == ((255,255,255,255)) and colors[2] == ((255,255,255,255)):
                    self._rect.x -= self._base_stats.speed

            if keys_pressed[K_s]:
                # color = screen.get_at((self._rect.x, self._rect.y + self._rect.height + 1))
                if colors[2] == ((255,255,255,255)) and colors[3] == ((255,255,255,255)):
                    self._rect.y += self._base_stats.speed

            if keys_pressed[K_w]:
                # color = screen.get_at((self._rect.x, self._rect.y - 1))
                if colors[0] == ((255,255,255,255)) and colors[1] == ((255,255,255,255)):
                    self._rect.y -= self._base_stats.speed

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

    def get_rect(self) -> pygame.Rect:
        return self._rect


class Hero(Unit):
    pass
