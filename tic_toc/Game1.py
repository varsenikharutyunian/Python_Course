from Board import Board_Class
from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from Player import Player

class Game:
    def __init__(self) -> None:
        self.board = Board_Class()
        self.human = HumanPlayer("X", self.board) 
        self.computer = ComputerPlayer("0", self.board) 
        
    def play(self):
        while True:
            self.human.move()
            self.board.print_board()
            if self.check_status(self.human):
                break
            self.computer.move()
            self.board.print_board()
            if self.check_status(self.computer):
                break
            
    def check_status(self,player:Player) -> bool:
        board_state = self.board.board_sate
        for i in range(3):
            if board_state[ i*3: (i+1)*3] == [player.value]*3:
                print(player.value, "winner")
                return True        
            
            
    
            
            if [board_state[i],board_state[i+3],board_state[i+6]]==[player.value]*3:
                print(player.value, "winner")
                return True
        if [board_state[0],board_state[4],board_state[8]]==[player.value]*3:
            print(player.value, "winner")
            return True
        if [board_state[2],board_state[4],board_state[6]]==[player.value]*3:
            print(player.value, "winner")
            return True
        if len(self.board.get_free_slots())==0:
            print("Draw!")
            return True
            
        return False
            
            

if __name__ == "__main__":
    game = Game()  
    game.play() 
    