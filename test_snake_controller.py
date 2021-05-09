"""
This module deals with testing some of the functions in the snake_controller
module.
"""
import pytest
import pygame
from snake_controller import SnakePlayer, get_restart_input, check_input_list
from snake_model import GameBoard


GET_INPUT_CASES = [
    (pygame.K_DOWN, [1, 0]),  # Check that down-arrow key changes
    # snake direction to down
    (pygame.K_UP, [-1, 0]),  # Check that up-arrow key changes
    # snake direction to up
    (pygame.K_RIGHT, [0, 1]),  # Check that right-arrow key changes
    # snake direction to right
    (pygame.K_LEFT, [0, -1]),  # Check that left-arrow key changes
    # snake direction to left
    (pygame.K_SPACE, [0, 0]),  # Check that non-arrow key does not
    # change direction
]


@pytest.mark.parametrize("test_input,expected", GET_INPUT_CASES)
def test_get_input(test_input, expected):
    """
    Adds given key press to event queue and checks snake direction is expected.

    Args:
        test_input: A pygame key constant.
        expected: A list of two integers that signify a direction (row, col).
    """
    # Set up GameBoard and
    pygame.init()
    board = GameBoard(11)
    controller = SnakePlayer(board)
    pygame.event.clear()
    newevent = pygame.event.Event(
        pygame.KEYDOWN, key=test_input)  # create the event
    pygame.event.post(newevent)  # add the event to the queue
    controller.get_input()
    assert board.direction == expected


CHECK_INPUT_LIST_CASES = [
    ([], False),  # Check that empty event queue returns False
    ([pygame.KEYDOWN], True),  # Check that single KEYDOWN event returns True
    ([pygame.KEYUP], False),  # Check that single non-KEYDOWN event returns False
    ([pygame.KEYDOWN, pygame.KEYUP], True),  # Check that two events, with
    # one KEYDOWN first, returns True
    ([pygame.KEYUP, pygame.KEYDOWN], True),  # Check that two events, with
    # one KEYDOWN second, returns True
    ([pygame.MOUSEWHEEL, pygame.KEYUP], False),  # Check that two events, with
    # no KEYDOWN, returns False
    ([pygame.KEYDOWN, pygame.KEYDOWN], True),  # Check that two KEYDOWN events
    # return True
]


@pytest.mark.parametrize("test_input,expected", CHECK_INPUT_LIST_CASES)
def test_check_input_list(test_input, expected):
    """
    Manually add pygame events to an event queue to test that the function
    check_input_list recognizes keydown events.

    Args:
        test_input: a list of pygame events to be added to the queue
        expected: a boolean value indicating if there is a keydown event
    """
    pygame.init()
    pygame.event.clear()
    for event in test_input:
        newevent = pygame.event.Event(event)  # create the event
        pygame.event.post(newevent)  # add the event to the queue
    assert check_input_list(pygame.KEYDOWN) == expected


GET_RESTART_INPUT_CASES = [
    (pygame.K_y, True),  # Check that function returns True when y is pressed
    (pygame.K_SPACE, None),  # Check that other keys return None
]


@pytest.mark.parametrize("test_input,expected", GET_RESTART_INPUT_CASES)
def test_restart_input_cases(test_input, expected):
    """
    Simulates a key pressed and checks that get_restart_input is as expected.

    Args:
        test_input: A pygame key constant.
        expected: Return from get_restart_input (Boolean or None)
    """
    pygame.init()
    pygame.event.clear()
    newevent = pygame.event.Event(
        pygame.KEYDOWN, key=test_input)  # create the event
    pygame.event.post(newevent)  # add the event to the queue
    assert get_restart_input() == expected
