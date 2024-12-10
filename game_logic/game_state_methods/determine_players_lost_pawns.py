from game_logic.enums.player_role import PlayerRole


def determine_players_lost_pawns(board_pawns):
    player1s_lost_pawns = [
        pawn
        for pawn in board_pawns
        if pawn.owner == PlayerRole.PLAYER1 and not pawn.is_alive
    ]
    player2s_lost_pawns = [
        pawn
        for pawn in board_pawns
        if pawn.owner == PlayerRole.PLAYER2 and not pawn.is_alive
    ]

    return {
        "player1s_lost_pawns": player1s_lost_pawns,
        "player2s_lost_pawns": player2s_lost_pawns,
    }
