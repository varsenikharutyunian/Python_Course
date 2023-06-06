from abc import abstractmethod
from Board import Board_Class

class Player:
    def __init__(self,value: str,board:Board_Class) ->   None:
        self.value = value
        self.board = board
    
    
    @abstractmethod 
    def move(self):
        pass
    
    
