from tkinter import *
import pandas as pd 
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = None
flip_timer = None

#SET UP DATA FRAME
try:
    data = pd.read_csv("words_to_learn.csv")
except:
    data = pd.read_csv("./data/french_words.csv")

data_dict = data.to_dict(orient='records')


# FUNCTIONS
def got_it_right():
    global current_card
    try:
        data_dict.remove(current_card)
    except:
        pass
        
    
    next_card()
    
def next_card():
    global current_card, flip_timer
    
    
    if flip_timer:
        window.after_cancel(flip_timer)
    
    if not data_dict:
        canvas.itemconfig(lang_text, text="Congrats", fill='black', font=('Ariel', 60, 'bold'))
        canvas.itemconfig(word_text, text="You have finished the flashcard deck!", fill='black', font=('Ariel', 40, 'normal'))
        window.after(4000, save_and_close)
        return
    
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_img, image=french_img)

    canvas.itemconfig(lang_text, text="French", fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')

    flip_timer=window.after(3000, flip_to_eng)
    
def flip_to_eng():
    global current_card
    if current_card:
        canvas.itemconfig(canvas_img, image=eng_img)
        canvas.itemconfig(lang_text, text="English", fill='white')
        canvas.itemconfig(word_text, text=current_card['English'], fill='white')
    
def save_and_close():
    df = pd.DataFrame(data_dict)
    df.to_csv("words_to_learn.csv", index=False)
    window.destroy()

    
# UI SETUP

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_to_eng)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

french_img = PhotoImage(file="./images/card_front.png")
eng_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400,263, image=french_img)

lang_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, 'italic'))
word_text = canvas.create_text(400, 263, text=f'', fill="black", font=("Ariel", 60, "bold"))

canvas.grid(column=1, row=1, columnspan=2)

n = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=n, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=2)

y = PhotoImage(file="./images/right.png")
right_button = Button(image=y, highlightthickness=0,command=got_it_right)
right_button.grid(column=2, row=2)

next_card()

window.protocol("WM_DELETE_WINDOW", save_and_close)

window.mainloop()
