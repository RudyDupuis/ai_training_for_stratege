from game_logic.enums.PlayerRole import PlayerRole


def pawn_id_formatter(pawn):
    player = 1 if pawn.owner == PlayerRole.Player1 else 2
    pawn_number = int(pawn.id.split("-")[1])
    return [player, pawn_number]
