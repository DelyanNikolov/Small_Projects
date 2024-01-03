from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.question_field = Canvas(width=300, height=250, highlightthickness=0)
        self.question_field.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.question_field.create_text(150, 125,
                                                             text="Question text",
                                                             fill=THEME_COLOR, font=FONT)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=false_img, highlightthickness=0)
        self.true_button.grid(column=1, row=2)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.window.mainloop()
