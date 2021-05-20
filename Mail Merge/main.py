#TODO: Create a letter using starting_letter.txt
with open('./Input/Letters/starting_letter.txt') as file:
    letter = file.read()
#for each name in invited_names.txt
with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()
for name in names:
    name = name.strip('\n')
    new_letter = letter.replace('[name]', name)
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as out_letter:
        out_letter.write(new_letter)
