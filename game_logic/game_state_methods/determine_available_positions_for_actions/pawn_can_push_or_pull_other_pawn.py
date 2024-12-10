from game_logic.classes.pawn_position import PawnPosition


def pawn_can_push_or_pull_other_pawn(
    game_state, arrival_position_row, arrival_position_col, positions_available
):
    from game_logic.classes.game_state import GameState

    if GameState.is_in_board_game_bounds(
        game_state.board, arrival_position_row, arrival_position_col
    ) and not GameState.is_cell_occupied(
        game_state.board, arrival_position_row, arrival_position_col
    ):
        positions_available.append(
            PawnPosition(arrival_position_row, arrival_position_col)
        )
