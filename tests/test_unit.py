<<<<<<< HEAD
import pygame

from league.unit import Unit
from league.team import Team
from league.stats import Stats

"""
base_health: int
base_damage: int
base_armor: int
base_range: int
base_speed: int
team: Team
enemy_team: Team
rect: pygame.Rect
"""

"""
        Unit
--------------------
- base_stats: Stats
- level: int
- team: Team
- enemy_team: Team
- rect: pygame.Rect
"""

t1 = Team()
t2 = Team()
r1 = pygame.Rect(100, 100, 30, 30)
r2 = pygame.Rect(500, 500, 10, 15)


def test_can_create_unit(): 
    team = Team()
    enemy_team = Team()
    stats = Stats()

    unit = Unit(stats, team, enemy_team)
    assert unit.get_stats() is stats
    assert unit.get_team() is team
    assert unit.get_enemy_team() is enemy_team


def test_unit_attributes():
    u = Unit(
        500,
        50,
        10,
        150,
        10,
        t1,
        t2,
        r1
    )

    assert u._base_stats.health == 500
    assert u._base_stats.damage == 50
    assert u._base_stats.armor == 10
    assert u._base_stats.range == 150
    assert u._base_stats.speed == 10
    assert u._level == 1
    assert u._team == t1
    assert u._enemy_team == t2
    assert u._rect == r1


def test_get_health():
    u1 = Unit(500, 0, 0, 0, 0, t1, t2, r1)
    assert u1.get_health() == 500

    u2 = Unit(1000, 0, 0, 0, 0, t1, t2, r1)
    assert u2.get_health() == 1000


def test_get_damage():
    u1 = Unit(0, 100, 0, 0, 0, t1, t2, r1)
    assert u1.get_damage() == 100

    u2 = Unit(0, 50, 0, 0, 0, t1, t2, r1)
    assert u2.get_damage() == 50


def test_get_armor():
    u1 = Unit(0, 0, 10, 0, 0, t1, t2, r1)
    assert u1.get_armor() == 10

    u2 = Unit(0, 0, 30, 0, 0, t1, t2, r1)
    assert u2.get_armor() == 30


def test_get_range():
    u1 = Unit(0, 0, 0, 100, 0, t1, t2, r1)
    assert u1.get_range() == 100

    u2 = Unit(0, 0, 0, 500, 0, t1, t2, r1)
    assert u2.get_range() == 500


def test_get_speed():
    u1 = Unit(0, 0, 0, 0, 10, t1, t2, r1)
    assert u1.get_speed() == 10

    u2 = Unit(0, 0, 0, 0, 30, t1, t2, r1)
    assert u2.get_speed() == 30


def test_get_level():
    u1 = Unit(0, 0, 0, 0, 0, t1, t2, r1)
    assert u1.get_level() == 1


def get_rect():
    u1 = Unit(0, 0, 0, 0, 0, t1, t2, r1)
    assert u1.get_rect() == r1
    assert u1.get_rect().left == 100
    assert u1.get_rect().top == 100
    assert u1.get_rect().width == 30
    assert u1.get_rect().height == 30

    u2 = Unit(0, 0, 0, 0, 0, t1, t2, r2)
    assert u2.get_rect() == r2
    assert u2.get_rect().left == 500
    assert u2.get_rect().top == 500
    assert u2.get_rect().width == 10
    assert u2.get_rect().height == 15
