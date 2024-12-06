from game_logic.enums.PlayerRole import PlayerRole


def determine_winner(player1s_lost_pawns, player2s_lost_pawns):
    from game_logic.classes.GameState import GameState

    if len(player1s_lost_pawns) == GameState.MAX_PAWNS_PER_PLAYER:
        return PlayerRole.Player2
    if len(player2s_lost_pawns) == GameState.MAX_PAWNS_PER_PLAYER:
        return PlayerRole.Player1
