"""Game loop and turn management."""

from core.board import Board
from core.player import Player


class Game:
    """Coordinates two players, the board, and game-over detection."""
    def __init__(self,white_player:Player,black_player:Player):
        self.b=Board()
        self.turn_white:bool=True
        self.running=True
        self.white_player=white_player
        self.black_player=black_player

    def request_turn(self):
        if(self.running==False):
            return False
        if(self.turn_white==True):
            self.current_player=self.white_player
        else:
            self.current_player=self.black_player
        move=self.current_player.get_move(self)
        if (move is None):
            return False
        chk=self.b.make_move(move)
        if(chk==False):
            return False
        self.turn_white=(not self.turn_white)
        if(self.b.board.is_game_over()==True):
            self.running=False
        return True


    def get_fen(self):
        return self.b.get_fen()

    def is_running(self):
        return self.running
    
    def get_curr_color(self):
        if self.turn_white==True:
            return "white"
        else:
            return "black"
        
    def print_board(self):
        self.b.print_board()