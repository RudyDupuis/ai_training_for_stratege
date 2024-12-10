from game_logic.enums.orientation import Orientation
from game_logic.enums.action import Action
from game_logic.mappers.pawn_id_to_number import pawn_to_id_to_number
from game_logic.mappers.action_to_action_matrice import action_to_action_matrice


def board_infos_data_to_state_matrice(game_state):
    pawns_positions_on_board_matrice = []
    for row in game_state.board:
        for cell in row:
            if cell is None:
                pawns_positions_on_board_matrice.append(0)
                pawns_positions_on_board_matrice.append(0)
            else:
                pawns_positions_on_board_matrice.append(
                    pawn_to_id_to_number(cell)["player"]
                )
                pawns_positions_on_board_matrice.append(
                    pawn_to_id_to_number(cell)["number"]
                )

    pawns_infos_matrice = []
    for pawn in game_state.board_pawns:
        pawns_infos_matrice.append(pawn_to_id_to_number(pawn)["player"])
        pawns_infos_matrice.append(pawn_to_id_to_number(pawn)["number"])
        pawns_infos_matrice.append(1 if pawn.is_alive else 0)
        pawns_infos_matrice.append(pawn.remaining_move)
        pawns_infos_matrice.append(1 if pawn.orientation == Orientation.NE else 0)
        pawns_infos_matrice.append(1 if pawn.orientation == Orientation.NW else 0)
        pawns_infos_matrice.append(1 if pawn.orientation == Orientation.SE else 0)
        pawns_infos_matrice.append(1 if pawn.orientation == Orientation.SW else 0)

    return pawns_positions_on_board_matrice + pawns_infos_matrice


def actions_to_actions_matrice(game_state, player):
    actions_matrice = []
    player_pawns = [
        pawn
        for pawn in game_state.board_pawns
        if pawn.owner == player and pawn.is_alive
    ]

    for pawn in player_pawns:
        available_positions_for_actions = (
            game_state.determine_available_positions_for_actions(pawn, player)
        )

        for (
            move_position
        ) in available_positions_for_actions.positions_available_for_moving:
            actions_matrice.append(
                action_to_action_matrice(Action.MOVE, pawn, move_position, None)
            )

        for (
            kill_position
        ) in available_positions_for_actions.positions_available_for_killing:
            actions_matrice.append(
                action_to_action_matrice(Action.KILL, pawn, kill_position, None)
            )

        for (
            push_position
        ) in available_positions_for_actions.positions_available_for_pushing:
            actions_matrice.append(
                action_to_action_matrice(Action.PUSH, pawn, push_position, None)
            )

        for (
            pull_position
        ) in available_positions_for_actions.positions_available_for_pulling:
            actions_matrice.append(
                action_to_action_matrice(Action.PULL, pawn, pull_position, None)
            )

        if pawn.last_action != Action.ROTATE:
            for orientation in Orientation:
                if orientation != pawn.orientation:
                    actions_matrice.append(
                        action_to_action_matrice(Action.ROTATE, pawn, None, orientation)
                    )

    actions_matrice.append(action_to_action_matrice("pass_turn", None, None, None))

    return actions_matrice
