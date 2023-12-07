from tkinter import *


def miles_to_cm():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km:.3f}")


window = Tk()
window.title("Simple converter")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_cm)
calculate_button.grid(column=1, row=2)

window.mainloop()
