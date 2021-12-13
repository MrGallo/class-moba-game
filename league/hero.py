from typing import List
from .item import Item
from .stat import Stat


class Hero:
    def __init__(self, gold, items: List[Item]) -> None:
        if gold < 0:
            raise ValueError()
        self._gold = gold
        self._items = items

    
    def get_gold(self) -> int:
        return self._gold


    def get_level(self) -> int:
        return self._level


    def get_buffs(self) -> Stat:
        return self._get_stat_buff
