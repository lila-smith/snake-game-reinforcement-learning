"""
This module assembles the MVC components to create a functional snake game.
"""

import time
import pygame
from snake_model import GameBoard
from snake_view import PygameView
from snake_controller import SnakePlayer, check_to_exit, check_input_list, get_restart_input


def main():
    """
    Run a functional snake game

    Args:
        None
    Returns:
        No return value
    """
    pygame.init()

    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.set_allowed(pygame.KEYDOWN)

    gameboard = GameBoard(20)
    graphic_view = PygameView(gameboard)
    controls = SnakePlayer(gameboard)

    graphic_view.draw()

    pygame.event.clear()
    while not check_input_list(pygame.KEYDOWN):
        graphic_view.start_text()
        check_to_exit()

    while not gameboard.end_condition:
        controls.get_input()
        gameboard.check_next_square()
        graphic_view.draw()
        check_to_exit()
        time.sleep(.2)

    while gameboard.end_condition:
        graphic_view.draw_gameover()
        if get_restart_input() is True:
            main()
        check_to_exit()


if __name__ == "__main__":
    main()
