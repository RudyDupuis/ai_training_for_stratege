from game_logic.enums.PlayerRole import PlayerRole
from game_logic.utils.build_board import build_board
from game_logic.utils.determine_winner import determine_winner
from game_logic.utils.determine_players_lost_pawns import determine_players_lost_pawns
from game_logic.utils.determineAvailablePositionsForActions.determine_available_positions_for_actions import (
    determine_available_positions_for_actions,
)
from game_logic.utils.find_pawn_by_position import find_pawn_by_position


class GameState:
    MAX_PAWN_MOVEMENT = 2
    MAX_PAWNS_PER_PLAYER = 8
    BOARD_WIDTH = 8
    BOARD_HEIGHT = 8
    TURN_TIME_SECONDS = 100
    GIVE_UP_TIME_SECONDS = 30

    def __init__(self, turn, boardPawns):
        if len(boardPawns) != GameState.MAX_PAWNS_PER_PLAYER * 2:
            raise ValueError(
                f"Le nombre de pions doit être exactement de {GameState.MAX_PAWNS_PER_PLAYER * 2}."
            )

        self.turn = turn
        self.boardPawns = boardPawns
        self.board = build_board(self.boardPawns)
        self.winner = None
        self.checkIfThereIsAWinner()

    def updateBoard(self):
        self.board = build_board(self.boardPawns)

    def updatePawn(self, newPawn):
        self.boardPawns = [
            newPawn if oldPawn.id == newPawn.id else oldPawn
            for oldPawn in self.boardPawns
        ]

    def checkIfThereIsAWinner(self):
        if self.winner:
            return

        playersLostPawns = self.determinePlayersLostPawns()
        self.winner = determine_winner(
            playersLostPawns["player1s_lost_pawns"],
            playersLostPawns["player2s_lost_pawns"],
        )

    def determinePlayerBasedOnTurn(self):
        return PlayerRole.Player2 if self.turn % 2 == 0 else PlayerRole.Player1

    def determinePlayersLostPawns(self):
        return determine_players_lost_pawns(self.boardPawns)

    def findPawnByPosition(self, pawnPosition):
        return find_pawn_by_position(self.boardPawns, pawnPosition)

    def resetRemainingMovesPawns(self):
        for pawn in self.boardPawns:
            pawn.remainingMove = GameState.MAX_PAWN_MOVEMENT

    def resetLastActionAndPositionPawns(self):
        for pawn in self.boardPawns:
            pawn.lastAction = None
            pawn.lastPosition = None

    def determineAvailablePositionsForActions(self, pawn, player):
        return determine_available_positions_for_actions(self, pawn, player)

    @staticmethod
    def isInBoardGameBounds(board, row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    @staticmethod
    def isCellOccupied(board, row, col):
        return board[row][col] != None
