from game_logic.enums.action import Action


def rotate_pawn(game_state, player, pawn, orientation):
    try:
        if not game_state.determine_player_based_on_turn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
        if not pawn.owner == player:
            raise Exception("Ce n'est pas le pion du joueur.")
    except Exception as error:
        raise Exception(str(error))

    pawn.orientation = orientation
    pawn.last_action = Action.ROTATE

    game_state.update_pawn(pawn)
    game_state.update_board()
