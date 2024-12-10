def build_board(board_pawns):
    from game_logic.classes.game_state import GameState

    board = [
        [None for _ in range(GameState.BOARD_WIDTH)]
        for _ in range(GameState.BOARD_HEIGHT)
    ]

    for pawn in board_pawns:
        if pawn.is_alive:
            position = pawn.position

            if (
                0 <= position.row < GameState.BOARD_HEIGHT
                and 0 <= position.col < GameState.BOARD_WIDTH
            ):
                board[position.row][position.col] = pawn
            else:
                raise ValueError(
                    f"Position du pion ({position.row}, {position.col}) hors du plateau."
                )

    return board
