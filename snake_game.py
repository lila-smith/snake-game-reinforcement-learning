from snake_model import GameBoard
from snake_view import PygameView
from snake_controller import SnakePlayer
import time


def main():
    """
    
    """
    gameboard = GameBoard(15)
    graphic_view = PygameView(gameboard)
    controls = SnakePlayer(gameboard)
    
    graphic_view.draw()
    

    while not gameboard.end_condition:
        controls.get_input()
        gameboard.check_next_square()
        graphic_view.draw()
        time.sleep(.2)
        
    
if __name__ == "__main__":
    main()