from dataclasses import dataclass, field
from game_logic.enums.player_role import PlayerRole
from game_logic.enums.orientation import Orientation
from game_logic.enums.action import Action
from game_logic.classes.pawn_position import PawnPosition


@dataclass
class Pawn:
    id: str
    owner: PlayerRole
    is_alive: bool
    remaining_move: int
    orientation: Orientation
    position: PawnPosition
    last_position: PawnPosition = field(default=None)
    last_action: Action = field(default=None)
