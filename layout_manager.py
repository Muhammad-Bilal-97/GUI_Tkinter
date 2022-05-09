# import tkinter
from tkinter import *


def button_clicked():
    print("I got clicked")
    # my_label["text"] = "Button got clicked"
    # new_text = input.get()
    # my_label.config(text=new_text)
# my_label["text"] = "New text"
# my_label.config(text="Again new text")



# Creating a new window and configurations
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I'm a label.", font=("Arial", 24, "bold"))
my_label.config(text="New text.")
my_label.grid(column=0, row=0)


# Buttons
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entries(Input)
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)





window.mainloop()