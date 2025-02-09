"""
This module assembles the MVC components to create a functional snake game.
"""

import time
import pygame
from snake_model import GameBoard
from snake_view import PygameView, PygameViewRL
from snake_controller import SnakePlayer, MarkovPlayer, RLPlayer, check_to_exit, check_to_exit_rl, check_input_list, get_restart_input
import pandas as pd

csv = "snake1.csv"
rounds = 500

def main():
    """
    Run a learning round of snake games

    Args:
        None
    Returns:
        No return value
    """
    for i in range(rounds):

        pygame.init()

        pygame.event.set_allowed(pygame.QUIT)
        pygame.event.set_allowed(pygame.KEYDOWN)

        gameboard = GameBoard(20)
        graphic_view = PygameViewRL(gameboard)
        controls = SnakePlayer(gameboard)
        fake_controls = RLPlayer(gameboard,"snake1.csv", "snake1_record.csv", new_agent=False, e=0)

        graphic_view.draw()

        pygame.event.clear()

        while not gameboard.end_condition:
            fake_controls.get_input()
            gameboard.check_next_square()
            graphic_view.draw()
            check_to_exit_rl(fake_controls)
            time.sleep(.05)

        fake_controls.export_at_endgame()




if __name__ == "__main__":
    main()
