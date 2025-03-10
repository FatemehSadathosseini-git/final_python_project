import random
import time
import re
from nltk.corpus import reuters

class Feedback:
    def __init__(self, player):
        """Initialize feedback session with the player's stats."""
        self.player = player

    def process(self, command):
        """Handles the transition between feedback sessions."""
        if command == "give feedback":
            if self.player.evaluation == 0:  # First feedback session
                return self.feedback_session_1()
            else:  # Second feedback session
                return self.feedback_session_2()
        else:
            print("Invalid command in this state!")
            return "feedback_1" if self.player.evaluation == 0 else "feedback_2"


    def feedback_session_1(self):
        """First feedback session: Tutor must guess three topics based on a riddle."""
        print("\n--- Feedback Session 1: Guess the Topic! ---")

        topics = reuters.categories()
        chosen_topics = random.sample(topics, 3)  # Pick 3 random topics
        total_points = 0

        for topic in chosen_topics:
            # Collect valid sentences for the topic
            sentences = [s for s in reuters.sents(categories=topic) if len(s) < 20]
            valid_sentences = []

            for sent in sentences:
                text = " ".join(sent)
                if len(re.findall(r"\d+", text)) > 3:
                    continue  # Skip if too many numbers
                text = re.sub(rf"\b{topic}\b", "[HIDDEN]", text, flags=re.IGNORECASE)  # Mask topic name
                valid_sentences.append(text)

            if not valid_sentences:
                print(f"\nNo valid sentences found for topic {topic}. Skipping...")
                continue

            sentence = random.choice(valid_sentences)
            print(f"\nHere is the sentence:\n{sentence}")

            attempts = 0
            hint_given = False  # To track if the player has used "clarify"
            start_time = time.time()  # Track time for the 1-minute rule

            while attempts < 3:
                guess = input("> Guess the topic (or type 'clarify' for a hint): ").strip().lower()

                # Check if time exceeded 1 minute
                if time.time() - start_time > 60:
                    print("\nYou took too long to answer! Game Over.")
                    return "defeat"

                if guess == "clarify" and not hint_given:
                    print("Hint:", random.choice(valid_sentences))
                    hint_given = True  # Allow one hint per topic
                    continue  # Don't count this as an attempt

                attempts += 1  # Count an actual guess attempt

                if guess == topic.lower():
                    points = 40 - (attempts - 1) * 10  # 40, 30, or 20 points
                    print(f"Correct! +{points} evaluation points.")
                    total_points += points
                    break  # Move to the next topic
                else:
                    print("Wrong answer! Try again.")

            if attempts == 3:
                print(f"\nYou failed to guess the topic '{topic}'. No points awarded.")

        self.player.evaluation += total_points
        print(f"\nTotal evaluation points earned: {total_points}")
        return "grading"


    def feedback_session_2(self):
        """Second feedback session: Find the code phrase."""
        print("\n--- Feedback Session 2: Find the Code Phrase! ---")
        attempts = 3
        while attempts > 0:
            phrase = input("> Enter a code phrase: ").strip().split()
            if phrase and len(phrase) >=1 and self.is_valid_code_phrase(phrase):
                print("Correct! +80 evaluation points.")
                self.player.evaluation += 80
                return "evaluation"
            else:
                attempts -= 1
                print(f"Invalid code phrase! {attempts} attempts left.")

        print("\nYou failed to find a valid code phrase. Game over!")
        return "defeat"

    def is_valid_code_phrase(self, phrase):
        """Recursively checks if a phrase follows the code phrase rule as defined in the PDF."""
        # Convert to lowercase for case-insensitive comparison and filter out non-alphabetic words
        phrase = [word.lower() for word in phrase if word.isalpha()]

        n = len(phrase)

        # Base Case 1: If there are no words left, it means all checks have passed
        if n == 0:
            return True

            # Base Case 2: If there's only one word (odd n), check first letter <= last letter
        if n == 1:
            return phrase[0][0] <= phrase[0][-1]

        # Check the first and last word conditions
        if phrase[0][0] > phrase[-1][0] or phrase[-1][-1] > phrase[0][-1]:
            return False  # Condition fails → Not a valid code phrase

        # Recursive Case: Check the remaining words
        return self.is_valid_code_phrase(phrase[1:-1])


