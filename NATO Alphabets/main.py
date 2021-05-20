
import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# data = pandas.read_csv('nato_phonetic_alphabet.csv').to_dict('index')
# print(type(data))
# print(data)
# letters = data.letter.to_list()
diction = {row.letter: row.code for (index, row) in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
should_continue = True
while should_continue:
    user_input = input("Enter the word yow want phonetic for? : ").upper()
    try:
        result = [diction[n] for n in user_input]
        should_continue = False
    except KeyError:
        result = "Sorry, only letters in alphabet please."
    print(result)
