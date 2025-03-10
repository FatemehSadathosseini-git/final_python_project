import random
import os
import csv

from nltk.corpus import names

def load_descriptions(file_path):
    """Loads scene descriptions from a text file into a dictionary."""
    descriptions = {}
    if not os.path.exists(file_path):
        print("Warning: Description file not found!")
        return descriptions

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        for line in reader:
            descriptions[line[0]] = line[1]
    return descriptions

def generate_student_names(count=8):
    """Returns a list of unique random student names from the NLTK corpus."""
    return random.sample(names.words(), count)
