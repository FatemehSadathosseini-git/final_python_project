"""
Author: Fatemeh Sadat Hosseini
Date: 2025-03-10
Purpose: Main entry point for the text adventure game.
"""
from engine import GameEngine
from player import Player
import nltk

# Ensure required NLTK datasets are available
def download_nltk_data():
    """Downloads necessary NLTK datasets if not already installed."""
    required_datasets = ["names", "reuters", "punkt", "wordnet", "punkt_tab"]
    for dataset in required_datasets:
        nltk.download(dataset, quiet=True)  # Suppress output for a cleaner experience

# Download data before starting the game
download_nltk_data()


def main():

    print("Welcome to 'A Semester as a Text Adventure'!")

    # Initialize Player
    tutor = Player()

    # Start Game Engine
    game = GameEngine(tutor)
    game.run()


if __name__ == "__main__":
    main()