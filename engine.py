"""
Author: Fatemeh Sadat Hosseini
Date: 2025-02-04
Purpose: Defines the Player class and manages the player's state.
"""
import random
import time
from grading import Grading
from feedback import Feedback
from player import Player
from utils import load_descriptions



class GameEngine:
    def __init__(self, player):
        self.player = player
        self.state = "start"  # Initial game state
        self.grading = Grading(player)
        self.feedback = Feedback(player)
        self.descriptions = load_descriptions("data/description.csv")  # Load scene descriptions

        self.commands_by_state = {
            "start": ["grade", "inspect report", "exit", "delay grade"],
            "grading": ["grade", "delay grade", "inspect report", "exit"],
            "feedback_1": ["give feedback", "inspect report", "exit"],
            "feedback_2": ["give feedback", "inspect report", "exit"],
            "evaluation": ["get eval", "inspect report", "exit"],
            "finished": ["play again", "inspect report", "exit"],
            "defeat": ["play again", "inspect report", "exit"]
        }


    def run(self):
        """Main game loop with restart option after defeat."""
        con= True
        while con:


            self.display_scene()
            print("EP: ", self.player.energy)
            print("Evaluation: ", self.player.evaluation)
            command = input("> ").strip().lower()

            if command == "exit":
                print("Goodbye! See you next semester!")
                break

            con= self.process_command(command)


    def display_scene(self):
        """Prints the scene description and available commands based on current state."""
        print("\n" + self.descriptions.get(self.state, "Undefined state."))


    def process_command(self, command):
        """Handles user input and transitions game states, enforcing allowed commands."""
        # Ensure the command is valid for the current state
        if command not in self.commands_by_state.get(self.state, []):
            print(f"Invalid command in {self.state} state! Try again. {self.commands_by_state.get(self.state, [])}")
            return True



        elif command == "inspect report":
            self.player.show_report()
            return True

        else:
            if self.state == "start" or self.state == "grading":
                result = self.grading.grade(command)
                if result == "defeat":
                    self.state= "defeat"
                    return True
                elif result == "exit":
                    return False
                else:
                    self.state= result
                    return True


            elif "feedback" in self.state:
                result = self.feedback.process(command)
                if result == "defeat":
                    self.state = "defeat"
                elif result == "grading":
                    self.state = "grading"
                elif result == "evaluation":
                    self.state = "evaluation"
                else:
                    return False
                return True

            elif self.state == "evaluation":
                assert command == "get eval"
                self.player.get_evaluation()
                self.state = "finished"
                return True

            elif self.state == "defeat":
                assert command == "play again"
                self.reset_game()
                return True

    def reset_game(self):
        """Resets game state for a new session."""
        self.player = Player()  # Reinitialize player stats
        self.grading = Grading(self.player)
        self.feedback = Feedback(self.player)
        self.state = "start"

