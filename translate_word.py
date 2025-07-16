# Capstone project - Flash Card program
# frequency dictionary - That keeps tracks of how many times each unique item(like a word, number, or characters appear on the given data set
from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {} # shuffling our dict data

try:
    data = pandas.read_csv("data/words_to_learn.csv") # if the file was deleted or not right here
except FileNotFoundError: # it will access japanese_Tamil data to show what we have missed to learn
    original_data = pandas.read_csv("data/japanese_Tamil.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    # orient use case to convert dictionary values in list format value
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time) # if we fastly flip our card this argument will replace it with matching words
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Japanese")
    canvas.itemconfig(card_word, text=current_card["Japanese"])
    canvas.itemconfig(card_background, image=card_front_img)
    flip_time = window.after(1500, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Tamil", fill="purple")
    canvas.itemconfig(card_word, text=current_card["Tamil"])
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card) # when the user click the check mark it will remove the current card
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")# it will create a file data
    next_card()

window = Tk()
window.title("Flash card quiz")
window.config(padx=50, pady=50, bg="#FFC0CB")

flip_time = window.after(2000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "bold", "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold", "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
cross_image = PhotoImage(file="images/wrong.png")
x_button_button = Button(image=cross_image, highlightthickness=0, command=next_card, bg="#000000")
x_button_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_mark_button = Button(image=check_image, highlightthickness=0, command=is_known, bg="#000000")
check_mark_button.grid(row=1, column=1)

next_card()

window.mainloop()
