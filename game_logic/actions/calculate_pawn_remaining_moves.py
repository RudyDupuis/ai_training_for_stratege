def calculate_pawn_remaining_moves(pawn, desired_pawn_position):
    move_distance = abs(pawn.position.row - desired_pawn_position.row) + abs(
        pawn.position.col - desired_pawn_position.col
    )

    pawn.remaining_move -= move_distance
