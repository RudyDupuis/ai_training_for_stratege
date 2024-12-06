from game_logic.classes.PawnPosition import PawnPosition


def pawn_can_push_or_pull_other_pawn(
    gameState, arrivalPositionRow, arrivalPositionCol, positionsAvailable
):
    from game_logic.classes.GameState import GameState

    if GameState.isInBoardGameBounds(
        gameState.board, arrivalPositionRow, arrivalPositionCol
    ) and not GameState.isCellOccupied(
        gameState.board, arrivalPositionRow, arrivalPositionCol
    ):
        positionsAvailable.append(PawnPosition(arrivalPositionRow, arrivalPositionCol))
