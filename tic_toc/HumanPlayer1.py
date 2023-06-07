from Player import Player


class HumanPlayer(Player):
    """-summary_
    
    Args:
        Player (_type): _description_   
    """
    
    def move(self):
        while True:
            number = input("Choose board coors from 1-9:->")
            # if user input is not digit
            if number.isdigit():
                number = int(number)
            else:
                print("Type  integer from 1-9")  
                continue
            
            if number not in list(range(1, 10)):
                print("Integer should be from 1  to 9 range")
                continue
            
            if number not in self.board.get_free_slots():
                print(f"Choosen slot is not avilable.Choose another number from{self.board.get_free_slots()} this opshons")
                continue
            
            break
        print("number = ", number)
        self.board.change_board_state(number,self.value)
        


