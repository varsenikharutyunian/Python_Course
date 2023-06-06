class  Board_Class:
    """_sumary_
    """
    def __init__(self) -> None:
        self.board_sate=["*","*","*","*","*","*","*","*","*"]
    
    def change_board_state(self,number:int,string:str):
        """change board state 
        Args:
            number (int):cordinates
            string (str): x or o
        """
        self.board_sate[number -1] = string
        

    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board_sate[row*3+ col], end =" ")   
            print()   
    
    def get_free_slots(self):
        free_slots = []
        for index ,value in enumerate(self.board_sate):
            if value =="*":
                free_slots.append(index+1)
        return free_slots        
            
if __name__ == "__main__" :
    b= Board_Class()
    b.change_board_state(3, 'x')
    b.change_board_state(5, 'o')  
    b.print_board() 
    print(b.get_free_slots())       