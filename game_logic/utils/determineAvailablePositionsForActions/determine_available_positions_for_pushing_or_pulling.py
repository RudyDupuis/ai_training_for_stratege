from game_logic.utils.determineAvailablePositionsForActions.pawn_can_push_or_pull_other_pawn import (
    pawn_can_push_or_pull_other_pawn,
)


def determine_available_positions_for_pushing_or_pulling(
    gameState, pawn, positionsAvailableForPushing, positionsAvailableForPulling
):
    from game_logic.classes.GameState import GameState
    from game_logic.utils.determineAvailablePositionsForActions.determine_available_positions_for_actions import (
        PAWN_POSITION_DIRECTIONS,
        PAWN_POSITION_TOP,
        PAWN_POSITION_BOTTOM,
        PAWN_POSITION_LEFT,
        PAWN_POSITION_RIGHT,
    )

    if pawn.remainingMove == 0:
        return

    for direction in PAWN_POSITION_DIRECTIONS:
        newRow = pawn.position.row + direction.row
        newCol = pawn.position.col + direction.col

        if GameState.isInBoardGameBounds(
            gameState.board, newRow, newCol
        ) and GameState.isCellOccupied(gameState.board, newRow, newCol):
            if direction == PAWN_POSITION_TOP:
                pawn_can_push_or_pull_other_pawn(
                    gameState, newRow - 1, newCol, positionsAvailableForPushing
                )
                pawn_can_push_or_pull_other_pawn(
                    gameState, newRow + 2, newCol, positionsAvailableForPulling
                )
            elif direction == PAWN_POSITION_BOTTOM:
                pawn_can_push_or_pull_other_pawn(
                    gameState, newRow + 1, newCol, positionsAvailableForPushing
                )
                pawn_can_push_or_pull_other_pawn(
                    gameState, newRow - 2, newCol, positionsAvailableForPulling
                )
            elif direction == PAWN_POSITION_LEFT:
                pawn_can_push_or_pull_other_pawn(
                    gameState, newRow, newCol - 1, positionsAvailableForPushing
                )
                pawn_can_push_or_pull_other_pawn(
                    gameState, newRow, newCol + 2, positionsAvailableForPulling
                )
            elif direction == PAWN_POSITION_RIGHT:
                pawn_can_push_or_pull_other_pawn(
                    gameState, newRow, newCol + 1, positionsAvailableForPushing
                )
                pawn_can_push_or_pull_other_pawn(
                    gameState, newRow, newCol - 2, positionsAvailableForPulling
                )
