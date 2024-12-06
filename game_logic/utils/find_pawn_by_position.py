def find_pawn_by_position(board_pawns, pawn_position):
    pawn = next(
        (
            pawn
            for pawn in board_pawns
            if pawn.position.row == pawn_position.row
            and pawn.position.col == pawn_position.col
            and pawn.isAlive
        ),
        None,
    )

    if pawn is None:
        raise ValueError("Une erreur est survenue lors de la recherche du pion.")

    return pawn
