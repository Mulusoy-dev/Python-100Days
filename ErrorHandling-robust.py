from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        },
    }
    if website == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", 'r') as data_file:
                # Reading old data
                data_read = json.load(data_file)                         # Read operation
                # Updating old data with new data
                data_read.update(new_data)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=5)
        else:
            with open("data.json", 'w') as data_file:
                json.dump(data_read, data_file, indent=5)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------SEARCH------------------------------------ #
def find_password():
    search_website = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if search_website in data:
            messagebox.showinfo(title=search_website, message=f"Email: {data[search_website]['email']}\nPassword: {data[search_website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_website} exist")


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
web_input = Entry(width=30)
web_input.grid(row=1, column=1)
web_input.focus()

email_input = Entry(width=30)
email_input.grid(row=2, column=1)
email_input.insert(0, "mulusoy583@gmail.com")


password_input = Entry(width=30)
password_input.grid(row=3, column=1)


# Buttons
password_button = Button(text="Generate Password", width=18, command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=25, command=save)
add_button.grid(row=4, column=1, columnspan=1)
search_button = Button(text="Search", width=18, command=find_password)
search_button.grid(row=1, column=2)





window.mainloop()

