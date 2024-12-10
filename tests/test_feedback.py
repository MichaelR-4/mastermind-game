# saving history, if combination has been prevously selected return a mesasge of "hey this took you x amount of attempts to solve last time"
# saving memory to disk 
# making sure I can continue or exit the game manually 

import pytest
from utils.feedback import calculate_feedback

@pytest.mark.parametrize(
    "guess, combination, num, expected_feedback",
    [
        # Test case: All correct
        ([1, 2, 3, 4], [1, 2, 3, 4], 4, "4 correct numbers and 4 correct locations"),
        
        # Test case: Some correct positions and numbers
        ([1, 2, 3, 5], [1, 2, 3, 4], 4, "3 correct numbers and 3 correct locations"),
        
        # Test case: Only correct numbers, no correct positions
        ([4, 3, 2, 1], [1, 2, 3, 4], 4, "4 correct numbers and 0 correct locations"),
        
        # Test case: All incorrect
        ([5, 6, 7, 8], [1, 2, 3, 4], 4, "All incorrect"),
        
        # Test case: Duplicate numbers in guess, unique in combination
        ([1, 1, 2, 3], [1, 2, 3, 4], 4, "3 correct numbers and 1 correct locations"),
        
        # Test case: Combination has duplicates, guess doesn't
        ([1, 2, 3, 4], [1, 1, 2, 3], 4, "3 correct numbers and 1 correct locations"),
        
        # Test case: Combination and guess have duplicates
        ([1, 1, 2, 2], [1, 2, 2, 3], 4, "3 correct numbers and 2 correct locations"),
    ],
)
def test_calculate_feedback_easy(guess, combination, num, expected_feedback):
    assert calculate_feedback(guess, combination, num) == expected_feedback

@pytest.mark.parametrize(
    "guess, combination, num, expected_feedback",
    [
        # Test case: All correct
        ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 6, "6 correct numbers and 6 correct locations"),
        
        # Test case: Some correct positions and numbers
        ([1, 2, 3, 5, 0, 4], [1, 2, 3, 5, 2, 7], 6, "4 correct numbers and 4 correct locations"),
        
        # Test case: Only correct numbers, no correct positions
        ([4, 3, 2, 1, 5, 6], [1, 2, 4, 3, 0, 7], 6, "4 correct numbers and 0 correct locations"),

        # Test case: All incorrect
        ([2, 5, 5, 6, 7, 2], [0, 0, 1, 3, 4, 4], 4, "All incorrect"),
        
        # Test case: Duplicate numbers in guess, unique in combination
        ([1, 1, 2, 2, 3, 5], [1, 2, 3, 4, 5, 6], 6, "4 correct numbers and 1 correct locations"),
        
        # Test case: Combination has duplicates, guess doesn't
        ([1, 2, 3, 4, 5, 6], [4, 4, 0, 0, 1, 2], 6, "3 correct numbers and 0 correct locations"),
        
        # Test case: Combination and guess have duplicates
        ([1, 4, 2, 2, 3, 3], [1, 2, 2, 3, 0, 0], 6, "4 correct numbers and 2 correct locations"),
    ],
)
def test_calculate_feedback_medium(guess, combination, num, expected_feedback):
    assert calculate_feedback(guess, combination, num) == expected_feedback

@pytest.mark.parametrize(
    "guess, combination, num, expected_feedback",
    [
        # Test case: All correct
        ([1, 2, 3, 4, 5, 6, 7, 0], [1, 2, 3, 4, 5, 6, 7, 0], 8, "8 correct numbers and 8 correct locations"),
        
        # Test case: Some correct positions and numbers
        ([1, 2, 3, 5, 0, 4, 6, 7], [1, 2, 3, 5, 2, 1, 1, 4], 8, "5 correct numbers and 4 correct locations"),
        
        # Test case: Only correct numbers, no correct positions
        ([4, 3, 2, 1, 5, 6, 2, 3], [1, 2, 4, 3, 0, 7, 5, 4], 8, "5 correct numbers and 0 correct locations"),

        # Test case: All incorrect
        ([2, 5, 5, 4, 3, 2, 1, 4], [0, 0, 7, 0, 7, 0, 6, 7], 8, "All incorrect"),
        
        # Test case: Duplicate numbers in guess, unique in combination
        ([1, 1, 2, 2, 3, 5, 5, 0], [1, 2, 3, 4, 5, 6, 7, 0], 8, "5 correct numbers and 2 correct locations"),
        
        # Test case: Combination has duplicates, guess doesn't
        ([1, 2, 3, 4, 5, 6, 7, 0], [4, 4, 0, 0, 1, 2, 3, 3], 8, "5 correct numbers and 0 correct locations"),
        
        # Test case: Combination and guess have duplicates
        ([1, 4, 2, 2, 3, 3, 6, 6], [1, 2, 2, 3, 0, 0, 6, 6], 8, "6 correct numbers and 4 correct locations"),
    ],
)
def test_calculate_feedback_hard(guess, combination, num, expected_feedback):
    assert calculate_feedback(guess, combination, num) == expected_feedback