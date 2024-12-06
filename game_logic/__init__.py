from game_logic.classes.GameState import GameState
from game_logic.utils.initial_board import initial_board
from game_logic.ai_formatting.formatting_game_data_for_ai import (
    formatting_game_data_for_ai,
)
from game_logic.ai_formatting.formatting_possible_actions_for_ai import (
    formatting_possible_actions_for_ai,
)
from game_logic.ai_formatting.do_action import do_action
import random


def display_board(game_state):
    print(
        "Turn: "
        + str(game_state.turn)
        + " - Player: "
        + str(game_state.determinePlayerBasedOnTurn().name)
        + " - Winner: "
        + str(game_state.winner.name if game_state.winner else None)
        + " - Pawns: p1 - "
        + str((8 - len(game_state.determinePlayersLostPawns()["player1s_lost_pawns"])))
        + " | p2 - "
        + str((8 - len(game_state.determinePlayersLostPawns()["player2s_lost_pawns"])))
    )
    print("      " + "      ".join([str(i) for i in range(len(game_state.board[0]))]))
    print("  +" + "------+" * len(game_state.board[0]))
    for row_idx, row in enumerate(game_state.board):
        row1_display = (
            f"{row_idx} | "
            + " | ".join([str(cell.id) if cell else "    " for cell in row])
            + " |"
        )
        row2_display = "  | "
        for cell in row:
            if cell:
                if cell.orientation.name == "SE":
                    row2_display += "  ◢  | "
                elif cell.orientation.name == "SW":
                    row2_display += "  ◣  | "
                elif cell.orientation.name == "NE":
                    row2_display += "  ◥  | "
                elif cell.orientation.name == "NW":
                    row2_display += "  ◤  | "
            else:
                row2_display += "     | "
        print(row1_display)
        print(row2_display)
        print("  +" + "------+" * len(game_state.board[0]))


def test_game_logic():
    gameState = GameState(1, initial_board())

    display_board(gameState)

    for i in range(1000):
        do_action(
            random.choice(
                formatting_possible_actions_for_ai(
                    gameState, gameState.determinePlayerBasedOnTurn()
                )
            ),
            gameState,
            gameState.determinePlayerBasedOnTurn(),
        )
        display_board(gameState)

    # print(formatting_game_data_for_ai(gameState))
    # print(formatting_possible_actions_for_ai(gameState, gameState.determinePlayerBasedOnTurn()))
