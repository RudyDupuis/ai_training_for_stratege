def pass_turn(game_state, player):
    try:
        if not game_state.determinePlayerBasedOnTurn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
    except Exception as error:
        raise Exception(str(error))

    game_state.turn += 1
    game_state.resetRemainingMovesPawns()
    game_state.resetLastActionAndPositionPawns()
