from league.stats import Stats
from league.unit import Unit

def test_stat_getters():
    unit1 = Unit(10, 5 ,14, 19, 35, 'Red', 'Blue')
    """
    health
    damage
    armor
    range
    speed
    """

    assert unit1.get_damage() == 5
    assert unit1.get_health() == 10
    assert unit1.get_armor() == 14
    assert unit1.get_range() == 19
    assert unit1.get_speed() == 35

def test_update_stats():
    unit1 = Unit(10, 5 ,14, 19, 35, 'Red', 'Blue')
    unit1._update_stats(Stats(health = 300, armor = 45, speed = 5))
    assert unit1.get_health() == 310
    assert unit1.get_armor() == 59
    assert unit1.get_speed() == 40
    assert unit1._current_stats.speed == 40