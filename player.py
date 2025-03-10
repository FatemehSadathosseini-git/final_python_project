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
        valid_grades = {"1.0", "1.3", "1.7", "2.0", "2.3", "2.7", "3.0", "3.3", "3.7", "4.0", "5.0"}
        if grade in valid_grades:
            self.grades[student] = grade
            return True
        return False  # Invalid grade input

    def get_evaluation(self):
        """Displays the final evaluation points and moves to the evaluation phase."""
        print(f"\nFinal Evaluation Points: {self.evaluation}")
        return

