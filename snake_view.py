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
                pygame.draw.rect(self.screen, item.color, (col_index * self.scale_factor, row_index * self.scale_factor, self.scale_factor, self.scale_factor))
        
        pygame.display.flip()
        
        