"""
This module contains the controller for the snake game, which is a class called
SnakePlayer. It includes methods for checking for arrow key input and updating
the gameboard accordingly.
"""

import sys
import pygame
import random
import numpy as np
import pandas as pd


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

class MarkovPlayer:
    """
    Snake game controller that is used to update the gameboard using keyboard
    input.

    Attributes:
        _board: an instance of the GameBoard class
    """
    key_value = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    rewards = {
        "apple": 50,
        "to_apple": 1,
        "away_apple": -1,
        "obstacle": -100
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
    
    def calculate_outcomes(self):
        empty, to_apples, apples = self.board.markov_state
        outcomes = ~np.array(empty)*self.rewards["obstacle"] + \
                   np.array(to_apples)*self.rewards["to_apple"] + \
                   ~np.array(to_apples)*self.rewards["away_apple"] + \
                   np.array(apples)*self.rewards["apple"]
        return outcomes

        
    def get_input(self):
        """
        Update the gameboard according to the Markov Decision Process

        Args:
            None
        Returns:
            No return value
        """
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()
        
        outcomes = self.calculate_outcomes()
        max_item = max(outcomes)
        index_list = [index for index in range(len(outcomes)) if outcomes[index] == max_item]
        self.board.change_direction(self.key_value[random.choice(index_list)])


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
            sys.exit()
    return None

class RLPlayer:
    """
    Snake game controller that is used to update the gameboard using keyboard
    input.

    Attributes:
        _board: an instance of the GameBoard class
    """
    key_value = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    rewards = {
        "apple": 50,
        "to_apple": 1,
        "away_apple": -1,
        "obstacle": -100
    }

    column_names = ["w_l","w_s","w_r","apple","tail","Q_k_l","k_l","Q_k_s","k_s","Q_k_r","k_r"]

    directions = [[-1,-1],[-1,0],[-1,1], \
                  [0,-1],[0,0],[0,1], \
                  [0,-1],[0,0],[0,1]]

    initial_reward = 5

    num_states = len(directions)**2 * 2**3

    walls = [True, False]

    def __init__(self, board_instance, path_to_agent):
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
        self._csv = path_to_agent
        temp_numpy = np.zeros([self.num_states, len(self.column_names)])
        print(np.shape(temp_numpy))
        i = 0
        for direction_tail in self.directions:
            for direction_apple in self.directions:
                for wall_l in self.walls:
                    for wall_s in self.walls:
                        for wall_r in self.walls:
                            temp_numpy[i,:] = np.array([wall_l, wall_s, wall_r, np.array(direction_apple), np.array(direction_tail), self.initial_reward, 1, self.initial_reward, 1, self.initial_reward, 1])
                            i += 1

        self._df = pd.DataFrame(temp_numpy, columns=self.column_names)
                            



        

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

    @property
    def df(self):
        """
        """
        return self._df

    @property
    def csv(self):
        """
        """
        return self._csv
    
    def calculate_outcomes(self):
        empty, to_apples, apples = self.board.markov_state
        outcomes = ~np.array(empty)*self.rewards["obstacle"] + \
                   np.array(to_apples)*self.rewards["to_apple"] + \
                   ~np.array(to_apples)*self.rewards["away_apple"] + \
                   np.array(apples)*self.rewards["apple"]
        return outcomes


        
    def get_input(self):
        """
        Update the gameboard according to the Markov Decision Process

        Args:
            None
        Returns:
            No return value
        """
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()
        
        outcomes = self.calculate_outcomes()
        max_item = max(outcomes)
        index_list = [index for index in range(len(outcomes)) if outcomes[index] == max_item]
        self.board.change_direction(self.key_value[random.choice(index_list)])

    def export_at_endgame(self):
        """
        """
        self.df.to_csv(self.csv)



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
