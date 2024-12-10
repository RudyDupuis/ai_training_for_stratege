def pass_turn(game_state, player):
    try:
        if not game_state.determine_player_based_on_turn() == player:
            raise Exception("Ce n'est pas le tour du joueur.")
    except Exception as error:
        raise Exception(str(error))

    game_state.turn += 1
    game_state.reset_remaining_moves_pawns()
    game_state.reset_last_action_and_position_pawns()
