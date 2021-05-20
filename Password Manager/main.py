from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ('Ariel', 12, 'normal')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list.extend([choice(letters) for _ in range(randint(8, 10))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.delete(0, END)
    pass_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if website.strip() == "" or password.strip() == "":
        messagebox.showerror('OOPS!!!', "Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(website.upper(), f"You have entered following details:\n\nEmail: {email}\nPassword: "
                                                f"{password}\n\nIs it OK to save?")
        if is_ok:
            try:
                with open('passwords.json', mode='r') as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open('passwords.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open('passwords.json', mode='w') as file:
                    json.dump(data, file, indent=4)
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = website_entry.get().lower()
    if len(website.strip()) == 0:
        messagebox.showerror('ERROR!!!', 'Please enter data to search.')
    else:
        try:
            with open('passwords.json', mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror('ERROR!!!', f'No data found for {website}.')
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(website.upper(), f"E-Mail : {email}\nPassword : {password}")
                pyperclip.copy(password)
            else:
                messagebox.showerror('ERROR!!!', f'No details found for {website}.')
        finally:
            website_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('My Password Manager')
window.config(padx=50, pady=100, bg='white')

logo = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

# labels
website_label = Label(text='Website:', font=FONT, pady=10, bg='white')
website_label.grid(column=1, row=2)
email_label = Label(text='Email/Username:', font=FONT, pady=10, bg='white')
email_label.grid(column=1, row=3)
pass_label = Label(text='Password:', font=FONT, pady=10, bg='white')
pass_label.grid(column=1, row=4)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=2, row=2)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.insert(END, 'arunbaaliyan@gmail.com')
email_entry.grid(column=2, row=3, columnspan=2)
pass_entry = Entry(width=35)
pass_entry.grid(column=2, row=4)

# Buttons
generate_button = Button(text='Generate', font=FONT, bg='white', command=password_generator)
generate_button.grid(column=3, row=4)

search_button = Button(text='Search', font=FONT, bg='white', command=search)
search_button.grid(column=3, row=2)

add_button = Button(text='Add', font=FONT, width=33, bg='white', command=add_password)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
