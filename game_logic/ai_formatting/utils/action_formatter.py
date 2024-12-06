from game_logic.enums.Action import Action
from game_logic.enums.Orientation import Orientation
from game_logic.classes.PawnPosition import PawnPosition
from game_logic.ai_formatting.utils.pawn_id_formatter import pawn_id_formatter


def ai_action_formatter(action, pawn, position, orientation):
    return [
        pawn_id_formatter(pawn)[0] if pawn else 0,
        pawn_id_formatter(pawn)[1] if pawn else 0,
        1 if Action.Move == action else 0,
        1 if Action.Kill == action else 0,
        1 if Action.Push == action else 0,
        1 if Action.Pull == action else 0,
        1 if Action.Rotate == action else 0,
        1 if "pass" == action else 0,
        position.row if position else 0,
        position.col if position else 0,
        1 if orientation == Orientation.NE else 0,
        1 if orientation == Orientation.NW else 0,
        1 if orientation == Orientation.SE else 0,
        1 if orientation == Orientation.SW else 0,
    ]


def python_action_formatter(matrice, game_state):
    print("------------------------")
    print(matrice)
    print("------------------------")

    pawn_id = (
        "p" + str(matrice[0]) + "-" + str(matrice[1]) if matrice[0] != 0 and matrice[1] != 0 else None
    )

    pawn = None
    for p in game_state.boardPawns:
        if p.id == pawn_id:
            pawn = p
            break

    action = None
    if matrice[2] == 1:
        action = Action.Move
    elif matrice[3] == 1:
        action = Action.Kill
    elif matrice[4] == 1:
        action = Action.Push
    elif matrice[5] == 1:
        action = Action.Pull
    elif matrice[6] == 1:
        action = Action.Rotate
    elif matrice[7] == 1:
        action = "pass"

    position_obj = None
    if (
        action == Action.Move
        or action == Action.Kill
        or action == Action.Push
        or action == Action.Pull
    ):
        position_obj = PawnPosition(matrice[8], matrice[9])

    orientation = None
    if action == Action.Rotate:
        if matrice[10] == 1:
            orientation = Orientation.NE
        elif matrice[11] == 1:
            orientation = Orientation.NW
        elif matrice[12] == 1:
            orientation = Orientation.SE
        elif matrice[13] == 1:
            orientation = Orientation.SW

    return {
        "action": action,
        "pawn": pawn,
        "position": position_obj,
        "orientation": orientation,
    }
