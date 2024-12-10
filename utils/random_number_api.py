import requests
import json
import os

# load config file 
def load_config ():
    # ensure file path works for cross-platform OS
    config_path = os.path.join("data", "config.json")
    with open(config_path, "r") as config_file:
      return json.load(config_file)
    
cfg = load_config()

API_URL = "https://www.random.org/integers"

def get_random_combination(difficulty_level):
    params = {
        "num": cfg["levels"][difficulty_level]["num_digit"],
        "min": 0,
        "max": 7,
        "col": 1,
        "base": 10,
        "format": "plain"
    }

    response = requests.get(API_URL, params=params)
       
    # check HTTP status code for any error
    response.raise_for_status()

    # validate api response
    response_text = response.text.strip()
    if not response_text:
        raise ValueError("API returned an invalid response")
       
    numbers = list(map(int, response.text.strip().split()))

    return numbers
