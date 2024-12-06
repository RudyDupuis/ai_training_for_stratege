from game_logic.enums.PlayerRole import PlayerRole


def determine_players_lost_pawns(board_pawns):
    player1s_lost_pawns = [
        pawn
        for pawn in board_pawns
        if pawn.owner == PlayerRole.Player1 and not pawn.isAlive
    ]
    player2s_lost_pawns = [
        pawn
        for pawn in board_pawns
        if pawn.owner == PlayerRole.Player2 and not pawn.isAlive
    ]

    return {
        "player1s_lost_pawns": player1s_lost_pawns,
        "player2s_lost_pawns": player2s_lost_pawns,
    }
