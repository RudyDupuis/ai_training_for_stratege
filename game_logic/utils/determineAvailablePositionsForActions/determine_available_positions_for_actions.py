from game_logic.classes.PawnPosition import PawnPosition
from game_logic.utils.determineAvailablePositionsForActions.determine_available_positions_for_moving_or_killing_by_moving_one_cell_at_a_time import (
    determine_available_positions_for_moving_or_killing_by_moving_one_cell_at_a_time,
)
from game_logic.utils.determineAvailablePositionsForActions.determine_available_positions_for_pushing_or_pulling import (
    determine_available_positions_for_pushing_or_pulling,
)

PAWN_POSITION_TOP = PawnPosition(-1, 0)
PAWN_POSITION_BOTTOM = PawnPosition(1, 0)
PAWN_POSITION_LEFT = PawnPosition(0, -1)
PAWN_POSITION_RIGHT = PawnPosition(0, 1)
PAWN_POSITION_DIRECTIONS = [
    PAWN_POSITION_TOP,
    PAWN_POSITION_BOTTOM,
    PAWN_POSITION_LEFT,
    PAWN_POSITION_RIGHT,
]


class PositionsAvailableForActions:
    def __init__(self):
        self.positionsAvailableForMoving = []
        self.positionsAvailableForKilling = []
        self.positionsAvailableForPushing = []
        self.positionsAvailableForPulling = []


def determine_available_positions_for_actions(game_state, pawn, player):
    positions_available_for_moving = []
    positions_available_for_killing = []
    positions_available_for_pushing = []
    positions_available_for_pulling = []

    determine_available_positions_for_moving_or_killing_by_moving_one_cell_at_a_time(
        game_state,
        pawn.position,
        pawn.remainingMove,
        player,
        positions_available_for_moving,
        positions_available_for_killing,
    )

    determine_available_positions_for_pushing_or_pulling(
        game_state,
        pawn,
        positions_available_for_pushing,
        positions_available_for_pulling,
    )

    result = PositionsAvailableForActions()
    result.positionsAvailableForMoving = positions_available_for_moving
    result.positionsAvailableForKilling = positions_available_for_killing
    result.positionsAvailableForPushing = positions_available_for_pushing
    result.positionsAvailableForPulling = positions_available_for_pulling

    return result
