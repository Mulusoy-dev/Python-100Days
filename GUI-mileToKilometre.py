from tkinter import *


def button_clicked():
    km_calc = int(input.get()) * 1.6
    label_out.config(text=km_calc)


window = Tk()                                         # yeni obje oluşturulması işlemi
window.title("My Fist GUI Application")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)                       # padx ve pady ile etrafı ile köşelere olam mesafe ayarlanır


# Label
my_label = Label(text="is equal to", font=("Arial", 10, "bold"))
my_label.grid(row=1, column=0)

label2 = Label(text="Miles", font=("Arial", 10, "bold"))
label2.grid(row=0, column=2)

label3 = Label(text="Km", font=("Arial", 10, "bold"))
label3.grid(row=1, column=2)

label_out = Label(text="", font=("Arial", 10, "bold"))
label_out.grid(row=1, column=1)


# Button
my_button = Button(text="Calculate", command=button_clicked)           # Buton nesnesinin oluşturulması
my_button.grid(row=2, column=1)


# Entry
input = Entry(width=10)
input.grid(row=0, column=1)


window.mainloop()