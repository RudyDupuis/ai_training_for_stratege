from game_logic.enums.player_role import PlayerRole


def pawn_to_id_to_number(pawn):
    return {
        "player": 1 if pawn.owner == PlayerRole.PLAYER1 else 2,
        "number": int(pawn.id.split("-")[1]),
    }
