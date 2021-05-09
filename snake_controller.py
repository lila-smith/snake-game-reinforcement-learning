"""
This module contains the controller for the snake game, which is a class called
SnakePlayer. It includes methods for checking for arrow key input and updating
the gameboard accordingly.
"""

import sys
import pygame


class SnakePlayer:
    """
    Snake game controller that is used to update the gameboard using keyboard
    input.

    Attributes:
        _board: an instance of the GameBoard class
    """
    key_value = {
        pygame.K_LEFT: [0, -1],
        pygame.K_RIGHT: [0, 1],
        pygame.K_UP: [-1, 0],
        pygame.K_DOWN: [1, 0],
    }
    opposite = {
        pygame.K_LEFT: [0, 1],
        pygame.K_RIGHT: [0, -1],
        pygame.K_UP: [1, 0],
        pygame.K_DOWN: [-1, 0],
    }

    def __init__(self, board_instance):
        """
        Initialize the controller with a gameboard, so that the controller
        can update the model

        Args:
            board_instance: a gameboard, which is an instance of class
            GameBoard
        Returns:
            No return value
        """
        self._board = board_instance

    @property
    def board(self):
        """
        Return the gameboard, which is a private attribute

        Args:
            None
        Returns:
            self._board: the gameboard
        """
        return self._board

    def get_input(self):
        """
        Access the pygame event queue and update the gameboard according to
        the arrow key input

        Args:
            None
        Returns:
            No return value
        """
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN and event.key in self.key_value:
            if self.board.snake_length == 1 or \
                    not self.board.direction == self.opposite[event.key]:
                self.board.change_direction(self.key_value[event.key])


def check_to_exit():
    """
    Close the game if the player has x-ed out of the pygame screen

    Args:
        None
    Returns:
        No return value
    """
    if pygame.event.peek(pygame.QUIT):
        sys.exit()


def check_input_list(event_type=None):
    """
    Check if there are any events in the queue

    Args:
        event_type: a pygame event type, which is None by default
    Returns:
        True, if there are any of the given event in the queue
        False, if otherwise
    """
    return pygame.event.peek(event_type)


def get_restart_input():
    """
    Get user input when displaying end screen and either restart the game
    or quit the game

    Args:
        None
    Returns:
        True, if the user inputs "y" to restart the game
        No return value, if the user inputs "n" - quits the game
        None, if the user inputs something other than "y" or "n"
    """
    event = pygame.event.poll()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_y:
            return True

        if event.key == pygame.K_n:
            return False
            sys.exit()
    return None
