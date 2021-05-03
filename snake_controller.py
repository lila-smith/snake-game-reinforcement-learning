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
        

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not self.board.direction == [0,1]:
                self.board.change_direction([0, -1])
            if event.key == pygame.K_RIGHT and not self.board.direction == [0,-1]:
                self.board.change_direction([0, 1])
            if event.key == pygame.K_UP and not self.board.direction == [1,0]:
                self.board.change_direction([-1, 0])
            if event.key == pygame.K_DOWN and not self.board.direction == [-1,0]:
                self.board.change_direction([1, 0])                    
        return