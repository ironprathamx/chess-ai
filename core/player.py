"""Player abstractions for human and engine opponents."""

from engine.stockfish_engine import get_best_move


class Player:
    """Base class for chess players."""

    def __init__(self,color):
        self.color=color
    def get_move(self,game):
        raise NotImplementedError
    
class HumanPlayer(Player):
    """Reads moves supplied interactively via set_move()."""

    def __init__(self,color):
        super().__init__(color)
        self.pending_move=None

    def set_move(self,move):
        self.pending_move=move
        
    def get_move(self,game):
        move = self.pending_move
        self.pending_move = None
        return move
    
class EnginePlayer(Player):
    """Selects moves using the Stockfish UCI engine."""

    def __init__(self, color):
        super().__init__(color)

    def get_move(self, game):
        fen = game.get_fen()
        return get_best_move(fen)