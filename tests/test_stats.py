

from league.stats import Stats

"""
- health
- damage
- armor
- range
- speed
"""

def test_stats_constructor():
    s = Stats(1, 2, 3, 4, 5)
    assert s.health == 1
    assert s.damage == 2
    assert s.armor == 3
    assert s.range == 4
    assert s.speed == 5


def test_stats_addition():
    stats1 = Stats(1, 2, 3, 4, 5)
    stats2 = Stats(1, 2, 3, 4, 5)
    result = stats1 + stats2

    assert result.health == 2
    assert result.damage == 4
    assert result.armor == 6
    assert result.range == 8
    assert result.speed == 10

    assert stats1 is not result
    assert stats2 is not result


def test_stats_addition_does_not_modify_existing():
    stats1 = Stats(1, 2, 3, 4, 5)
    stats2 = Stats(1, 2, 3, 4, 5)
    result = stats1 + stats2

    assert result.health != stats1.health
    assert result.damage != stats1.damage
    assert result.armor != stats1.armor
    assert result.range != stats1.range
    assert result.speed != stats1.speed

    assert result.health != stats2.health
    assert result.damage != stats2.damage
    assert result.armor != stats2.armor
    assert result.range != stats2.range
    assert result.speed != stats2.speed


def test_stats_optional_args():
    s = Stats(health=5)

    assert s.health == 5
    assert s.damage == 0
    assert s.armor == 0
    assert s.range == 0
    assert s.speed == 0


    s = Stats(speed=10, range=6)

    assert s.health == 0
    assert s.damage == 0
    assert s.armor == 0
    assert s.range == 6
    assert s.speed == 10

def test_stats_copy():
    stats1 = Stats(1, 2, 3, 4, 5)
    stats2 = Stats.copy_stats(stats1)
    stats2 += Stats(health = 10)
    assert stats1.health != stats2.health
    assert stats1.health == 1
    assert stats2.health == 11



