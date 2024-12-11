import json
import os

# load user data if it exists 
def load_user_data(username):
    file_path = os.path.join("data", f"{username}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        # Initialize data for new users
        return None

# save user data for new user
def save_user_data(username, user_data):
  file_path = os.path.join("data", f"{username}.json")
  with open(file_path, "w") as file:
     json.dump(user_data, file)

# update user score
def update_score(user_data, is_win):
    if is_win:
       user_data["wins"] += 1
    else:
       user_data["losses"] += 1
