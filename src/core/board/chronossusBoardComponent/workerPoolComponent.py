from src.core.Interface.IPoolComponent import IPoolComponent
from src.core.Interface.IRewardedComponent import IRewardedComponent
from src.core.base.type import WorkerType


class WorkerPoolComponent(IPoolComponent, IRewardedComponent):

    def __init__(self):
        super().__init__(WorkerType)

    def add(self, worker: WorkerType):
        self._points += 1
        super().add(worker)

    def get_victory_points(self) -> int:
        """
        Sum of points from pool.
        :return: Collected victory points value from.
        """
        return self._points