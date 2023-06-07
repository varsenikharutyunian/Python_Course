import random
from Player import Player


class ComputerPlayer(Player):
    """ _summary_
    
    Args:
        Player (_type_):_dwscription_
    """    
    def move(self):
        
        number = random.choice(self.board.get_free_slots())
        print("number = ",number)
        self.board.change_board_state(number,self.value)
        
