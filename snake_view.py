from abc import ABC, abstractmethod
import pygame

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
    
    def draw(self):
        """
        
        """
        pygame.init()
        
        scale_factor = 30
        screen_width = self.board.size * scale_factor
        screen_height = self.board.size * scale_factor
        
        screen = pygame.display.set_mode((screen_width, screen_height))
        
        
        for row_index, row in enumerate(self.board.board_array):
            for col_index, item in enumerate(row):
                pygame.draw.rect(screen, (255, 255, 255), (row_index * 10, col_index * 10, scale_factor, scale_factor))
        
        pygame.display.flip()
        
        