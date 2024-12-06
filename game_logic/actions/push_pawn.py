from game_logic.classes.PawnPosition import PawnPosition
from game_logic.enums.Action import Action, ReceivedAction
from game_logic.actions.calculate_pawn_remaining_moves import (
    calculate_pawn_remaining_moves,
)


def push_pawn(game_state, player, pawn, desired_pushed_pawn_position):
    try:
        if not game_state.determinePlayerBasedOnTurn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    positions_available_for_pushing = game_state.determineAvailablePositionsForActions(
        pawn, player
    ).positionsAvailableForPushing

    try:
        if not any(
            pos.row == desired_pushed_pawn_position.row
            and pos.col == desired_pushed_pawn_position.col
            for pos in positions_available_for_pushing
        ):
            raise Exception(
                f"La position {desired_pushed_pawn_position.row}, {desired_pushed_pawn_position.col} n'est pas valide."
            )
    except Exception as error:
        raise Exception(f"Error: {error}")

    min_col = min(pawn.position.col, desired_pushed_pawn_position.col)
    max_col = max(pawn.position.col, desired_pushed_pawn_position.col)
    min_row = min(pawn.position.row, desired_pushed_pawn_position.row)
    max_row = max(pawn.position.row, desired_pushed_pawn_position.row)

    pawn_to_push_position = None

    if max_col - min_col > 0:
        pawn_to_push_position = PawnPosition(min_row, min_col + 1)
    if max_row - min_row > 0:
        pawn_to_push_position = PawnPosition(min_row + 1, min_col)

    if pawn_to_push_position is None:
        raise Exception("Le pion ne peut pas aller dans cette direction")

    pawn_to_push = game_state.findPawnByPosition(pawn_to_push_position)

    if pawn_to_push is None:
        raise Exception("Le pion à pousser n'existe pas")

    calculate_pawn_remaining_moves(pawn, pawn_to_push_position)

    pawn_to_push.lastPosition = PawnPosition(
        pawn_to_push.position.row, pawn_to_push.position.col
    )
    pawn_to_push.position = desired_pushed_pawn_position
    pawn_to_push.lastAction = ReceivedAction.IsPushed

    pawn.lastPosition = PawnPosition(pawn.position.row, pawn.position.col)
    pawn.position = pawn_to_push.lastPosition
    pawn.lastAction = Action.Push

    game_state.updatePawn(pawn_to_push)
    game_state.updatePawn(pawn)

    game_state.updateBoard()
