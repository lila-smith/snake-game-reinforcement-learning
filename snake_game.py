from snake_model import GameBoard
from snake_view import PygameView
from snake_controller import SnakePlayer
import time
import pygame


def main():
    """
    
    """
    pygame.init()
    
    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.set_allowed(pygame.KEYDOWN)

    gameboard = GameBoard(20)
    graphic_view = PygameView(gameboard)
    controls = SnakePlayer(gameboard)
    
    graphic_view.draw()

    pygame.event.clear()
    while not controls.check_input_list(pygame.KEYDOWN):
        graphic_view.start_text()
        controls.check_to_exit()
        if controls.check_input_list(pygame.KEYDOWN):
            break
        time.sleep(1.5)
        
        graphic_view.draw()
        controls.check_to_exit()
        if controls.check_input_list(pygame.KEYDOWN):
            break
        time.sleep(.5)

    while not gameboard.end_condition:
        controls.get_input()
        gameboard.check_next_square()
        graphic_view.draw()
        controls.check_to_exit()
        time.sleep(.2)

    while gameboard.end_condition:
        controls.check_to_exit()
        graphic_view.draw_gameover()
    
if __name__ == "__main__":
    main()