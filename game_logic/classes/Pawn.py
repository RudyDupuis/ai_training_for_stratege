class Pawn:
    def __init__(
        self,
        id,
        owner,
        isAlive,
        remainingMove,
        orientation,
        position,
        lastPosition=None,
        lastAction=None,
    ):
        self.id = id
        self.owner = owner
        self.isAlive = isAlive
        self.remainingMove = remainingMove
        self.orientation = orientation
        self.position = position
        self.lastPosition = lastPosition
        self.lastAction = lastAction
