from game_logic.classes.pawn_position import PawnPosition
from game_logic.enums.action import Action, ReceivedAction
from game_logic.actions.calculate_pawn_remaining_moves import (
    calculate_pawn_remaining_moves,
)


def kill_pawn(game_state, player, pawn, desired_pawn_position_for_kill):
    try:
        if not game_state.determine_player_based_on_turn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    positions_available_for_killing = (
        game_state.determine_available_positions_for_actions(
            pawn, player
        ).positions_available_for_killing
    )

    try:
        if not any(
            pos.row == desired_pawn_position_for_kill.row
            and pos.col == desired_pawn_position_for_kill.col
            for pos in positions_available_for_killing
        ):
            raise Exception(
                f"La position {desired_pawn_position_for_kill.row}, {desired_pawn_position_for_kill.col} n'est pas valide."
            )
    except Exception as error:
        raise Exception(str(error))

    pawn_to_kill = game_state.find_pawn_by_position(desired_pawn_position_for_kill)

    if pawn_to_kill is None:
        raise Exception("Le pion à prendre n'existe pas")

    if pawn_to_kill.owner == player:
        raise Exception("Le pion à prendre appartient au même joueur")

    calculate_pawn_remaining_moves(pawn, desired_pawn_position_for_kill)

    pawn_to_kill.is_alive = False
    pawn_to_kill.last_position = PawnPosition(
        pawn_to_kill.position.row, pawn_to_kill.position.col
    )
    pawn_to_kill.position = PawnPosition(-1, -1)
    pawn_to_kill.last_action = ReceivedAction.IS_KILLED

    pawn.last_position = PawnPosition(pawn.position.row, pawn.position.col)
    pawn.position = desired_pawn_position_for_kill
    pawn.last_action = Action.KILL

    game_state.update_pawn(pawn_to_kill)
    game_state.update_pawn(pawn)

    game_state.check_if_there_is_a_winner()
    game_state.update_board()
