"""Board representation and move handling."""

import chess


class Board:
    """Thin wrapper around python-chess for game state and UCI moves."""
    def __init__(self, fen=None):
        if(fen):
            self.board=chess.Board(fen)
        else:
            self.board=chess.Board()

    def print_board(self):
        print(self.board)

    def make_move(self,uci):
        try:
            move=chess.Move.from_uci(uci)
        except chess.InvalidMoveError:
            return False
        except ValueError:
            return False
        if(move in self.board.legal_moves):
            self.board.push(move)
            return True
        else:
            return False
    def undo_move(self):
        try:
            self.board.pop()
            return True
        except IndexError:
            return False

    def get_fen(self):
        return self.board.fen()
    
    def load_fen(self,fen):
        self.board=chess.Board(fen)
        

