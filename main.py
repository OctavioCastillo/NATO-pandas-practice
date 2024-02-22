"""
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}"""

# Project starts from here
import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# read the csv
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# set the letter as a key and the code as a value, meanwhile the dictionary is created
# iterative the for into the index and the row, using .iterrows() method
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        # get the value of the letter in the dictionary already created
        phonetic_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print(" Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_word)


generate_phonetic()
