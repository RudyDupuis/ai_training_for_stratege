from game_logic.enums.action import Action, ReceivedAction
from game_logic.enums.player_role import PlayerRole
from game_logic.mappers.action_matrice_to_action_infos import (
    action_matrice_to_action_infos,
)
from game_logic.mappers.board_and_actions_data_to_state_matrice_and_actions_matrice import (
    actions_to_actions_matrice,
)

REWARD_FOR_KILL = 40
REWARD_FOR_PUSH = 5
REWARD_FOR_PULL = 5
REWARD_FOR_MOVE = 5
REWARD_FOR_PULL_OPPONENT = 2
REWARD_FOR_PUSH_OPPONENT = 2
PENALTY_FOR_ROTATE = -5
REWARD_FOR_VICTORY = 100
PENALTY_FOR_PASS_TURN = -5
REWARD_PER_CAPTURED_PAWN = 1


def calculate_reward(choosen_action, game_state, current_player):
    action_info = action_matrice_to_action_infos(choosen_action, game_state)

    reward = 0

    if action_info["action"] == Action.KILL:
        reward += REWARD_FOR_KILL

    if action_info["action"] == Action.PUSH:
        reward += REWARD_FOR_PUSH

    if action_info["action"] == Action.PULL:
        reward += REWARD_FOR_PULL

    if action_info["action"] == Action.MOVE:
        reward += REWARD_FOR_MOVE

    if action_info["action"] == Action.ROTATE:
        reward += PENALTY_FOR_ROTATE

    if action_info["action"] == "pass_turn":
        possible_actions = actions_to_actions_matrice(game_state, current_player)
        player_pawns = [
            pawn
            for pawn in game_state.board_pawns
            if pawn.owner == current_player and pawn.is_alive
        ]

        ROTATE_AND_PASSTURN_ACTION = (len(player_pawns) * 3) + 1
        if len(possible_actions) >= ROTATE_AND_PASSTURN_ACTION:
            reward += PENALTY_FOR_PASS_TURN

        ROTATE_AND_PASSTURN_AND_MOVE_ACTION = (len(player_pawns) * 4) + 1
        if len(possible_actions) >= ROTATE_AND_PASSTURN_AND_MOVE_ACTION:
            reward += PENALTY_FOR_PASS_TURN

        ROTATE_AND_PASSTURN_AND_MOVE_AND_PUSH_PULL_ACTION = (len(player_pawns) * 6) + 1
        if len(possible_actions) >= ROTATE_AND_PASSTURN_AND_MOVE_AND_PUSH_PULL_ACTION:
            reward += PENALTY_FOR_PASS_TURN * 2

        ROTATE_AND_PASSTURN_AND_MOVE_AND_PUSH_PULL_AND_KILL_ACTION = (
            len(player_pawns) * 7
        ) + 1
        if (
            len(possible_actions)
            >= ROTATE_AND_PASSTURN_AND_MOVE_AND_PUSH_PULL_AND_KILL_ACTION
        ):
            reward += PENALTY_FOR_PASS_TURN * 4

    opponent_pawns = [
        pawn
        for pawn in game_state.board_pawns
        if pawn.owner != current_player and pawn.is_alive
    ]

    for pawn in opponent_pawns:
        if pawn.last_action == ReceivedAction.IS_PULLED:
            reward += REWARD_FOR_PULL_OPPONENT
            break
        if pawn.last_action == ReceivedAction.IS_PUSHED:
            reward += REWARD_FOR_PUSH_OPPONENT
            break
    lost_pawns = game_state.determine_players_lost_pawns()
    player1_captured = len(lost_pawns["player2s_lost_pawns"])
    player2_captured = len(lost_pawns["player1s_lost_pawns"])

    if current_player == PlayerRole.PLAYER1:
        reward += player1_captured * REWARD_PER_CAPTURED_PAWN
        reward -= player2_captured * REWARD_PER_CAPTURED_PAWN
    if current_player == PlayerRole.PLAYER2:
        reward += player2_captured * REWARD_PER_CAPTURED_PAWN
        reward -= player1_captured * REWARD_PER_CAPTURED_PAWN

    if game_state.winner:
        reward += (
            REWARD_FOR_VICTORY
            if game_state.winner == current_player
            else -REWARD_FOR_VICTORY
        )

    print(f"Récompense: {reward}")

    return reward
