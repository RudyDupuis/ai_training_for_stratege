from dataclasses import dataclass, field
from game_logic.classes.pawn_position import PawnPosition
from game_logic.game_state_methods.determine_available_positions_for_actions.determine_available_positions_for_moving_or_killing_by_moving_one_cell_at_a_time import (
    determine_available_positions_for_moving_or_killing_by_moving_one_cell_at_a_time,
)
from game_logic.game_state_methods.determine_available_positions_for_actions.determine_available_positions_for_pushing_or_pulling import (
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


@dataclass
class PositionsAvailableForActions:
    positions_available_for_moving: list = field(default_factory=list)
    positions_available_for_killing: list = field(default_factory=list)
    positions_available_for_pushing: list = field(default_factory=list)
    positions_available_for_pulling: list = field(default_factory=list)


def determine_available_positions_for_actions(game_state, pawn, player):
    positions_available_for_moving = []
    positions_available_for_killing = []
    positions_available_for_pushing = []
    positions_available_for_pulling = []

    determine_available_positions_for_moving_or_killing_by_moving_one_cell_at_a_time(
        game_state,
        pawn.position,
        pawn.remaining_move,
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
    result.positions_available_for_moving = positions_available_for_moving
    result.positions_available_for_killing = positions_available_for_killing
    result.positions_available_for_pushing = positions_available_for_pushing
    result.positions_available_for_pulling = positions_available_for_pulling

    return result
