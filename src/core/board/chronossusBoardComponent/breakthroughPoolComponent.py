from src.core.base.type import BreakthroughType
from src.core.interface.IEnumPoolComponent import IEnumPoolComponent
from src.core.interface.IRewardedComponent import IRewardedComponent
from src.core.util.exception import ActionFailedException


class BreakthroughEnumPoolComponent(IEnumPoolComponent, IRewardedComponent):
    """
    Breakthrough pool component for chronossus board
    """

    def get(self) -> dict[BreakthroughType, int]:
        """
        Get pool from component
        :return: dict of breakthrough and their number
        """
        return self._pool

    def add(self, breakthrough: BreakthroughType):
        """
        Add breakthrough to pool
        :param breakthrough: a breakthrough to add
        """
        super().add(breakthrough)

    def __init__(self):
        super().__init__(BreakthroughType)

    def remove_any(self) -> None:
        """
        Remove breakthrough of any shape or icon; if it has multiples, it discards one of whichever it has the most of
        """
        if all(b == 0 for b in self._pool.values()):
            raise ActionFailedException("There is no breakthroughs.")
        breakthrough_type = max(self._pool, key=self._pool.get)
        self._pool[breakthrough_type] -= 1

    def get_victory_points(self) -> int:
        """
        Calculate: 1 VP per Breakthrough, plus 2 additional VPs for each complete shape set.
        :return: Victory points value from breakthrough pool
        """
        # 1 VP per Breakthrough
        points = sum(self._pool.values())
        # 2 VPs for each complete shape set
        points += min(self._pool.values()) * 2
        return points
