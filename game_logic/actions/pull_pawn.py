from game_logic.classes.PawnPosition import PawnPosition
from game_logic.enums.Action import Action, ReceivedAction
from game_logic.actions.calculate_pawn_remaining_moves import (
    calculate_pawn_remaining_moves,
)


def pull_pawn(game_state, player, pawn, desired_pawn_position_after_pulling):
    try:
        if not game_state.determinePlayerBasedOnTurn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    positions_available_for_pulling = game_state.determineAvailablePositionsForActions(
        pawn, player
    ).positionsAvailableForPulling

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

    pawn_to_pull = game_state.findPawnByPosition(pawn_to_pull_position)

    if pawn_to_pull is None:
        raise Exception("Le pion à tirer n'existe pas")

    calculate_pawn_remaining_moves(pawn, desired_pawn_position_after_pulling)

    pawn.lastPosition = PawnPosition(pawn.position.row, pawn.position.col)
    pawn.position = desired_pawn_position_after_pulling
    pawn.lastAction = Action.Pull

    pawn_to_pull.lastPosition = PawnPosition(
        pawn_to_pull.position.row, pawn_to_pull.position.col
    )
    pawn_to_pull.position = pawn.lastPosition
    pawn_to_pull.lastAction = ReceivedAction.IsPulled

    game_state.updatePawn(pawn)
    game_state.updatePawn(pawn_to_pull)

    game_state.updateBoard()
