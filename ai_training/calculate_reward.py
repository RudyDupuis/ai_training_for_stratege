from game_logic.enums.action import Action, ReceivedAction
from game_logic.enums.player_role import PlayerRole
from game_logic.mappers.action_matrice_to_action_infos import (
    action_matrice_to_action_infos,
)

REWARD_FOR_KILL = 15
REWARD_FOR_PUSH = 0.5
REWARD_FOR_PULL = 0.5
REWARD_FOR_MOVE = 0.5
REWARD_FOR_PULL_OPPONENT = 2
REWARD_FOR_PUSH_OPPONENT = 0.5
PENALTY_FOR_ROTATE = -1
PENALTY_PER_TURN = -0.2
REWARD_FOR_VICTORY = 20
REWARD_PER_CAPTURED_PAWN = 5


def calculate_reward(choosen_action, game_state, current_player):
    action_info = action_matrice_to_action_infos(choosen_action, game_state)

    reward = 0
    reward += PENALTY_PER_TURN * game_state.turn

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
