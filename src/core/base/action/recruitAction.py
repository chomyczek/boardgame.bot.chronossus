from src.core.base.type import WorkerType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.interface.IPriority import IPriority


class RecruitAction(IAction, IPriority):
    _board: ChronossusBoard

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board

    def execute(self, worker_type: WorkerType) -> None:
        self._board.workers_pool.add(worker_type)

    def get_priority(self) -> list[WorkerType]:
        priority = []
        pool = self._board.workers_pool.get()
        i = 0
        for worker in [WorkerType.GENIUS, WorkerType.ADMINISTRATOR, WorkerType.ENGINEER, WorkerType.SCIENTIST]:
            if pool[worker] == 0:
                priority.insert(i, worker)
                i += 1
            else:
                priority.append(worker)
        return priority
