from game_logic.enums.Action import Action


def rotate_pawn(game_state, player, pawn, orientation):
    try:
        if not game_state.determinePlayerBasedOnTurn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    pawn.orientation = orientation
    pawn.lastAction = Action.Rotate

    game_state.updatePawn(pawn)
    game_state.updateBoard()
