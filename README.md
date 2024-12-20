# Mastermind Game with Extensions

## Overview

This project implements a "Mastermind" game where a player attempts to guess a 4-digit combination generated by the computer. The game provides feedback on the player's guesses to guide them toward the correct combination. Additionally, I have implemented three creative extensions:

1. **Countdown Timer**: Players have a total time limit to guess the correct combination.
2. **Difficulty Levels**: Players can choose from multiple difficulty levels, which adjust the number of attempts and complexity.
3. **Score Tracker**: User data is stored, tracking wins and losses between sessions.

## Project Features

- **Core Functionality**:

  - Random 4-digit combination generated using the Random.org API.
  - Feedback includes correct numbers and their positions.
  - Up to 10 attempts to guess the correct combination.

- **Extensions**:

  - **Countdown Timer**: Adds urgency by limiting the total time available to guess the combination based on difficulty level.
  - **Difficulty Levels**:
    - Easy: 10 attempts allowed, 4-digit combination, with a 20-minute time limit.
    - Medium: 8 attempts, 6-digit combination, with a 15-minute time limit.
    - Hard: 6 attempts, 8-digit combination, with a 10-minute time limit.
  - **Score Tracker**: Tracks user performance across games and persists data to a JSON file.

- **Testing and API Usage**:

  - Used `requests` library to interact with the Random.org API.
  - Added unit tests with `pytest` to ensure code reliability.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mastermind
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Install required dependencies:
   ```bash
   pip install pytest requests
   ```

## Running the Game

1. Launch the game:

   ```bash
   python main.py
   ```

2. Follow the prompts to:

   - Enter your username.
   - Select a difficulty level.
   - Make guesses within the total time limit.

3. Feedback will be provided for each guess. Win or lose, your score will be updated and saved.

## Testing

Run the tests using `pytest`:

```bash
pytest tests/<test_file_name>.py
```

## Thought Process

### Core Logic

The game uses the `calculate_feedback` function to determine feedback for each guess. This function ensures:

- Accurate feedback on correct numbers and positions.
- Logical differentiation between a win, partial correctness, and complete incorrectness.

### Extensions

- **Countdown Timer**:

  - Implemented using Python's `time` module.
  - The timer tracks the total time available for the game by repeatedly checking the remaining time after each guess. If the time runs out, the game ends.

- **Difficulty Levels**:

  - Adjusts game settings, including the number of attempts, the length of the combination to guess, and the total time limit for the game.

- **Score Tracker**:

  - Utilizes JSON files to persist user data.
  - Tracks and updates wins and losses seamlessly.

### Libraries Used

- `requests`: For API calls to Random.org.
- `pytest`: For unit testing game logic and api handling.

## Challenges and Solutions

- **Tracking Guesses and Validating Feedback**:

  - Developing the logic to compare the player's guesses with the generated number and provide feedback on correct numbers and positions was more complex than anticipated. It required methodical planning to ensure the logic was accurate and efficient, especially when handling edge cases.

- **Combining User Data Storage with Game Logic**:

  - Storing user guesses and game progress in a way that seamlessly integrated with the game logic proved challenging. Using JSON files for data persistence required careful structuring to ensure data could be efficiently read and updated.

- **Writing Tests for API and Game Logic**:

  - As the game logic became more intricate, writing unit tests for the API and validating game behavior became harder. It demanded creative approaches and unique methods to cover all scenarios.

### Solutions

- Used modular and clear logic to manage and validate user guesses effectively.
- Employed JSON for simplicity and human readability, ensuring data was saved and loaded seamlessly.
- Created extensive unit tests to ensure the game logic and API integration were reliable.

## Attempted Enhancements

- Add multiplayer functionality.
- Provide a graphical user interface (GUI).
- Persist continous playing

---
