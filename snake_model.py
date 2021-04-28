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
        self._board_array = [["" for _ in range(self._side)] \
                            for _ in range(self._side)]

        for row in range(self._side):
            for col in range(self._side):
                if row == 0 or row == self._side - 1 \
                or col == 0 or row == self._side - 1:
                    self._board_array[row][col] = Border(self._board_array)
                elif row == col == math.ceil(self._side / 2):
                    self._board_array[row][col] = SnakeHead(self._board_array)
                    self._snake = [[row, col]]
                else:
                    self._board_array[row][col] = Blank(self._board_array)

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
    
    def get_square(self):
        pass
    

from abc import ABC, abstractmethod
class Object(ABC):
    def __init__(self, board):
        self._board_array = board
    
    @abstractmethod
    def interaction(self):
        pass

class Apple(Object):
    def interaction(self):
        self._board_array.increase_length()
    
    def __repr__(self):
        pass

class Blank(Object):
    def interaction(self):
        self._board_array.maintain_velocity()
    
    def __repr__(self):
        pass

class Border(Object):
    def interaction(self):
        self._board_array.game_over()
    
    def __repr__(self):
        pass

class SnakeHead(Object):
    def interaction(self):
        self._board_array.increase_length()
    
    def __repr__(self):
        pass

class SnakeTail(Object):
     def interaction(self):
        self._board_array.increase_length()
    
     def __repr__(self):
        pass

