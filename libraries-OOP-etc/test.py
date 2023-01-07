from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    str1 = ""

    letters_list = random.sample(letters, nr_letters)
    numbers_list = random.sample(numbers, nr_numbers)
    symbols_list = random.sample(symbols, nr_symbols)

    password_list = letters_list+numbers_list+symbols_list
    password = str1.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        # message box
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered: \nEmail: {email}"
                                                              f" \nPassword: {password}"
                                                              f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}")
                data_file.write('\n')
                web_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)


# Canvas widget
canvas = Canvas(width=200, height=200)                                   # Canvas widget creation
logo_image = PhotoImage(file="logo.png")                                                   # png object is created
canvas.create_image(100, 100, image=logo_image)                                              # image align to center
canvas.grid(row=0, column=1)

###################################################################

# Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
userMail = Label(text="Email/Username:")
userMail.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# Entries
web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "mulusoy583@gmail.com")


password_input = Entry(width=36)
password_input.grid(row=3, column=1, columnspan=2)


# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()

