# import tkinter
from tkinter import *

# Variables
FONT = ("Arial", 16, "normal")


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")


# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entries(Input)
miles_input = Entry(width=7)
print(miles_input.get())
miles_input.grid(column=1, row=0)


# Label
miles_label = Label(text=" Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=5, pady=5)

km_result_label = Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)
km_result_label.config(padx=5, pady=5)


km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

# Buttons
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=5, pady=5)


window.mainloop()
