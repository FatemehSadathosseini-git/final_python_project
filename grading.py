import random
from player import Player


class Grading:
    def __init__(self, player):
        """Initialize grading session with the player's stats."""
        self.player = player
        self.chocolate_used = False  # Track if chocolate has been used in the session

    def grade(self, command):
        """Start grading session and transition to feedback after completion."""
        if command == "grade":
            print("\n--- Grading ---")
            for student in self.player.students:
                result = self.grade_student(student)

                # if result in ["defeat", "time_off", "cholocate"]:
                if result in ["defeat", "exit"]:
                    return result


            print("\nAll grades entered! Time for feedback.")

        elif command == "delay grade":
            print("\nSkipping to feedback session...")

        return "feedback_1" if self.player.evaluation == 0 else "feedback_2"


    def grade_student(self, student):
        """Handles grading a single student, including random events."""
        while True:
            grade = input(
                f"Enter valid grade for {student} or wanna rest or eat a chocolate : ").strip()

            if grade == "rest":
                self.player.rest()
            elif grade in ["chocolate", "eat chocolate", "eat a chocolate"]:
                if not self.chocolate_used:
                    self.player.eat_chocolate()
                    self.chocolate_used = True
                else:
                    print("You've already used chocolate for this grading session.")
                continue
            elif grade == "exit":
                return "exit"
            elif grade == "inspect report":
                self.player.show_report()
            elif self.player.assign_grade(student, grade):
                print(f"Grade {grade} assigned to {student}. -5EP")
                if self.player.update_energy(-5) == "defeat":
                    return "defeat"
                self.random_event()
                return
            else:
                print("Invalid grade! Try again.")

    def random_event(self):
        """Triggers random events that impact energy."""
        event = random.choices(
            ["extension", "regrading", "debugging", "appreciation", "none"],
            weights=[0.2, 0.2, 0.3, 0.1, 0.2]
        )[0]

        if event == "extension":
            print("A student requested an extension! -3EP")
            self.player.update_energy(-3)
        elif event == "regrading":
            print("A student requested regrading! -2EP")
            self.player.update_energy(-2)
        elif event == "debugging":
            print("You had to do some heavy debugging! -1EP")
            self.player.update_energy(-1)
        elif event == "appreciation":
            print("A student appreciated your hard work! +3EP")
            self.player.update_energy(+3)
