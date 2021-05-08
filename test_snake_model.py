"""
This module deals with testing some of the functions in the snake_model
module.
"""
import pytest
from snake_model import GameBoard, Apple, Blank, Border, Snake

CHANGE_DIRECTION_CASES = [
    ([1, 0],[1, 0]), # changing direction to down updates attribute to down
    ([0, -1],[0, -1]), # changing direction to left updates attribute to left
    ([0, 1],[0, 1]), # changing direction to right updates attribute to right
]

@pytest.mark.parametrize("test_input,expected", CHANGE_DIRECTION_CASES)
def test_change_direction(test_input, expected):
    """
    Test that using the change_direction method correctly updates the direction
    attribute.
    
    Test cases are commented next to the variable CHANGE_DIRECTION_CASES
    """
    test_board = GameBoard(10)
    test_board.change_direction(test_input)
    
    assert test_board.direction == expected
    
GET_SQUARE_CASES = [
    ([0, 4],"#"), # the fifth item in the first row is a border object
    ([5, 5],"■"), # the starting position of the snake on a board of size 10
]

@pytest.mark.parametrize("test_input,expected", GET_SQUARE_CASES)
def test_get_square(test_input, expected):
    """
    Test that using the get_square method correctly retrieves the status of
    know squares at the start of the game.
    
    Test cases are commented next to the variable GET_SQUARE_CASES
    """
    test_board = GameBoard(10)
    
    assert str(test_board.get_square(test_input)) == expected

MARK_SQUARE_CASES = [
    ([[1, 1], Apple()],"@"), # mark an apple at [1,1] correctly
    ([[4, 3], Snake()],"■"), # mark a snake at [4,3] correctly
]
    
@pytest.mark.parametrize("test_input,expected", MARK_SQUARE_CASES)
def test_mark_square(test_input, expected):
    """
    Test that manually marking the board using the mark_square method correctly
    updates the board.
    
    Test cases are commented next to the variable MARK_SQUARE_CASES
    """
    test_board = GameBoard(10)
    test_board.mark_square(test_input[0], test_input[1])
    
    assert str(test_board.get_square(test_input[0])) == expected
    
INCREASE_LENGTH_CASES = [
    (0,1), # increasing the length zero times yeilds a snake of length 1
    (1,2), # increasing the length one time yeilds a snake of length 2
    (2,3), # increasing the length two times yeilds a snake of length 3
]

@pytest.mark.parametrize("test_input,expected", INCREASE_LENGTH_CASES)
def test_increase_length(test_input, expected):
    """
    Test that increasing the length of the snake a certain number of times
    using the method increase_length yeilds the correct snake length.
    
    Test cases are commented next to the variable INCREASE_LENGTH_CASES
    """
    test_board = GameBoard(10)
    test_board.change_direction([-1, 0])
    
    counter = test_input
    while counter > 0:
        test_board.increase_length()
        counter -= 1
        
    assert len(test_board.snake) == expected

GAME_OVER_CASES = [
    (False,False), # not calling game_over means that the attribute stays False
    (True,True), # calling game_over switches the attribute to True
]

@pytest.mark.parametrize("test_input,expected", GAME_OVER_CASES)
def test_game_over(test_input, expected):
    """
    Test that the method game_over changes the GameBoard attribute
    '_end_condition' to True, and that the attribute is False otherwise.
    
    Test cases are commented next to the variable INCREASE_LENGTH_CASES
    """
    test_board = GameBoard(10)
    
    if test_input:
        test_board.game_over()
        
    assert test_board.end_condition == expected
    
MAINTAIN_VELOCITY_CASES = [
    ([([-1, 0], 2)],[[3,5]]), # move the snake up two steps and check location
    ([([-1, 0], 2), ([0, -1], 3)],[[3,2]]), # move snake in 2 directions
]

@pytest.mark.parametrize("test_input,expected", MAINTAIN_VELOCITY_CASES)
def test_maintain_velocity(test_input, expected):
    """
    Test that the method maintain_velocity keeps the snake moving in a straight
    line.
    
    Test cases are commented next to the variable MAINTAIN_VELOCITY_CASES
    """
    test_board = GameBoard(10)
    
    # clear randomly spawned apple
    for row_index, row in enumerate(test_board.board_array):
        for col_index, item in enumerate(row):
            if isinstance(item, Apple):
                test_board.mark_square([row_index, col_index], Blank())
    
    # move snake as indicated by test_input
    for dir_step_pair in test_input:
        direction = dir_step_pair[0]
        test_board.change_direction(direction)
        num_steps = dir_step_pair[1]
        
        while num_steps > 0:
            test_board.maintain_velocity()
            num_steps -= 1
            
    assert test_board.snake == expected

# the first two cases are the same as maintain_velocity, because 
# check_next_square is a more general version of maintain_velocity
# the third case checks that the length is increased when it eats an apple
# the fourth case check that the end condition is triggered when hitting a wall
CHECK_NEXT_SQUARE_CASES = [
    # general structure:
    # ([([direction], num steps)...],[[snake list], end condition])
    ([([-1, 0], 2)],[[[3,5]], False]),
    ([([-1, 0], 2), ([0, -1], 3)],[[[3,2]], False]),
    ([([-1, 0], 2), ([0, -1], 3), ([-1, 0], 1)],[[[2,2], [3,2]], False]),
    ([([0, -1], 5)],[[[5,1]], True]),
]

@pytest.mark.parametrize("test_input,expected", CHECK_NEXT_SQUARE_CASES)
def test_check_next_square(test_input, expected):
    """
    Test that the check_next_square method completes the appropriate
    interaction with the square in front of the snake.
    
    Test cases are commented above the variable CHECK_NEXT_SQUARE_CASES
    """
    test_board = GameBoard(10)
    
    # clear randomly spawned apple and mark one in a known location
    for row_index, row in enumerate(test_board.board_array):
        for col_index, item in enumerate(row):
            if isinstance(item, Apple):
                test_board.mark_square([row_index, col_index], Blank())
    test_board.mark_square([2, 2], Apple())
    
    # move snake as indicated by test_input
    for dir_step_pair in test_input:
        direction = dir_step_pair[0]
        test_board.change_direction(direction)
        num_steps = dir_step_pair[1]
        
        while num_steps > 0:
            test_board.check_next_square()
            num_steps -= 1
            
    assert [test_board.snake, test_board.end_condition] == expected
            