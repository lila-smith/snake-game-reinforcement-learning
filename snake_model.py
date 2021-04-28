import math
import random

class GameBoard:
    """
    Attributes:
    _board_array: a 2d list containing the one of objects Apple, Blank, Border, SnakeTail, or SnakeHead for each square of the board
    _snake_direction: current direction of motion
    _snake: list of snake positions
    _dimensions: the side length of the board
    _timestep: time for snake to move one block
    Maybe move to main.py
    """

    def __init__(self, side):
        """
        """
        self._side = side
        self._direction = [-1, 0] #Delta row, delta column
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

    def change_direction(self, direction):
        self._direction = direction

    def check_next_square(self):
        snake_head = self._snake[0]
        self.board_array[(snake_head[0] + self.direction[0])] \
                        [(snake_head[1] + self.direction[1])] \
                        .interaction(self)

    def maintain_velocity(self):
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
        blank_indexes = []
        for row_index, row in enumerate(self.board_array):
            for col_index, item in enumerate(row):
                if isinstance(item, Blank):
                    blank_indexes.append([row_index, col_index])
        chosen_square = random.choice(blank_indexes)
        self.mark_square(chosen_square[0], chosen_square[1], Apple())
    
    def game_over(self):
        pass
    
    def get_square(self, row, col):
        """
        """
        return self.board_array[row][col]
    
    def mark_square(self, row, col, object_type):
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
    
    _color = (255, 0, 0)
    
    def interaction(self, board_instance):
        board_instance.increase_length()
    
    def __repr__(self):
        return "@"
    
    @property
    def color(self):
        """
        
        """
        return (255, 0, 0)

    
class Blank(Object):
    
    _color = (255, 255, 255)
    
    def interaction(self, board_instance):
        board_instance.maintain_velocity()
    
    def __repr__(self):
        return " "
    
    @property
    def color(self):
        """
        
        """
        return (255, 255, 255)

    
class Border(Object):
    
    _color = (0, 0, 0)
    
    def interaction(self, board_instance):
        board_instance.game_over()
    
    def __repr__(self):
        return "#"

    @property
    def color(self):
        """
        
        """
        return (0, 0, 0)
    
    
class SnakeHead(Object):
    
    _color = (0, 255, 0)
    
    def interaction(self, board_instance):
        board_instance.increase_length()
    
    def __repr__(self):
        return "o"

    @property
    def color(self):
        """
        
        """
        return (0, 255, 0)

    
class SnakeTail(Object):
    
    _color = (0, 255, 0)
    
    def interaction(self, board_instance):
        board_instance.increase_length()
    
    def __repr__(self):
        return "■"

    @property
    def color(self):
        """

        """
        return (0, 255, 0)
