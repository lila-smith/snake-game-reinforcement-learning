"""
This module deals with testing some of the functions in the snake_controller
module.
"""
import pytest, sys, pygame
from snake_controller import SnakePlayer
from snake_model import GameBoard


GET_INPUT_CASES = [
    (pygame.K_DOWN,[1,0]), # Check that down-arrow key changes 
                           # snake direction to down
    (pygame.K_UP,[-1,0]), # Check that up-arrow key changes 
                          # snake direction to up
    (pygame.K_RIGHT,[0,1]), # Check that right-arrow key changes
                            # snake direction to right
    (pygame.K_LEFT,[0,-1]), #Check that left-arrow key changes
                            # snake direction to left
    (pygame.K_SPACE,[0,0]), # Check that non-arrow key does not
                            # change direction                       
]

@pytest.mark.parametrize("test_input,expected", GET_INPUT_CASES)
def test_get_input(test_input, expected):
    """
    Adds given key press to event queue and checks snake direction is expected.

    Args:
        test_input: A pygame key
    """
    # Set up GameBoard and 
    pygame.init()
    board = GameBoard(11)
    controller = SnakePlayer(board)
    pygame.event.clear()
    newevent = pygame.event.Event(pygame.KEYDOWN, key=test_input) #create the event
    pygame.event.post(newevent) #add the event to the queue
    controller.get_input()
    assert board.direction == expected
