def calculate_feedback(guess, combination, num):
    # logic to determine correct positions 
    correct_positions = sum(1 for g, c in zip(guess, combination) if g == c)
    # logic to determine correct numbers
    correct_numbers = sum(min(guess.count(n), combination.count(n)) for n in set(guess))
    # track of correct numbers and correct positions 
    correct_only_numbers = correct_numbers - correct_positions

    if correct_positions == num:
        return True
    elif correct_only_numbers > 0 or correct_positions > 0:
        return f"{correct_numbers} correct numbers and {correct_positions} correct locations"
    else:
        return False 
