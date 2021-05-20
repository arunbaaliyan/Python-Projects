from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REP
    REP = 0
    window.after_cancel(TIMER)
    tick_label['text'] = ""
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REP
    REP += 1
    if REP % 2 == 1 and REP < 8:
        timer_label.config(text='Work', fg=GREEN)
        countdown(WORK_MIN * 60)
    elif REP % 2 == 0 and REP < 8:
        timer_label.config(text='Break', fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    elif REP == 8:
        timer_label.config(text='Break', fg=RED)
        countdown(LONG_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global TIMER
    minutes = int(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f'{minutes:02d}:{seconds:02d}')
    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if REP % 2 == 0:
            tick_label['text'] += "✔"


# ---------------------------- UI SETUP ------------------------------- #
# making window
window = Tk()
window.title('My pomodoro timer')
window.config(bg=YELLOW, padx=50, pady=50)

# making canvas
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato)
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=2, row=2)
# making buttons
start_button = Button(text='Start', command=start_timer, bg=YELLOW, highlightthickness=0)
start_button.grid(column=1, row=3)
reset_button = Button(text='Reset', command=reset_timer, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=3, row=3)

# making labels
timer_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=YELLOW)
timer_label.grid(column=2, row=1)
tick_label = Label(text='', fg=GREEN, font=(FONT_NAME, 14), bg=YELLOW)
tick_label.grid(column=2, row=4)

window.mainloop()
