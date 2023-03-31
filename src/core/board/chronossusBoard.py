from src.core.board.chronossusBoardComponent.WorkerPoolComponent import WorkerPoolComponent
from src.core.board.chronossusBoardComponent.breakthroughPoolComponent import BreakthroughPoolComponent
from src.core.board.chronossusBoardComponent.buildingsPoolComponent import BuildingPoolComponent
from src.core.board.chronossusBoardComponent.exosuitPoolComponent import ExosuitPoolComponent
from src.core.board.chronossusBoardComponent.paradoxTrackComponent import ParadoxTrackComponent
from src.core.board.chronossusBoardComponent.timeTravelTrackComponent import TimeTravelTrackComponent


class ChronossusBoard:
    _actions = None
    _resources_pool = None
    _workers_pool: WorkerPoolComponent
    _exosuits_pool: ExosuitPoolComponent
    _paradox_track: ParadoxTrackComponent
    _time_travel_track: TimeTravelTrackComponent
    _breakthroughs_pool: BreakthroughPoolComponent
    _buildings_pool: BuildingPoolComponent

    def __init__(self):
        self._buildings_pool = BuildingPoolComponent()
        self._breakthroughs_pool = BreakthroughPoolComponent()
        self._time_travel_track = TimeTravelTrackComponent()
        self._paradox_track = ParadoxTrackComponent()
        self._exosuits_pool = ExosuitPoolComponent()
