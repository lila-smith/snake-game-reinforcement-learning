import sys
import pygame

class SnakePlayer:
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
    
    def get_input(self):
        """
        
        """
        pygame.init()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.board.change_direction([0, -1])
                if event.key == pygame.K_RIGHT:
                    self.board.change_direction([0, 1])
                if event.key == pygame.K_UP:
                    self.board.change_direction([-1, 0])
                if event.key == pygame.K_DOWN:
                    self.board.change_direction([1, 0])                    
        return