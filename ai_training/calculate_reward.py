from game_logic.enums.action import Action
from game_logic.enums.player_role import PlayerRole
from game_logic.mappers.action_matrice_to_action_infos import (
    action_matrice_to_action_infos,
)


def calculate_reward(choosen_action, game_state, current_player):
    action_info = action_matrice_to_action_infos(choosen_action, game_state)

    reward = 0

    # Penalty for the duration of the game
    reward -= 0.1

    if action_info["action"] == Action.KILL:
        reward += 10

    if action_info["action"] == Action.PUSH:
        reward += 0.5

    if action_info["action"] == Action.PULL:
        reward += 0.5

    if action_info["action"] == Action.ROTATE:
        reward -= 0.5

    # Bonus if the agent has more pawns
    if current_player == PlayerRole.PLAYER1:
        if len(game_state.determine_players_lost_pawns()["player1s_lost_pawns"]) < len(
            game_state.determine_players_lost_pawns()["player2s_lost_pawns"]
        ):
            reward += 1
    if current_player == PlayerRole.PLAYER2:
        if len(game_state.determine_players_lost_pawns()["player2s_lost_pawns"]) < len(
            game_state.determine_players_lost_pawns()["player1s_lost_pawns"]
        ):
            reward += 1

    if game_state.winner:
        reward += 50 if game_state.winner == current_player else -50

    print(f"Récompense: {reward}")

    return reward
