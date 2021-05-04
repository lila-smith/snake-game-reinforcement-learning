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
    opposite = {
        pygame.K_LEFT: [0, 1],
        pygame.K_RIGHT: [0, -1],
        pygame.K_UP: [1,0],
        pygame.K_DOWN: [-1,0],
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


        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            try:
                if self.board.snake_length == 1 or \
                not self.board.direction == self.opposite[event.key]:
                    self.board.change_direction(self.key_value[event.key])
            except:
                pass
        return
    
    def check_to_exit(self):
        """
        
        """
        if pygame.event.peek(pygame.QUIT):
            sys.exit()