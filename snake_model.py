"""
This file outlines the GameBoard class that creates a model of the snake board
squares using a 2D list. It also includes the abstract class Object that's
inheritors are placed in the GameBoard to represent types of squares.
"""

import math
import random

class GameBoard:
    """
    Snake game representation.

    Attributes:
    _end_condition: Boolean representation for if game is over.
    _board_array: 2D list containing the one of objects (Apple, Blank, Border,
                  SnakeTail, or SnakeHead) for each square of the board
    _side: An integer for side length of the board in squares.
    _snake: List of ordered Snake positions (from head to end of tail).
    _direction: A list for current direction of motion referring to
                _board_array indices.
    """

    def __init__(self, side):
        """
        Initializes GameBoard with SnakeHead in center, a randomly spawned
        Apple, Border, and Blank instances.

        Args:
            side: An integer length of GameBoard. Includes borders. 
        """
        self._end_condition = False
        self._side = side
        self._direction = [0, 0] #Delta row, delta column
        self._board_array = [[None for _ in range(self._side)] \
                            for _ in range(self._side)]

        for row in range(self._side):
            for col in range(self._side):
                if row == 0 or row == self._side - 1 \
                or col == 0 or col == self._side - 1:
                    self._board_array[row][col] = Border()
                elif row == col == math.ceil(self._side / 2):
                    self._board_array[row][col] = SnakeHead()
                    self._snake = [[row, col]]
                else:
                    self._board_array[row][col] = Blank()
        self.spawn_apple()

    def __repr__(self):
        """
        Iterates through GameBoard to represent each square as part of string.
        """
        repr_string = ""
        for row in self.board_array:
            str_temp = ""
            for item in row:
                str_temp += repr(item)
            repr_string += str_temp + "\n"
        return repr_string

    @property    
    def board_array(self):
        return self._board_array

    @property
    def size(self):
        return self._side

    @property
    def direction(self):
        return self._direction
    
    @property
    def end_condition(self):
        return self._end_condition

    @property
    def snake_length(self):
        return len(self._snake)

    @property
    def snake(self):
        return self._snake

    def change_direction(self, direction):
        """
        Switches current direction to input. Any input outside of the specified
        may result in abnormal snake behavior.

        Args:
            direction: A two-element list that is one of the following: [1,0],
                       [-1,0], [0,1], or [0,-1].
        """
        self._direction = direction

    def check_next_square(self):
        """
        Moves snake in direction and interacts with the next square. The
        interaction will result in maintained velocity, increased length,
        or game over.
        """
        snake_head = self._snake[0]
        if not self.direction == [0,0]:
            self.board_array[(snake_head[0] + self.direction[0])] \
                        [(snake_head[1] + self.direction[1])] \
                        .interaction(self)

    def maintain_velocity(self):
        """
        Moves snake one block forward. 
        
        Removes last snake entry, changes current SnakeHead instance to
        SnakeTail instance, and adds new SnakeHead instance. Interaction is
        called when next square is Blank instance.
        """
        # Set up rows and cols to access
        previous_head = self._snake[0]
        last_square = self._snake.pop()
        next_square = [(previous_head[0] + self.direction[0]), \
                       (previous_head[1] + self.direction[1])]
        # Mark appropriate squares
        self.mark_square(last_square[0], last_square[1], Blank())
        self.mark_square(next_square[0], next_square[1], SnakeHead())
        if not self._snake == []:
            self.mark_square(previous_head[0], previous_head[1], SnakeTail())
        # Update snake list
        self._snake = [next_square] + self._snake

    def increase_length(self):
        """
        Moves snake one block forward and increases length by one. 
        
        Changes current SnakeHead instance to SnakeTail instance and adds new
        SnakeHead instance in front. Interaction is called when next square is
        Apple instance.
        """
        # Set up rows and cols to access
        previous_head = self._snake[0]
        next_square = [(previous_head[0] + self.direction[0]), \
                       (previous_head[1] + self.direction[1])]
        # Mark appropriate squares
        self.mark_square(next_square[0], next_square[1], SnakeHead())
        self.mark_square(previous_head[0], previous_head[1], SnakeTail())
        # Update snake list
        self._snake = [next_square] + self._snake
        # Make new apple
        self.spawn_apple()
    
    def spawn_apple(self):
        """
        Randomly chooses a Blank instance to turn into an Apple instance.
        """
        blank_indexes = []
        for row_index, row in enumerate(self.board_array):
            for col_index, item in enumerate(row):
                if isinstance(item, Blank):
                    blank_indexes.append([row_index, col_index])
        chosen_square = random.choice(blank_indexes)
        self.mark_square(chosen_square[0], chosen_square[1], Apple())
    
    def game_over(self):
        """
        Ends game.

        Changes end condition to True. Interaction is called when next square
        is Border or SnakeTail instance.
        """
        self._end_condition = True
    
    def get_square(self, row, col):
        """
        Returns the Object instance in specified row and column.

        Args:
            row: Integer less than _side for first index of _board_array.
            col: Integer less than _side for second index of _board_array.
        """
        return self.board_array[row][col]
    
    def mark_square(self, row, col, object_type):
        """
        Changes the Object in specified row and column.

        Args:
            row: Integer less than _side for first index of _board_array.
            col: Integer less than _side for second index of _board_array.
            object_type: An instance of inheritor of Object.
        """
        self._board_array[row][col] = object_type
    

from abc import ABC, abstractmethod
class Object(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def interaction(self, board_instance):
        pass
    
    @property
    @abstractmethod
    def color(self):
        """
        
        """
        pass
    

class Apple(Object):
    
    def __init__(self):
        """
        
        """
        self._color = (255, 0, 0)
    
    def interaction(self, board_instance):
        board_instance.increase_length()
    
    def __repr__(self):
        return "@"
    
    @property
    def color(self):
        """
        
        """
        return self._color

    
class Blank(Object):
    
    def __init__(self):
        """
        
        """
        self._color = (255, 255, 255)
    
    def interaction(self, board_instance):
        board_instance.maintain_velocity()
    
    def __repr__(self):
        return " "
    
    @property
    def color(self):
        """
        
        """
        return self._color

    
class Border(Object):
    
    def __init__(self):
        """
        
        """
        self._color = (0, 0, 0)
    
    def interaction(self, board_instance):
        board_instance.game_over()
    
    def __repr__(self):
        return "#"

    @property
    def color(self):
        """
        
        """
        return self._color
    
    
class SnakeHead(Object):
    
    def __init__(self):
        """
        
        """
        self._color = (0, 255, 0)
    
    def interaction(self, board_instance):
        board_instance.increase_length()
    
    def __repr__(self):
        return "o"

    @property
    def color(self):
        """
        
        """
        return self._color

    
class SnakeTail(Object):
    
    def __init__(self):
        """
        
        """
        self._color = (0, 255, 0)
    
    def interaction(self, board_instance):
        board_instance.game_over()
    
    def __repr__(self):
        return "■"

    @property
    def color(self):
        """

        """
        return self._color
