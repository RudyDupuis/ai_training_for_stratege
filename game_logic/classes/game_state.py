from game_logic.enums.player_role import PlayerRole
from game_logic.game_state_methods.build_board import build_board
from game_logic.game_state_methods.determine_winner import determine_winner
from game_logic.game_state_methods.determine_players_lost_pawns import (
    determine_players_lost_pawns,
)
from game_logic.game_state_methods.determine_available_positions_for_actions.determine_available_positions_for_actions import (
    determine_available_positions_for_actions,
)
from game_logic.game_state_methods.find_pawn_by_position import find_pawn_by_position


class GameState:
    MAX_PAWN_MOVEMENT = 2
    MAX_PAWNS_PER_PLAYER = 8
    BOARD_WIDTH = 8
    BOARD_HEIGHT = 8
    TURN_TIME_SECONDS = 100
    GIVE_UP_TIME_SECONDS = 30

    def __init__(self, turn, board_pawns):
        if len(board_pawns) != GameState.MAX_PAWNS_PER_PLAYER * 2:
            raise ValueError(
                f"Le nombre de pions doit être exactement de {GameState.MAX_PAWNS_PER_PLAYER * 2}."
            )

        self.turn = turn
        self.board_pawns = board_pawns
        self.board = build_board(self.board_pawns)
        self.winner = None
        self.check_if_there_is_a_winner()

    def update_board(self):
        self.board = build_board(self.board_pawns)

    def update_pawn(self, new_pawn):
        self.board_pawns = [
            new_pawn if old_pawn.id == new_pawn.id else old_pawn
            for old_pawn in self.board_pawns
        ]

    def check_if_there_is_a_winner(self):
        if self.winner:
            return

        players_lost_pawns = self.determine_players_lost_pawns()
        self.winner = determine_winner(
            players_lost_pawns["player1s_lost_pawns"],
            players_lost_pawns["player2s_lost_pawns"],
        )

    def determine_player_based_on_turn(self):
        return PlayerRole.PLAYER2 if self.turn % 2 == 0 else PlayerRole.PLAYER1

    def determine_players_lost_pawns(self):
        return determine_players_lost_pawns(self.board_pawns)

    def find_pawn_by_position(self, pawn_position):
        return find_pawn_by_position(self.board_pawns, pawn_position)

    def reset_remaining_moves_pawns(self):
        for pawn in self.board_pawns:
            pawn.remaining_move = GameState.MAX_PAWN_MOVEMENT

    def reset_last_action_and_position_pawns(self):
        for pawn in self.board_pawns:
            pawn.last_action = None
            pawn.last_position = None

    def determine_available_positions_for_actions(self, pawn, player):
        return determine_available_positions_for_actions(self, pawn, player)

    @staticmethod
    def is_in_board_game_bounds(board, row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    @staticmethod
    def is_cell_occupied(board, row, col):
        return board[row][col] is not None
