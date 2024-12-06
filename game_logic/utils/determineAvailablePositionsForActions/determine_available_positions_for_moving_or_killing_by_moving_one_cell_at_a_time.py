from game_logic.classes.PawnPosition import PawnPosition
from game_logic.enums.Orientation import Orientation
from game_logic.utils.determineAvailablePositionsForActions.pawn_can_kill_other_pawn import (
    pawn_can_kill_other_pawn,
)


def determine_available_positions_for_moving_or_killing_by_moving_one_cell_at_a_time(
    game_state,
    current_position,
    remaining_move,
    player,
    positions_available_for_moving,
    positions_available_for_killing,
):
    from game_logic.classes.GameState import GameState
    from game_logic.utils.determineAvailablePositionsForActions.determine_available_positions_for_actions import (
        PAWN_POSITION_DIRECTIONS,
        PAWN_POSITION_TOP,
        PAWN_POSITION_BOTTOM,
        PAWN_POSITION_LEFT,
        PAWN_POSITION_RIGHT,
    )

    if remaining_move == 0:
        return

    for direction in PAWN_POSITION_DIRECTIONS:
        new_row = current_position.row + direction.row
        new_col = current_position.col + direction.col
        new_position = PawnPosition(new_row, new_col)

        if GameState.isInBoardGameBounds(game_state.board, new_row, new_col):
            if GameState.isCellOccupied(game_state.board, new_row, new_col):
                other_pawn = game_state.findPawnByPosition(new_position)

                if other_pawn.owner != player:
                    if direction == PAWN_POSITION_TOP:
                        pawn_can_kill_other_pawn(
                            other_pawn,
                            Orientation.NW,
                            Orientation.NE,
                            positions_available_for_killing,
                            new_position,
                        )
                    elif direction == PAWN_POSITION_BOTTOM:
                        pawn_can_kill_other_pawn(
                            other_pawn,
                            Orientation.SW,
                            Orientation.SE,
                            positions_available_for_killing,
                            new_position,
                        )
                    elif direction == PAWN_POSITION_LEFT:
                        pawn_can_kill_other_pawn(
                            other_pawn,
                            Orientation.NW,
                            Orientation.SW,
                            positions_available_for_killing,
                            new_position,
                        )
                    elif direction == PAWN_POSITION_RIGHT:
                        pawn_can_kill_other_pawn(
                            other_pawn,
                            Orientation.SE,
                            Orientation.NE,
                            positions_available_for_killing,
                            new_position,
                        )
            else:
                if not any(
                    pos.row == new_row and pos.col == new_col
                    for pos in positions_available_for_moving
                ):
                    positions_available_for_moving.append(new_position)

                determine_available_positions_for_moving_or_killing_by_moving_one_cell_at_a_time(
                    game_state,
                    new_position,
                    remaining_move - 1,
                    player,
                    positions_available_for_moving,
                    positions_available_for_killing,
                )
