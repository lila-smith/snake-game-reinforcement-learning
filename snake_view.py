"""
This module contains the view for the snake game, which is an abstract base
class called SnakeView, from which the TextView and PygameView classes inherit.
It includes methods for drawing the board to the screen and drawing the game
over screen.
"""

from abc import ABC, abstractmethod
from math import ceil, floor
import pygame


class SnakeView(ABC):
    """
    Abstract base class for the gameboard view that is used for visualizing
    the gameboard

    Attributes:
        _board: an instance of the GameBoard class
    """

    def __init__(self, board_instance):
        """
        Initialize the view with the gameboard that will be visualized

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

    @abstractmethod
    def draw(self):
        """
        Abstract method for drawing the board to the screen - will be
        overwritten in specific child classes

        Args:
            None
        Returns:
            No return value
        """

    @abstractmethod
    def draw_gameover(self):
        """
        Abstract method for drawing the gameover screen - will be overwritten
        in specific child classes

        Args:
            None
        Returns:
            No return value
        """


class TextView(SnakeView):
    """
    Class for printing a text-based gameboard to the screen, which inherits
    from SnakeView

    Attributes:
        _board: an instance of GameBoard
    """

    def draw(self):
        """
        Print the gameboard to the screen using text-based visualization

        Args:
            None
        Returns:
            No return value
        """
        print(self.board)


class PygameView(SnakeView):
    """
    Class for displaying the gameboard using a pygame screen, which inherits
    from SnakeView

    Attributes:
        _board: an instance of GameBoard
        _scale_factor: an int representing side dimension, in pixels, of the
        objects on the pygame screen
        _screen_size: an tuple representing the dimensions of the pygame
        screen, in pixels
        _screen: a pygame surface
        _buffer: an int controlling the color gradient of the snake
        _eye_color: a tuple for the RGB value of the snake's eyes
        _eye_size: an int representing the size of the snake's eyes
        _padding: an int representing the dist. the snake's eyes are from the
        edge of the head
    """

    def __init__(self, board_instance):
        """
        Initialize the pygame view using the gameboard that will be visualized
        and set up the pygame screen dimensions and snake colors

        Args:
            board_instance: a gameboard
        Returns:
            No return value
        """
        super().__init__(board_instance)

        self._scale_factor = 30
        self._screen_size = self.board.size * \
            self._scale_factor, self.board.size * self._scale_factor
        self._screen = pygame.display.set_mode(self._screen_size)

        self._buffer = 20  # Higher buffer means lighter snake in general
        self._eye_color = (200, 200, 0)
        self._eye_size = .125
        self._padding = .2

    @property
    def scale_factor(self):
        """
        Return the scale factor, which is a private attribute

        Args:
            None
        Returns:
            self._scale_factor: an int representing the scale factor
        """
        return self._scale_factor

    @property
    def screen(self):
        """
        Return the screen surface, which is a private attribute

        Args:
            None
        Returns:
            self._screen: the pygame screen
        """
        return self._screen

    @property
    def buffer(self):
        """
        Return the value for buffer, which is a private attribute

        Args:
            None
        Returns:
            self._buffer: an int controlling the color of the snake
        """
        return self._buffer

    @property
    def eye_color(self):
        """
        Return the tuple for eye color, which is a private attribute

        Args:
            None
        Returns:
            self._eye_color: a tuple for the RGB value for the snake's eyes
        """
        return self._eye_color

    @property
    def eye_size(self):
        """
        Return the value for eye size, which is a private attribute

        Args:
            None
        Returns:
            self._eye_size: an int representing the size of the snake's eyes
        """
        return self._eye_size

    @property
    def padding(self):
        """
        Return the value for padding, which is a private attribute

        Args:
            None
        Returns:
            self._padding: an int representing the distance the snake's eyes
            are from the edge of the head
        """
        return self._padding

    def draw(self):
        """
        Draw the current state of the board to the screen and update the screen

        Args:
            None
        Returns:
            None
        """
        for row_index, row in enumerate(self.board.board_array):
            for col_index, item in enumerate(row):
                pygame.draw.rect(self.screen, item.color, pygame.Rect(
                    col_index * self.scale_factor,
                    row_index * self.scale_factor, self.scale_factor,
                    self.scale_factor))

        for index, square in enumerate(self.board.snake):
            item = self.board.get_square(square)
            color_factor = (index + self.buffer / 2) / \
                (self.board.snake_length + self.buffer)
            color = [item.color[0], item.color[1], item.color[2]]
            color = [color_factor * value for value in color]
            pygame.draw.rect(self.screen, color, pygame.Rect(
                square[1] * self.scale_factor,
                square[0] * self.scale_factor, self.scale_factor,
                self.scale_factor))

        head_row = self.board.snake[0][0]
        head_col = self.board.snake[0][1]
        direction_ver = self.board.direction[0]
        direction_hor = self.board.direction[1]
        if direction_hor != 0:
            x_ver = ceil((head_col + 0.5 - self.eye_size + 0.125 *
                          direction_hor) * self.scale_factor)
            y_ver = ceil((head_row + self.padding) * self.scale_factor)
            pygame.draw.rect(self.screen, self.eye_color,
                             (x_ver,
                              y_ver,
                              ceil(self.scale_factor * self.eye_size),
                                 ceil(self.scale_factor * self.eye_size)))
            pygame.draw.rect(self.screen, self.eye_color,
                             (x_ver,
                              y_ver + (1 - 3 * self.padding) *
                              self.scale_factor,
                                 ceil(self.scale_factor * self.eye_size),
                                 ceil(self.scale_factor * self.eye_size)))
        elif direction_ver != 0:
            x_ver = ceil((head_col + self.padding) * self.scale_factor)
            y_ver = ceil((head_row + .5 - self.eye_size + self.padding *
                          direction_ver) * self.scale_factor)
            pygame.draw.rect(self.screen, self.eye_color,
                             (x_ver,
                              y_ver,
                              ceil(self.scale_factor * self.eye_size),
                                 ceil(self.scale_factor * self.eye_size)))
            pygame.draw.rect(self.screen, self.eye_color,
                             (x_ver + (1 - 3 * self.padding) * self.scale_factor,
                              y_ver,
                              ceil(self.scale_factor * self.eye_size),
                                 ceil(self.scale_factor * self.eye_size)))

        pygame.display.flip()

    def draw_gameover(self):
        """
        Draw the gameover screen to the pygame surface and update the screen

        Args:
            None
        Returns:
            No return value
        """
        line_1_location = self.scale_factor * self.board.size / \
            2, self.scale_factor * self.board.size / 4
        line_2_location = self.scale_factor * \
            self.board.size / 2, line_1_location[1] + 50
        line_3_location = self.scale_factor * self.board.size / \
            2, self.scale_factor * self.board.size / 2

        font_game_over = pygame.font.SysFont(None, 70)
        font_text = pygame.font.SysFont(None, 35)

        end_msg_line_1 = font_game_over.render("GAME OVER", True, (255, 0, 0))
        end_msg_line_2 = font_text.render(
            f"Your final length was {self.board.snake_length}", True, (255, 0, 0))
        restart_msg = font_text.render("Restart? ( y / n )", True, (255, 0, 0))

        self.screen.fill((0, 0, 0))

        self.screen.blit(end_msg_line_1, end_msg_line_1.get_rect(
            center=line_1_location))
        self.screen.blit(end_msg_line_2, end_msg_line_2.get_rect(
            center=line_2_location))
        self.screen.blit(restart_msg, restart_msg.get_rect(
            center=line_3_location))

        pygame.display.flip()

    def start_text(self):
        """
        Draw the starting intstructions to the screen and update the screen

        Args:
            None
        Returns:
            No return value
        """
        location = self.scale_factor * self.board.size / \
            2, floor(self.board.size / 4 * self.scale_factor)

        font = pygame.font.SysFont(None, 30)

        start_text = font.render(
            "Press an Arrow Key to Start Moving", True, (0, 128, 0))
        text_background = start_text.get_rect(center=location)

        pygame.draw.rect(self.screen, (255, 255, 255), text_background)
        self.screen.blit(start_text, text_background)

        pygame.display.update()
