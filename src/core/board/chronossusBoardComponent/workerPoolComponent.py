from src.core.base.type import WorkerType
from src.core.interface.IEnumPoolComponent import IEnumPoolComponent
from src.core.interface.IRewardedComponent import IRewardedComponent


class WorkerEnumPoolComponent(IEnumPoolComponent, IRewardedComponent):
    """
    Worker pool component for chronossus board
    """

    def get(self) -> dict[WorkerType, int]:
        """
        Get pool from component
        :return: dict of worker types and their number
        """
        return self._pool

    def __init__(self):
        super().__init__(WorkerType)

    def add(self, worker: WorkerType) -> None:
        self._score += 1
        super().add(worker)
        super().check_for_completed_set()

    def get_victory_points(self) -> int:
        """
        Sum of points from pool.
        :return: Collected victory points value from.
        """
        return self._score
