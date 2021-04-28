from snake_model import GameBoard
from snake_view import PygameView
from snake_controller import SnakePlayer


def main():
    """
    
    """
    gameboard = GameBoard(10)
    graphic_view = PygameView(gameboard)
    
    graphic_view.draw()
    
if __name__ == "__main__":
    main()