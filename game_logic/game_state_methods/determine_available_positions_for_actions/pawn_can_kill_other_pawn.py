def pawn_can_kill_other_pawn(
    other_pawn,
    orientation1,
    orientation2,
    positions_available_for_killing,
    new_position,
):
    if other_pawn.orientation in (orientation1, orientation2):
        positions_available_for_killing.append(new_position)
