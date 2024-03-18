# CYOA-Champ

CYOA-Champ is a text-based adventure game where players can make choices that affect the outcome of the game. The game is built in Python and uses JSON files to store game data.

## Project Structure

The project is structured as follows:



## How to Play

To play the game, run the `main.py` script. This will start the game and present you with the first choice. Enter your choice to proceed through the game.

## Game Mechanics

The game uses a number of mechanics to create a dynamic and engaging experience:

- **Player Stats**: The player's stats are stored in `story/stats.json`. These stats are updated throughout the game based on the player's choices.
- **World**: The game world is defined in `story/world.json`. This file contains the different paths the player can take through the game.
- **Enemies**: The game's enemies are defined in `story/enemies.json`.

## Modifying the Game

You can modify the game by editing the JSON files. For example, you can add new paths to the game by adding new entries to `story/world.json`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
