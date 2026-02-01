from core.board import Board

class Game:
    def __init__(self):
        self.b=Board()
        self.turn_white:bool=True
        self.running=True

    def request_move(self,player_color, uci_move):
        if(self.running==False):
            return False
        if(player_color=="White" and self.turn_white==True):
            chk=self.b.make_move(uci_move)
            if(chk==False):
                return False
            self.turn_white=False
            if(self.b.is_game_over()==True):
                self.running=False
            return True
        elif(player_color=="Black" and self.turn_white==False):
            chk=self.b.make_move(uci_move)
            if(chk==False):
                return False
            self.turn_white=True
            if(self.b.is_game_over()==True):
                self.running=False
            return True
        
        else:
            return False

