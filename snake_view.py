from abc import ABC, abstractmethod
import pygame
from math import ceil, floor

class SnakeView(ABC):
    """
    
    """
    
    def __init__(self, board_instance):
        """
        
        """
        self._board = board_instance
        
    @property
    def board(self):
        """

        """
        return self._board
    
    @abstractmethod
    def draw(self):
        """
        
        """
        pass

    @abstractmethod
    def draw_gameover(self):
        """
        
        """
        pass

    
class TextView(SnakeView):
    """
    
    """
    
    def draw(self):
        """
        
        """
        print(self.board)
    
    
class PygameView(SnakeView):
    """
    
    """        
    
    def __init__(self, board_instance):
        """
        
        """
        super().__init__(board_instance)
        
        self._scale_factor = 30
        self._screen_size = self.board.size * self._scale_factor, self.board.size * self._scale_factor
        self._screen = pygame.display.set_mode(self._screen_size)
    
    @property
    def scale_factor(self):
        """
        
        """
        return self._scale_factor
    
    @property
    def screen(self):
        """
        
        """
        return self._screen
    
    def draw(self):
        """
        
        """   
        pygame.init()
        
        
        for row_index, row in enumerate(self.board.board_array):
            for col_index, item in enumerate(row):
                rect_temp = pygame.Rect(col_index * self.scale_factor, \
                                        row_index * self.scale_factor, \
                                        self.scale_factor, \
                                        self.scale_factor)
                pygame.draw.rect(self.screen, item.color, rect_temp)

        snake_length = self.board.snake_length
        buffer = 5
        for index, square in enumerate(self.board.snake):
            item = self.board.get_square(square[0], square[1])
            color_factor = (index + buffer / 2) / (snake_length + buffer)
            color = [item.color[0], item.color[1], item.color[2]]
            color = [color_factor * value for value in color]
            rect_temp = pygame.Rect(square[1] * self.scale_factor, \
                                        square[0] * self.scale_factor, \
                                        self.scale_factor, \
                                        self.scale_factor)
            pygame.draw.rect(self.screen, color, rect_temp)
        """
        head_row = self.board.snake_head[1]
        head_col = self.board.snake_head[0]
        direction_hor = self.board.snake[0][0]
        direction_ver = self.board.direction[0][1]
            if direction_ver == 0:
            pygame.draw.rect(self.screen, [0,0,0], \
                (ceil((head_col + 0.5 + direction_hor * 0.25) * self.scale_factor), \
                ceil((head_row + 0.5) * self.scale_factor), \
                ceil(self.scale_factor * 0.25), \
                ceil(self.scale_factor * 0.25)))
        """
        
        pygame.display.flip()

    def draw_gameover(self):
        """
        
        """
        line_1_location = self.scale_factor * self.board.size / 2, self.scale_factor * self.board.size / 4
        line_2_location = self.scale_factor * self.board.size / 2, line_1_location[1] + 50
        line_3_location = self.scale_factor * self.board.size / 2, self.scale_factor * self.board.size / 2
        
        font_game_over = pygame.font.SysFont(None, 70)
        font_text = pygame.font.SysFont(None, 35)
        
        end_msg_line_1 = font_game_over.render(f"GAME OVER", True, (255,0,0))
        end_msg_line_2 = font_text.render(f"Your final length was {self.board.snake_length}", True, (255, 0, 0))
        restart_msg = font_text.render("Restart? ( y / n )", True, (255, 0, 0))
        
        self.screen.fill((0,0,0))
        
        self.screen.blit(end_msg_line_1, end_msg_line_1.get_rect(center = line_1_location))
        self.screen.blit(end_msg_line_2, end_msg_line_2.get_rect(center = line_2_location))
        self.screen.blit(restart_msg, restart_msg.get_rect(center = line_3_location))
        
        pygame.display.flip()
        
    def start_text(self):
        """
        
        """
        location = self.scale_factor * self.board.size / 2, floor(self.board.size / 4 * self.scale_factor)
        
        font = pygame.font.SysFont(None, 30)
        
        start_text = font.render(f"Press an Arrow Key to Start Moving", True, (0, 128, 0))
        text_background = start_text.get_rect(center = location)

        pygame.draw.rect(self.screen, (255, 255, 255), text_background)
        self.screen.blit(start_text, text_background)
        
        pygame.display.update()
        