import random
from game_logic.classes.game_state import GameState
from game_logic.game_state_methods.initial_board import initial_board
from game_logic.displays.display_board import display_board
from game_logic.actions.do_action import do_action
from game_logic.mappers.board_and_actions_data_to_state_matrice_and_actions_matrice import (
    actions_to_actions_matrice,
)


def test_game_logic(range_number=200):
    game_state = GameState(1, initial_board())

    display_board(game_state)

    for _ in range(range_number):
        do_action(
            random.choice(
                actions_to_actions_matrice(
                    game_state, game_state.determine_player_based_on_turn()
                )
            ),
            game_state,
            game_state.determine_player_based_on_turn(),
        )
        display_board(game_state)
