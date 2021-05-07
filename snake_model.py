"""
This file outlines the GameBoard class that creates a model of the snake board
squares using a 2D list. It also includes the abstract class Object that's
inheritors are placed in the GameBoard to represent types of squares.
"""

from abc import ABC, abstractmethod
import math
import random


class GameBoard:
    """
    Snake game representation.

    Attributes:
    _end_condition: Boolean representation for if game is over.
    _board_array: 2D list containing the one of objects (Apple, Blank, Border,
                  or Snake) for each square of the board
    _size: An integer for side length of the board in squares.
    _snake: List of ordered Snake positions (from head to end of tail).
    _direction: A list for current direction of motion referring to
                _board_array indices.
    """

    def __init__(self, side):
        """
        Initializes GameBoard with Snake in center, a randomly spawned
        Apple, Border, and Blank instances.

        Args:
            side: An integer length of GameBoard. Includes borders.
        """
        self._end_condition = False
        self._size = side
        self._direction = [0, 0]  # Delta row, delta column
        self._board_array = [[Blank() for _ in range(self._size)]
                             for _ in range(self._size)]

        for index in range(0, self.size):
            for value in [0, self.size - 1]:
                self.mark_square([index, value], Border())
                self.mark_square([value, index], Border())

        snake_location = [math.ceil(self._size / 2), math.ceil(self._size / 2)]
        self._snake = [snake_location]
        self.mark_square(snake_location, Snake())

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
        return self._size

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
        snake_head = self.snake[0]
        if self.direction != [0, 0]:
            self.board_array[(snake_head[0] + self.direction[0])] \
            [(snake_head[1] + self.direction[1])].interaction(self)

    def maintain_velocity(self):
        """
        Moves snake one block forward.

        Removes last Snake entry and adds new Snake instance to front. 
        Interaction is called when next square is Blank instance.
        """
        # Set up rows and cols to access
        next_square = [(self.snake[0][0] + self.direction[0]),
                       (self.snake[0][1] + self.direction[1])]
        last_square = self._snake.pop()        
        # Mark appropriate squares
        self.mark_square(last_square, Blank())
        self.mark_square(next_square, Snake())
        # Update snake list
        self._snake = [next_square] + self._snake

    def increase_length(self):
        """
        Moves snake one block forward and increases length by one.

        Changes adds new Snake instance in front. Interaction is called when
        next square is Apple instance.
        """
        # Set up rows and cols to access
        next_square = [(self.snake[0][0] + self.direction[0]),
                       (self.snake[0][1] + self.direction[1])]
        # Mark appropriate squares
        self.mark_square(next_square, Snake())
        # Update snake list
        self._snake = [next_square] + self._snake
        # Make new apple
        self.spawn_apple()

    def spawn_apple(self):
        """
        Randomly chooses a Blank instance to turn into an Apple instance.
        """
        blank_indexes = []

        for row,col in enumerate(range(self.size)):
            if isinstance(self.get_square([row,col]), Blank):
                blank_indexes.append([row, col])

        chosen_square = random.choice(blank_indexes)
        self.mark_square(chosen_square, Apple())

    def game_over(self):
        """
        Ends game.

        Changes end condition to True. Interaction is called when next square
        is Border or Snake instance.
        """
        self._end_condition = True

    def get_square(self, location):
        """
        Returns the Object instance in specified row and column.

        Args:
            row: Integer less than _size for first index of _board_array.
            col: Integer less than _size for second index of _board_array.
        """
        return self.board_array[location[0]][location[1]]

    def mark_square(self, location, object_type):
        """
        Changes the Object in specified row and column.

        Args:
            row: Integer less than _size for first index of _board_array.
            col: Integer less than _size for second index of _board_array.
            object_type: An instance of inheritor of Object.
        """
        self._board_array[location[0]][location[1]] = object_type


class Object(ABC):
    """
    Object instances fill the squares of 2D-list _board_array in GameBoard.

    Attributes:
        _color: Tuple with three integers between 0 and 255. Format: (R, G, B)
    """
    def __init__(self):
        self._color = (0,0,0)

    @abstractmethod
    def interaction(self, board_instance):
        """
        Calls snake's next move on the GameBoard instance.
        """

    @property
    @abstractmethod
    def color(self):
        """

        """


class Apple(Object):
    """
    Apple is an Object in 2D-list _board_array in GameBoard.

    There is one apple per GameBoard instance at a time. When the apple is
    consumed, a new one will be spawned. Interacting with the apple increases
    the snake's length by one.

    Attributes:
        _color: Tuple with three integers between 0 and 255. Format: (R, G, B)
    """

    def __init__(self):

        """
        Create a new instance of Apple.
        """
        super().__init__()
        self._color = (255, 0, 0)

    def interaction(self, board_instance):
        """
        Calls snake's next move on the GameBoard instance.

        An Apple will increase the snake length.
        """
        board_instance.increase_length()

    def __repr__(self):
        """
        Return a string with the character representing Apple.
        """
        return "@"

    @property
    def color(self):
        """
        Return the tuple (R, G, B) for Apple color.
        """
        return self._color


class Blank(Object):
    """
    Blank is an Object in squares of 2D-list _board_array in GameBoard.

    Attributes:
        _color: Tuple with three integers between 0 and 255. Format: (R, G, B)
    """

    def __init__(self):
        """
        Create a new instance of Blank.
        """
        super().__init__()
        self._color = (255, 255, 255)

    def interaction(self, board_instance):
        """
        Calls snake's next move on the GameBoard instance.

        A Blank will maintain snake's trajectory.
        """
        board_instance.maintain_velocity()

    def __repr__(self):
        """
        Return a string with the character representing Blank.
        """
        return " "

    @property
    def color(self):
        """
        Return the tuple (R, G, B) for Blank color.
        """
        return self._color


class Border(Object):
    """
    Border is an Object in 2D-list _board_array in GameBoard.

    All edges of the board (i.e. items with index that is 0 or size - 1) are
    Border instances. Interacting with a Border ends the game.

    Attributes:
        _color: Tuple with three integers between 0 and 255. Format: (R, G, B)
    """

    def __init__(self):
        """
        Create a new instance of Border.
        """
        super().__init__()
        self._color = (0, 0, 0)

    def interaction(self, board_instance):
        """
        Calls snake's next move on the GameBoard instance.

        A Border will end the game.
        """
        board_instance.game_over()

    def __repr__(self):
        """
        Return a string of the character representing Border.
        """
        return "#"

    @property
    def color(self):
        """
        Return the tuple (R, G, B) for Border color.
        """
        return self._color


class Snake(Object):
    """
    Snake is an Object in 2D-list _board_array in GameBoard.

    The first Snake instance is spawned at the center of the board. From there,
    it will move and create more Snake instances when interacting with Apple. 
    Interacting with a Snake ends the game.

    Attributes:
        _color: Tuple with three integers between 0 and 255. Format: (R, G, B)
    """
    def __init__(self):
        """
        Create a new instance of Snake.
        """
        super().__init__()
        self._color = (0, 255, 0)

    def interaction(self, board_instance):
        """
        Calls snake's next move on the GameBoard instance.
        
        A Snake will end the game.
        """
        board_instance.game_over()

    def __repr__(self):
        """
        Return a string of the character representing Snake.
        """
        return "■"

    @property
    def color(self):
        """
        Return the tuple (R, G, B) for Snake color.
        """
        return self._color
