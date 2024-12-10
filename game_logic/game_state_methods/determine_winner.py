from game_logic.enums.player_role import PlayerRole


def determine_winner(player1s_lost_pawns, player2s_lost_pawns):
    from game_logic.classes.game_state import GameState

    if len(player1s_lost_pawns) == GameState.MAX_PAWNS_PER_PLAYER:
        return PlayerRole.PLAYER2
    if len(player2s_lost_pawns) == GameState.MAX_PAWNS_PER_PLAYER:
        return PlayerRole.PLAYER1
    return None
