import sys
import json
import os
import time
from utils.random_number_api import get_random_combination
from utils.feedback import calculate_feedback
from utils.countdown_timer import calculate_timer

# load config file 
def load_config ():
    # ensure file path works for cross-platform OS
    config_path = os.path.join("data", "config.json")
    with open(config_path, "r") as config_file:
      return json.load(config_file)
    
cfg = load_config()

def main():
    print(cfg["messages"]["welcome"])

    # difficulty level logic
    difficulty = input(cfg["messages"]["input_level"]).lower().strip()
    if difficulty not in ["easy", "medium", "hard"]:
        print(cfg["messages"]["invalid_input_level"])
        difficulty = "easy"
    
    # generate random combination
    try:
        combination = get_random_combination(difficulty)
        print (combination)
    except Exception as e:
        print(f"Error fetching random numbers: {e}")
        sys.exit(1)

    print(cfg["messages"]["start"])

    # start timer
    start_time = time.time()

    # starting rules    
    print(cfg["messages"]["rules"].format(num_digit=cfg["levels"][difficulty]["num_digit"], total_time=cfg["levels"][difficulty]["total_time"] // 60))
    
    attempts = cfg["levels"][difficulty]["max_attempts"]
    history = cfg["history"]
    
    # continuous loop to handle user input, display feedback, and track attempts
    while attempts > 0:
        # timer logic 
        remaining_time = calculate_timer(start_time, cfg["levels"][difficulty]["total_time"])
        if remaining_time == cfg["messages"]["timeout"]:
          print(f"{cfg["messages"]["timeout"]} The correct combination was {combination}")
          break
        else: print(remaining_time)

        print(f"\nYou have {attempts} attempts remaining.")
        
        # user input logic
        guess = input(cfg["messages"]["input"].format(num_digit=cfg["levels"][difficulty]["num_digit"])).strip()
        
        try:
            guess_list = list(map(int, guess.split()))
            if len(guess_list) != cfg["levels"][difficulty]["num_digit"] or any(num < 0 or num > 7 for num in guess_list):
                raise ValueError(cfg["messages"]["invalid_input"].format(num_digit=cfg["levels"][difficulty]["num_digit"]))
        except ValueError as ve:
            print(ve)
            continue
        
        feedback = calculate_feedback(guess_list, combination, cfg["levels"][difficulty]["num_digit"])
        history.append({"guess": guess_list, "feedback": feedback})
        
        print(f"Feedback: {feedback}")
        if feedback == f"{cfg["levels"][difficulty]["num_digit"]} correct numbers and {cfg["levels"][difficulty]["num_digit"]} correct locations":
            print(cfg["messages"]["correct_guess"])
            break
        
        attempts -= 1
    
        if attempts == 0:
          print(f"\n{cfg["messages"]["game_over"]}{combination}")
    
        print("\nGuess History:")
        for entry in history:
          print(f"Guess: {entry["guess"]} | Feedback: {entry["feedback"]}")

if __name__ == "__main__":
    main()
