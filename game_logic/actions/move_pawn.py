from game_logic.classes.PawnPosition import PawnPosition
from game_logic.enums.Action import Action
from game_logic.actions.calculate_pawn_remaining_moves import (
    calculate_pawn_remaining_moves,
)


def move_pawn(game_state, player, pawn, desired_pawn_position):
    try:
        if not game_state.determinePlayerBasedOnTurn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    positions_available_for_moving = game_state.determineAvailablePositionsForActions(
        pawn, player
    ).positionsAvailableForMoving

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

    pawn.lastPosition = PawnPosition(pawn.position.row, pawn.position.col)
    pawn.position = desired_pawn_position
    pawn.lastAction = Action.Move

    game_state.updatePawn(pawn)
    game_state.updateBoard()
