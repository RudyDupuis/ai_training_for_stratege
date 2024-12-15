import os
from game_logic.classes.game_state import GameState
from game_logic.enums.player_role import PlayerRole
from game_logic.game_state_methods.initial_board import initial_board
from game_logic.mappers.board_and_actions_data_to_state_matrice_and_actions_matrice import (
    board_infos_data_to_state_matrice,
    actions_to_actions_matrice,
)
from game_logic.actions.do_action import do_action
from game_logic.displays.display_board import display_board
from ai_training.calculate_reward import calculate_reward
from ai_training.agent import Agent


def train_agents(num_episodes, start_episode=0):
    agent1 = Agent(
        name="Agent1", player_role=PlayerRole.PLAYER1
    )
    agent2 = Agent(
        name="Agent2", player_role=PlayerRole.PLAYER2
    )

    if not os.path.exists("saved_model/"):
        os.makedirs("saved_model/")

    for episode in range(num_episodes):
        current_episode = episode + start_episode
        game_state = GameState(1, initial_board())
        done = False

        while not done:
            current_player = game_state.determine_player_based_on_turn()
            current_agent = agent1 if current_player == PlayerRole.PLAYER1 else agent2

            state = board_infos_data_to_state_matrice(game_state)
            possible_actions = actions_to_actions_matrice(game_state, current_player)

            choosen_action = current_agent.choose_action(state, possible_actions)
            do_action(choosen_action, game_state, current_player)

            reward = calculate_reward(choosen_action, game_state, current_player)

            if game_state.winner:
                done = True

            next_state = board_infos_data_to_state_matrice(game_state)
            next_possible_actions = actions_to_actions_matrice(
                game_state, current_player
            )

            current_agent.train(
                state, choosen_action, reward, next_state, next_possible_actions
            )

            print(f"Épisode {current_episode}")
            display_board(game_state)

        if episode % 1000 == 0:
            agent1.model.save(f"h5/{current_episode}_agent1.h5")
            agent2.model.save(f"h5/{current_episode}_agent2.h5")

            agent2.model.export(f"saved_model/{current_episode}_agent2")
