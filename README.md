# Higher or Lower Game - `famous.py`

This Python program is a simple "Higher or Lower" game where players compare two famous individuals based on their follower counts. The player must guess which individual has more followers. The game continues until the player guesses incorrectly, at which point the final score is displayed.

## Table of Contents

1. [Overview](#overview)
2. [How to Run the Program](#how-to-run-the-program)
3. [Game Rules](#game-rules)
4. [Dependencies](#dependencies)
5. [Sample Output](#sample-output)
6. [License](#license)

## Overview

The game randomly selects data from a dataset that contains information about famous personalities, including their name, description, country, and follower count. Two individuals are displayed for comparison, and the player must guess which one has a higher follower count.

If the guess is correct, the player’s score increases by 1, and the game continues with a new pair of individuals. If the guess is incorrect, the game ends, and the player’s final score is displayed.

## How to Run the Program

1. **Ensure you have Python installed**: The program requires Python 3.x to run.
2. **Clone the repository**: Clone the entire folder containing `famous.py` and `data.py` using the command below:

    ```bash
    git clone https://github.com/Pooja389/famous_game.git
    ```

3. **Navigate to the cloned folder**:

    ```bash
    cd famous_game
    ```

4. **Run the program**:

    ```bash
    python famous.py
    ```

5. **Follow the prompts**: The program will ask you to choose between "A" or "B" for each comparison. Type your choice and press Enter.

## Game Rules

1. Two individuals are shown on the screen with their descriptions and country.
2. The player must guess which individual has a higher follower count by typing `A` or `B`.
3. If the guess is correct, the player earns 1 point and a new pair of individuals is shown.
4. If the guess is incorrect, the game ends, and the final score is displayed.

## Dependencies

The program uses the following built-in Python modules:
- `random`: Used to randomly select individuals from the dataset.
  
Ensure that both `famous.py` and `data.py` are present in the same directory.
