import random
import time
from tkinter import *

import pandas
import pandas as pd
from time import sleep

BACKGROUND_COLOR = "#B1DDC6"
ENGLISH_TITLE = ("Ariel", 40, "italic")
WORD_TITLE = ("Ariel", 60, "bold")
random_word = {}
new_word_dict = {}

# ---------------------------- READ DATA ------------------------------- #
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_Data = pd.read_csv("data/english_vocabulary.csv")
    word_dict = original_Data.to_dict(orient="records")
else:
    word_dict = df.to_dict(orient="records")


# ---------------------------- CHANGE WORD ------------------------------- #
def random_words():
    global random_word
    global flip_timer
    global new_word_dict
    window.after_cancel(flip_timer)

    random_word = random.choice(word_dict)
    random_en_word = random_word["English"]               # Random English Word
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(cnv_word_label, text=random_en_word, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="Turkish", fill="white")
    random_tr_word = random_word["Turkish"]                # English to Turkish Translate
    canvas.itemconfig(cnv_word_label, text=random_tr_word, fill="white")


def is_known():
    word_dict.remove(random_word)
    print(len(word_dict))
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_words()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Ok Button
my_image = PhotoImage(file="/Users/mulus/Downloads/flash-card-project-start/images/right.png")
ok_button = Button(image=my_image, highlightthickness=0, borderwidth=0, command=is_known)
ok_button.grid(row=1, column=1)


# Not Button
my_image2 = PhotoImage(file="/Users/mulus/Downloads/flash-card-project-start/images/wrong.png")
not_button = Button(image=my_image2, highlightthickness=0, borderwidth=0, command=random_words)
not_button.grid(row=1, column=0)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_image = PhotoImage(file="/Users/mulus/Downloads/flash-card-project-start/images/card_back.png")
card_front_image = PhotoImage(file="/Users/mulus/Downloads/flash-card-project-start/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=ENGLISH_TITLE)
cnv_word_label = canvas.create_text(400, 263, text="", font=WORD_TITLE)
canvas.grid(row=0, column=0, columnspan=2)





random_words()











window.mainloop()

