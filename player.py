"""
Author: Fatemeh Sadat Hosseini
Date: 2025-03-10
Purpose: Defines the Player class and manages the player's state.
"""
import random
from nltk.corpus import names


class Player:
    def __init__(self):
        """Initialize the tutor with default stats."""
        self.energy = 10  # Initial energy points
        self.evaluation = 0  # Evaluation points
        self.students = self.generate_student_list()  # List of 8 random students
        self.grades = {student: None for student in self.students}  # Store grades

    def generate_student_list(self):
        """Select 8 random student names from the NLTK names corpus."""
        return random.sample(names.words(), 8)

    def show_report(self):
        """Displays the current semester report."""
        print("\n--- Semester Report ---")
        print(f"Energy Level: {self.energy} | Evaluation Points: {self.evaluation}")
        print("Grades:")
        for student, grade in self.grades.items():
            grade_display = grade if grade is not None else "-/-"
            print(f"   {student}: {grade_display}")
        print("------------------------")

    def rest(self):
        """Increase energy by resting."""
        self.energy += 5
        print("You took a break and gained 5 energy points.")

    def eat_chocolate(self):
        """Boost energy with chocolate (only once per grading session)."""
        self.energy += 10
        print("You ate some chocolate and gained 10 energy points.")

    def update_energy(self, amount):
        """Modify energy points and check if the game is lost."""
        self.energy += amount
        if self.energy <= 0:
            print("\nOh no! You are completely exhausted. Game over!")
            return "defeat"
        return None  # Game continues

    def assign_grade(self, student, grade):
        """Assign a valid grade to a student."""
        try:
            float_grade = float(grade)
        except ValueError:
            print(f"Invalid grade '{grade}' for student '{student}'. Grade must be a number.")
            return False

        if 1 <= float_grade <= 5:
            self.grades[student] = float_grade
            return True
        else:
            print(f"Invalid grade '{grade}' for student '{student}'. Grade must be between 1 and 5.")
            return False

    def get_evaluation(self):
        """Displays the final evaluation points and moves to the evaluation phase."""
        print(f"\nFinal Evaluation Points: {self.evaluation}")
        return

