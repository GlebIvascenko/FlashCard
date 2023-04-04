from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
word_pair_dict = {}

try:
    word_pair = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    word_pair_dict = original_data.to_dict(orient="records")
else:
    word_pair_dict = word_pair.to_dict(orient="records")


def select_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(word_pair_dict)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=random_word["English"], fill="White")

def is_known():
    word_pair_dict.remove(random_word)
    data = pandas.DataFrame(word_pair_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    select_word()


window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

red_button_img = PhotoImage(file="./images/wrong.png")
red_button = Button(image=red_button_img, highlightthickness=0, command=select_word)
red_button.grid(column=0, row=1)

green_button_img = PhotoImage(file="./images/right.png")
green_button = Button(image=green_button_img, highlightthickness=0, command=is_known)
green_button.grid(column=1, row=1)

select_word()


window.mainloop()
