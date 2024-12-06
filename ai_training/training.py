from game_logic.classes.GameState import GameState
from game_logic.enums.PlayerRole import PlayerRole
from game_logic.utils.initial_board import initial_board
from game_logic.ai_formatting.formatting_game_data_for_ai import (
    formatting_game_data_for_ai,
)
from game_logic.ai_formatting.formatting_possible_actions_for_ai import (
    formatting_possible_actions_for_ai,
)
from game_logic.ai_formatting.do_action import do_action
from game_logic import display_board
from ai_training.agent import Agent
import os


def train_agents(num_episodes=1000):
    # Initialisation des agents
    agent1 = Agent(name="Agent1", player_role=PlayerRole.Player1)
    agent2 = Agent(name="Agent2", player_role=PlayerRole.Player2)

    if not os.path.exists("saved_model/"):
        os.makedirs("saved_model/")

    # Boucle de jeu
    for episode in range(num_episodes):
        gameState = GameState(1, initial_board())
        done = False

        while not done:
            current_player = gameState.determinePlayerBasedOnTurn()
            current_agent = agent1 if current_player == PlayerRole.Player1 else agent2

            # Obtention de l'état du jeu et des actions possibles
            state = formatting_game_data_for_ai(gameState)
            possible_actions = formatting_possible_actions_for_ai(
                gameState, current_player
            )

            # Choisir une action
            action = current_agent.choose_action(state, possible_actions)

            # Effectuer l'action
            do_action(action, gameState, current_player)

            # Vérification de la fin de la partie
            if gameState.winner:
                done = True
                reward = (
                    1 if gameState.winner == current_player else -1
                )  # Récompense selon le gagnant
            else:
                reward = 0  # Pas de fin de partie

            # Obtenir le prochain état et les actions possibles
            next_state = formatting_game_data_for_ai(gameState)
            next_possible_actions = formatting_possible_actions_for_ai(
                gameState, current_player
            )

            # Entraîner l'agent avec l'état courant, l'action et la récompense
            current_agent.train(state, action, reward, next_state, next_possible_actions)

            # Afficher l'état du jeu
            display_board(gameState)

        agent1.model.save(f"saved_model/agent1_{episode}.h5")
        agent2.model.save(f"saved_model/agent2_{episode}.h5")
        print(f"Épisode {episode} terminé.")
