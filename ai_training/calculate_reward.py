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
REWARD_FOR_PASS_TURN = 10
REWARD_PER_CAPTURED_PAWN = 0.5


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
        print(f"Nombre d'actions possibles: {len(possible_actions)}")

        player_pawns = [
            pawn
            for pawn in game_state.board_pawns
            if pawn.owner == current_player and pawn.is_alive
        ]

        TWO_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN = (
            len(player_pawns) * 4
        ) + 1

        FOUR_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN = (
            len(player_pawns) * 6
        ) + 1

        SIX_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN = (
            len(player_pawns) * 8
        ) + 1

        if (
            len(possible_actions)
            < TWO_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN
        ):
            print(
                f"Seuil 2 actions restantes par pions: {TWO_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN}"
            )
            reward += REWARD_FOR_PASS_TURN

        elif (
            len(possible_actions)
            < FOUR_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN
        ):
            print(
                f"Seuil 4 actions restantes par pions: {FOUR_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN}"
            )
            reward += PENALTY_FOR_PASS_TURN

        elif (
            len(possible_actions)
            < SIX_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN
        ):
            print(
                f"Seuil 6 actions restantes par pions: {SIX_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN}"
            )
            reward += PENALTY_FOR_PASS_TURN * 2

        else:
            print(
                f"Seuil plus de 6 actions restantes par pions: >{SIX_REMAINING_ACTIONS_PER_PAWN_MINUS_ROTATES_AND_PASSTURN}"
            )
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
