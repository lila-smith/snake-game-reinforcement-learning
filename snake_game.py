from snake_model import GameBoard
from snake_view import PygameView
from snake_controller import SnakePlayer
import time


def main():
    """
    
    """
    gameboard = GameBoard(20)
    graphic_view = PygameView(gameboard)
    controls = SnakePlayer(gameboard)
    
    graphic_view.draw()
    

    while not gameboard.end_condition:
        
        while controls.check_input_list():
            controls.check_to_exit()
            controls.get_input()
            gameboard.check_next_square()
            graphic_view.draw()
            time.sleep(.2)
            
        gameboard.check_next_square()
        graphic_view.draw()
        time.sleep(.2)

    while gameboard.end_condition:
        controls.check_to_exit()
        graphic_view.draw_gameover()
    
if __name__ == "__main__":
    main()