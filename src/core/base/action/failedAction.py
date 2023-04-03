from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction


class FailedAction(IAction):
    def execute(self) -> None:
        self._board.victory_points_pool.add(1)

    _board: ChronossusBoard

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board