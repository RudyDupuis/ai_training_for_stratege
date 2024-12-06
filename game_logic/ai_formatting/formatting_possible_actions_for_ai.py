from game_logic.enums.Action import Action
from game_logic.enums.Orientation import Orientation
from game_logic.ai_formatting.utils.action_formatter import ai_action_formatter


def formatting_possible_actions_for_ai(gameState, player):
    possible_actions = []
    player_pawns = [
        pawn for pawn in gameState.boardPawns if pawn.owner == player and pawn.isAlive
    ]

    for pawn in player_pawns:
        availablePositionsForActions = gameState.determineAvailablePositionsForActions(
            pawn, player
        )

        for movePosition in availablePositionsForActions.positionsAvailableForMoving:
            possible_actions.append(
                ai_action_formatter(Action.Move, pawn, movePosition, None)
            )

        for killPosition in availablePositionsForActions.positionsAvailableForKilling:
            possible_actions.append(
                ai_action_formatter(Action.Kill, pawn, killPosition, None)
            )

        for pushPosition in availablePositionsForActions.positionsAvailableForPushing:
            possible_actions.append(
                ai_action_formatter(Action.Push, pawn, pushPosition, None)
            )

        for pullPosition in availablePositionsForActions.positionsAvailableForPulling:
            possible_actions.append(
                ai_action_formatter(Action.Pull, pawn, pullPosition, None)
            )

        for orientation in Orientation:
            possible_actions.append(
                ai_action_formatter(Action.Rotate, pawn, None, orientation)
            )

    possible_actions.append(ai_action_formatter("pass", None, None, None))

    return possible_actions
