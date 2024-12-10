from game_logic.classes.pawn_position import PawnPosition
from game_logic.enums.action import Action, ReceivedAction
from game_logic.actions.calculate_pawn_remaining_moves import (
    calculate_pawn_remaining_moves,
)


def pull_pawn(game_state, player, pawn, desired_pawn_position_after_pulling):
    try:
        if not game_state.determine_player_based_on_turn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    positions_available_for_pulling = (
        game_state.determine_available_positions_for_actions(
            pawn, player
        ).positions_available_for_pulling
    )

    try:
        if not any(
            pos.row == desired_pawn_position_after_pulling.row
            and pos.col == desired_pawn_position_after_pulling.col
            for pos in positions_available_for_pulling
        ):
            raise Exception(
                f"La position {desired_pawn_position_after_pulling.row}, {desired_pawn_position_after_pulling.col} n'est pas valide."
            )
    except Exception as error:
        raise Exception(f"Error: {error}")

    pawn_to_pull_position = PawnPosition(
        pawn.position.row + pawn.position.row - desired_pawn_position_after_pulling.row,
        pawn.position.col + pawn.position.col - desired_pawn_position_after_pulling.col,
    )

    pawn_to_pull = game_state.find_pawn_by_position(pawn_to_pull_position)

    if pawn_to_pull is None:
        raise Exception("Le pion à tirer n'existe pas")

    calculate_pawn_remaining_moves(pawn, desired_pawn_position_after_pulling)

    pawn.last_position = PawnPosition(pawn.position.row, pawn.position.col)
    pawn.position = desired_pawn_position_after_pulling
    pawn.last_action = Action.PULL

    pawn_to_pull.last_position = PawnPosition(
        pawn_to_pull.position.row, pawn_to_pull.position.col
    )
    pawn_to_pull.position = pawn.last_position
    pawn_to_pull.last_action = ReceivedAction.IS_PULLED

    game_state.update_pawn(pawn)
    game_state.update_pawn(pawn_to_pull)

    game_state.update_board()
