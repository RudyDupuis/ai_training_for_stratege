from game_logic.enums.orientation import Orientation
from game_logic.enums.action import Action
from game_logic.classes.pawn_position import PawnPosition


def action_matrice_to_action_infos(matrice, game_state):
    pawn_id = (
        "p" + str(matrice[0]) + "-" + str(matrice[1])
        if matrice[0] != 0 and matrice[1] != 0
        else None
    )

    pawn = None
    for p in game_state.board_pawns:
        if p.id == pawn_id:
            pawn = p
            break

    action = None
    if matrice[2] == 1:
        action = Action.MOVE
    if matrice[3] == 1:
        action = Action.KILL
    if matrice[4] == 1:
        action = Action.PUSH
    if matrice[5] == 1:
        action = Action.PULL
    if matrice[6] == 1:
        action = Action.ROTATE
    if matrice[7] == 1:
        action = "pass_turn"

    position = None
    if action in (Action.MOVE, Action.KILL, Action.PUSH, Action.PULL):
        position = PawnPosition(matrice[8], matrice[9])

    orientation = None
    if action == Action.ROTATE:
        if matrice[10] == 1:
            orientation = Orientation.NE
        if matrice[11] == 1:
            orientation = Orientation.NW
        if matrice[12] == 1:
            orientation = Orientation.SE
        if matrice[13] == 1:
            orientation = Orientation.SW

    return {
        "pawn": pawn,
        "action": action,
        "position": position,
        "orientation": orientation,
    }
