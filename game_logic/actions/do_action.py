from game_logic.enums.action import Action
from game_logic.mappers.action_matrice_to_action_infos import (
    action_matrice_to_action_infos,
)
from game_logic.actions.move_pawn import move_pawn
from game_logic.actions.kill_pawn import kill_pawn
from game_logic.actions.push_pawn import push_pawn
from game_logic.actions.pull_pawn import pull_pawn
from game_logic.actions.rotate_pawn import rotate_pawn
from game_logic.actions.pass_turn import pass_turn


def do_action(matrice, game_state, player):
    action_info = action_matrice_to_action_infos(matrice, game_state)

    print("***************")
    print(action_info["pawn"].id if action_info["pawn"] is not None else None)
    print(action_info["action"])
    print(action_info["position"].col if action_info["position"] is not None else None)
    print(action_info["position"].row if action_info["position"] is not None else None)
    print(action_info["orientation"])
    print("***************")

    if action_info["action"] == Action.MOVE:
        move_pawn(game_state, player, action_info["pawn"], action_info["position"])
    if action_info["action"] == Action.KILL:
        kill_pawn(game_state, player, action_info["pawn"], action_info["position"])
    if action_info["action"] == Action.PUSH:
        push_pawn(game_state, player, action_info["pawn"], action_info["position"])
    if action_info["action"] == Action.PULL:
        pull_pawn(game_state, player, action_info["pawn"], action_info["position"])
    if action_info["action"] == Action.ROTATE:
        rotate_pawn(game_state, player, action_info["pawn"], action_info["orientation"])
    if action_info["action"] == "pass_turn":
        pass_turn(game_state, player)
