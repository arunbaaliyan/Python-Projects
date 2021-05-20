from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FILE_PATH = "./data/french_words.csv"
SAVE_PATH = "./data/save_french.csv"
rand_dict = None
counter = None

# -----------------Create New Flash Cards---------------------
try:
    data = pandas.read_csv(SAVE_PATH)
except FileNotFoundError:
    data = pandas.read_csv(FILE_PATH)

LANGUAGE1 = data.columns[0]
LANGUAGE2 = data.columns[1]
print(data.columns)
word_list = data.to_dict('records')
print(word_list)


# -----------------Functions ---------------------


def next_word():
    global rand_dict, counter
    rand_dict = random.choice(word_list)
    fr_word = rand_dict[LANGUAGE1]
    en_word = rand_dict[LANGUAGE2]
    flashcard.itemconfig(lang, text=LANGUAGE1.title(), fill='black')
    flashcard.itemconfig(word, text=fr_word, fill='black')
    flashcard.itemconfig(card, image=card_front)
    counter = window.after(3000, flip, en_word)


def right():
    window.after_cancel(id=counter)
    word_list.remove(rand_dict)
    next_word()


def wrong():
    window.after_cancel(id=counter)
    next_word()


def flip(en_word):
    flashcard.itemconfig(card, image=card_back)
    flashcard.itemconfig(lang, text=LANGUAGE2.title(), fill='white')
    flashcard.itemconfig(word, text=en_word, fill='white')


def save_file():
    pandas.DataFrame(word_list).to_csv(SAVE_PATH, index=False)
    window.destroy()


# -----------------UI design---------------------

window = Tk()
window.title("Flashcard Learning")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Canvas

flashcard = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card = flashcard.create_image(400, 263, image=card_front)
lang = flashcard.create_text(400, 150, text=LANGUAGE1.title(), font=('Ariel', 40, 'italic'))
word = flashcard.create_text(400, 263, text="Word", font=('Ariel', 60, 'bold'))
flashcard.grid(column=1, row=1, columnspan=2)

# Buttons

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right)
right_button.grid(column=2, row=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.grid(column=1, row=2)

next_word()
window.protocol('WM_DELETE_WINDOW', save_file)
window.mainloop()
