from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


def next_card():
    current_card = random.choice(words_data)
    flash_card.itemconfig(card_title, text="French")
    flash_card.itemconfig(card_word, text=current_card["French"])


data = pandas.read_csv("data/french_words.csv")
words_data = data.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ____________________Flashcard____________________:
card_front_img = PhotoImage(file="images/card_front.png")
flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.create_image(400, 263, image=card_front_img)
flash_card.grid(column=0, row=0, columnspan=2)
card_title = flash_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = flash_card.create_text(400, 256, text="word", font=("Ariel", 60, "bold"))

# ____________________Buttons____________________:
wright_img = PhotoImage(file="images/right.png")
wright_button = Button(image=wright_img, highlightthickness=0, command=next_card)
wright_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
