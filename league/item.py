from .stats import Stats

class Item:
    def __init__(self, name: str, level: int, stat_buff: Stats):
        self._name = name
        if level < 1:
            raise ValueError("Level must be positive.")
        self._level = level
        self._stat_buff = stat_buff

    def get_name(self) -> str:
        return self._name
    
    def get_level(self) -> int:
        return self._level

    def get_cost(self) -> int:
        return self._level * 100

    def get_stat_buff(self) -> Stats:
        return self._stat_buff
