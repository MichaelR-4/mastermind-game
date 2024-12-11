import sys
import json
import os
import time
from utils.random_number_api import get_random_combination
from utils.feedback import calculate_feedback
from utils.countdown_timer import calculate_timer
from utils.update_user_data import load_user_data, save_user_data,update_score

# load config file 
def load_config ():
    # ensure file path works for cross-platform OS
    config_path = os.path.join("data", "config.json")
    with open(config_path, "r") as config_file:
      return json.load(config_file)
    
cfg = load_config()

def main():
    print(cfg["messages"]["welcome"])

    # ask for username
    username = input(cfg["messages"]["username"]).strip()

    # check if user exists
    user_data = load_user_data(username)

    # Generate the appropriate message based on whether the user exists
    if user_data:  # User data exists
        print(f"Welcome back {username}! Your current score is {user_data['wins']} wins and {user_data['losses']} losses.")
    else:  # New user
        print(f"Welcome {username}! {cfg["messages"]["current_score"].format(wins=cfg["scoreboard"]["wins"], losses=cfg["scoreboard"]["losses"])}")
        # Initialize new user data
        user_data = cfg["scoreboard"]
        save_user_data(username, user_data)

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
        
        if feedback == True:
            update_score(user_data, is_win=True)
            save_user_data(username, user_data)
            print(cfg["messages"]["correct_guess"])
            break
        elif feedback is False:
            print(cfg["messages"]["incorrect_guess"])
        else: print(f"Feedback: {feedback}")
        
        attempts -= 1
    
        if attempts == 0:
          print(f"\n{cfg["messages"]["game_over"]}{combination}")
          update_score(user_data, is_win=False)
          save_user_data(username, user_data)
    
        print("\nGuess History:")
        for entry in history:
          print(f"Guess: {entry["guess"]} | Feedback: {entry["feedback"]}")

if __name__ == "__main__":
    main()
