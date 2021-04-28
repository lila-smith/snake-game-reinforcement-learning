import math

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
                or col == 0 or row == self._side - 1:
                    self._board_array[row][col] = Border()
                elif row == col == math.ceil(self._side / 2):
                    self._board_array[row][col] = SnakeHead()
                    self._snake = [[row, col]]
                else:
                    self._board_array[row][col] = Blank()

    def __repr__(self):
        return self._board_array

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
        snake_head = self._snake[1]
        self.board_array[(snake_head[0] + self.direction[0])] \
                        [(snake_head[1] + self.direction[1])]

    def maintain_velocity(self):
        pass

    def increase_length(self):
        pass
    
    def spawn_apple(self):
        pass
    
    def game_over(self):
        pass
    
    def get_square(self, row, col):
        """
        
        """
        return self.board_array[row][col]
    

from abc import ABC, abstractmethod
class Object(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def interaction(self, board_instance):
        pass
    
    @property
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
        return _color

    
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
        return _color

    
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
        return _color
    
    
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
        return _color

    
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
        return _color
