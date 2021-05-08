"""
This module deals with testing some of the functions in the snake_model
module.
"""
import pytest
from snake_model import GameBoard, Apple, Blank, Border, Snake

CHANGE_DIRECTION_CASES = [
    ([1, 0],[1, 0]),
    ([0, -1],[0, -1]),
    ([1, 1],[1, 1]),
]

@pytest.mark.parametrize("test_input,expected", CHANGE_DIRECTION_CASES)
def test_change_direction(test_input, expected):
    """
    
    """
    test_board = GameBoard(10)
    test_board.change_direction(test_input)
    
    assert test_board.direction == expected
    
GET_SQUARE_CASES = [
    ([0, 4],"#"),
    ([5, 5],"■"),
]

@pytest.mark.parametrize("test_input,expected", GET_SQUARE_CASES)
def test_get_square(test_input, expected):
    """
    
    """
    test_board = GameBoard(10)
    
    assert str(test_board.get_square(test_input)) == expected

MARK_SQUARE_CASES = [
    (,),
    (,),
]
    
@pytest.mark.parametrize("test_input,expected", MARK_SQUARE_CASES)
def test_mark_square(test_input, expected):
    """
    
    """
    
