from game_logic.enums.PlayerRole import PlayerRole
from game_logic.enums.Orientation import Orientation
from game_logic.ai_formatting.utils.pawn_id_formatter import pawn_id_formatter
import numpy as np


def formatting_game_data_for_ai(gameState):
    simplified_board = []
    for row in gameState.board:
        simplified_row = []
        for cell in row:
            if cell is None:
                simplified_row.append([0, 0])
            else:
                simplified_row.append(pawn_id_formatter(cell))

        simplified_board.append(simplified_row)

    simplified_pawns_info = []
    for pawn in gameState.boardPawns:
        simplified_pawns_info.append(
            [
                pawn_id_formatter(pawn)[0],
                pawn_id_formatter(pawn)[1],
                1 if pawn.isAlive else 0,
                pawn.remainingMove,
                1 if pawn.orientation == Orientation.NE else 0,
                1 if pawn.orientation == Orientation.NW else 0,
                1 if pawn.orientation == Orientation.SE else 0,
                1 if pawn.orientation == Orientation.SW else 0,
            ]
        )

    flattened_board = np.array(simplified_board).flatten()
    flattened_pawns_info = np.array(simplified_pawns_info).flatten()

    return np.concatenate((flattened_board, flattened_pawns_info))
