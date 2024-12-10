from game_logic.game_state_methods.determine_available_positions_for_actions.pawn_can_push_or_pull_other_pawn import (
    pawn_can_push_or_pull_other_pawn,
)


def determine_available_positions_for_pushing_or_pulling(
    game_state, pawn, positions_available_for_pushing, positions_available_for_pulling
):
    from game_logic.classes.game_state import GameState
    from game_logic.game_state_methods.determine_available_positions_for_actions.determine_available_positions_for_actions import (
        PAWN_POSITION_DIRECTIONS,
        PAWN_POSITION_TOP,
        PAWN_POSITION_BOTTOM,
        PAWN_POSITION_LEFT,
        PAWN_POSITION_RIGHT,
    )

    if pawn.remaining_move == 0:
        return

    for direction in PAWN_POSITION_DIRECTIONS:
        new_row = pawn.position.row + direction.row
        new_col = pawn.position.col + direction.col

        if GameState.is_in_board_game_bounds(
            game_state.board, new_row, new_col
        ) and GameState.is_cell_occupied(game_state.board, new_row, new_col):
            if direction == PAWN_POSITION_TOP:
                pawn_can_push_or_pull_other_pawn(
                    game_state, new_row - 1, new_col, positions_available_for_pushing
                )
                pawn_can_push_or_pull_other_pawn(
                    game_state, new_row + 2, new_col, positions_available_for_pulling
                )
            elif direction == PAWN_POSITION_BOTTOM:
                pawn_can_push_or_pull_other_pawn(
                    game_state, new_row + 1, new_col, positions_available_for_pushing
                )
                pawn_can_push_or_pull_other_pawn(
                    game_state, new_row - 2, new_col, positions_available_for_pulling
                )
            elif direction == PAWN_POSITION_LEFT:
                pawn_can_push_or_pull_other_pawn(
                    game_state, new_row, new_col - 1, positions_available_for_pushing
                )
                pawn_can_push_or_pull_other_pawn(
                    game_state, new_row, new_col + 2, positions_available_for_pulling
                )
            elif direction == PAWN_POSITION_RIGHT:
                pawn_can_push_or_pull_other_pawn(
                    game_state, new_row, new_col + 1, positions_available_for_pushing
                )
                pawn_can_push_or_pull_other_pawn(
                    game_state, new_row, new_col - 2, positions_available_for_pulling
                )
