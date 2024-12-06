from game_logic.classes.PawnPosition import PawnPosition
from game_logic.enums.Action import Action, ReceivedAction
from game_logic.actions.calculate_pawn_remaining_moves import (
    calculate_pawn_remaining_moves,
)


def kill_pawn(game_state, player, pawn, desired_pawn_position_for_kill):
    try:
        if not game_state.determinePlayerBasedOnTurn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    positions_available_for_killing = game_state.determineAvailablePositionsForActions(
        pawn, player
    ).positionsAvailableForKilling

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

    pawn_to_kill = game_state.findPawnByPosition(desired_pawn_position_for_kill)

    if pawn_to_kill is None:
        raise Exception("Le pion à prendre n'existe pas")

    if pawn_to_kill.owner == player:
        raise Exception("Le pion à prendre appartient au même joueur")

    calculate_pawn_remaining_moves(pawn, desired_pawn_position_for_kill)

    pawn_to_kill.isAlive = False
    pawn_to_kill.lastPosition = PawnPosition(
        pawn_to_kill.position.row, pawn_to_kill.position.col
    )
    pawn_to_kill.position = PawnPosition(-1, -1)
    pawn_to_kill.lastAction = ReceivedAction.IsKilled

    pawn.lastPosition = PawnPosition(pawn.position.row, pawn.position.col)
    pawn.position = desired_pawn_position_for_kill
    pawn.lastAction = Action.Kill

    game_state.updatePawn(pawn_to_kill)
    game_state.updatePawn(pawn)

    game_state.checkIfThereIsAWinner()
    game_state.updateBoard()
