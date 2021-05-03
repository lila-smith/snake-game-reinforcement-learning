import sys
import pygame

class SnakePlayer:
    """
    
    """
    key_value = {
        pygame.K_LEFT: [0, -1],
        pygame.K_RIGHT: [0, 1],
        pygame.K_UP: [-1,0],
        pygame.K_DOWN: [1,0],
    }


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
                try:
                    if self.board.snake_length == 1 or \
                    not self.board.direction == -1 * self.key_value[event.key]:
                        self.board.change_direction(self.key_value[event.key])
                except:
                    continue                
        return