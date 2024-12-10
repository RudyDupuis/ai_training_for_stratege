from game_logic.enums.orientation import Orientation
from game_logic.enums.action import Action
from game_logic.mappers.pawn_id_to_number import pawn_to_id_to_number


def action_to_action_matrice(action, pawn, position, orientation):
    return [
        pawn_to_id_to_number(pawn)["player"] if pawn else 0,
        pawn_to_id_to_number(pawn)["number"] if pawn else 0,
        1 if Action.MOVE == action else 0,
        1 if Action.KILL == action else 0,
        1 if Action.PUSH == action else 0,
        1 if Action.PULL == action else 0,
        1 if Action.ROTATE == action else 0,
        1 if "pass_turn" == action else 0,
        position.row if position else 0,
        position.col if position else 0,
        1 if orientation == Orientation.NE else 0,
        1 if orientation == Orientation.NW else 0,
        1 if orientation == Orientation.SE else 0,
        1 if orientation == Orientation.SW else 0,
    ]
