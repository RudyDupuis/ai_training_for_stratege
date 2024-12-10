from game_logic.classes.pawn_position import PawnPosition
from game_logic.enums.action import Action
from game_logic.actions.calculate_pawn_remaining_moves import (
    calculate_pawn_remaining_moves,
)


def move_pawn(game_state, player, pawn, desired_pawn_position):
    try:
        if not game_state.determine_player_based_on_turn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    positions_available_for_moving = (
        game_state.determine_available_positions_for_actions(
            pawn, player
        ).positions_available_for_moving
    )

    try:
        if not any(
            pos.row == desired_pawn_position.row
            and pos.col == desired_pawn_position.col
            for pos in positions_available_for_moving
        ):
            raise Exception(
                f"La position {desired_pawn_position.row}, {desired_pawn_position.col} n'est pas valide."
            )
    except Exception as error:
        raise Exception(str(error))

    calculate_pawn_remaining_moves(pawn, desired_pawn_position)

    pawn.last_position = PawnPosition(pawn.position.row, pawn.position.col)
    pawn.position = desired_pawn_position
    pawn.last_action = Action.MOVE

    game_state.update_pawn(pawn)
    game_state.update_board()
