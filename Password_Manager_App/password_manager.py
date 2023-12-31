from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = username_entry.get()
    pas = password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": pas
        }
    }
    if len(website) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure all fields aren't empty")
    else:
        messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: \n \nEmail: {user}"
                                                           f"\nPassword: {pas} \nIs OK to save?")
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="Data file not found!")
    else:
        if not website:
            # Error msg for empty field.
            messagebox.showinfo(title=f"Oops", message=f"Website empty!")
        elif website in data:
            # Message with stored credentials
            messagebox.showinfo(title=f"{website}", message=f"Username: {data[website]['email']}\n"
                                                            f"Password: {data[website]['password']}")
        else:
            # Error msg when website not in stored data.
            messagebox.showinfo(title=f"{website}", message=f"You don't have registration on this website")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# labels:
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_suer_label = Label(text="Email/Username:")
email_suer_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry:
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=54)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "delian.nikolov@abv.bg")

password_entry = Entry(width=36)
password_entry.grid(column=1, row=3)

# Buttons:
search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
