from league.unit import Unit

class Team:
    pass

class Stats:
    pass


def test_can_create_unit(): 
    team = Team()
    enemy_team = Team()
    stats = Stats()

    unit = Unit(stats, team, enemy_team)
    assert unit.get_stats() is stats
    assert unit.get_team() is team
    assert unit.get_enemy_team() is enemy_team


