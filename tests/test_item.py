from league.item import Item
from league.stats import Stats
import pytest

s1 = Stats(0, 0, 0, 0, 0)
s2 = Stats(10, 5, 2, 0, 2)

def test_item_attributes():
    i1 = Item("hammer", 8, s1)
    assert i1._name == "hammer"
    assert i1._level == 8
    assert i1._stat_buff == s1

    with pytest.raises(ValueError) as excinfo:
        i2 = Item("", -1, s1)
    assert str(excinfo.value) == "Level must be positive."

def test_get_cost():
    i1 = Item("", 1, s1)
    assert i1.get_cost() == 100

    i2 = Item("", 4, s1)
    assert i2.get_cost() == 400

def test_get_name():
    i1 = Item("ring", 1, s1)
    assert i1.get_name() == "ring"

    i2 = Item("amulet", 4, s1)
    assert i2.get_name() == "amulet"

def test_get_level():
    i1 = Item("", 3, s1)
    assert i1.get_level() == 3

    i2 = Item("", 7, s1)
    assert i2.get_level() == 7

def test_get_stat_buff():
    i1 = Item("", 1, s1)
    assert i1.get_stat_buff() == s1

    i2 = Item("", 1, s2)
    assert i2.get_stat_buff() == s2
