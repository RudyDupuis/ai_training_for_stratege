def display_board(game_state):
    print(
        "Turn: "
        + str(game_state.turn)
        + " - Player: "
        + str(game_state.determine_player_based_on_turn().name)
        + " - Winner: "
        + str(game_state.winner.name if game_state.winner else None)
        + " - Pawns: p1 - "
        + str(
            (8 - len(game_state.determine_players_lost_pawns()["player1s_lost_pawns"]))
        )
        + " | p2 - "
        + str(
            (8 - len(game_state.determine_players_lost_pawns()["player2s_lost_pawns"]))
        )
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
