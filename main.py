from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
reps = 0

# ---------------------------- RIGTH/WRONG BUTTONS ------------------------------- #

def right():
  global reps
  del word_eng[reps]
  del word_pt[reps]
  new_data = []
  new_data = pd.DataFrame(new_data)
  new_data["English"] = word_eng
  new_data["Portuguese"] = word_pt
  new_data.to_csv("data/to_learn.csv")
  change()
  
def wrong():
  global reps
  get_e = word_eng[reps]
  get_p = word_pt[reps]
  del word_eng[reps]
  del word_pt[reps]
  word_eng.append(get_e)
  word_pt.append(get_p)
  change()

# ---------------------------- CHANGE TEXT ------------------------------- #

def change():
  global reps
  language = canvas.itemcget(title,"text")
  if language == "English":
    canvas.itemconfig(img,image=back_img)
    canvas.itemconfig(title,text="Português",fill="white")
    canvas.itemconfig(word,text=word_pt[reps],fill="white")
  else:
    canvas.itemconfig(img,image=front_img)
    canvas.itemconfig(title,text="English",fill="black")
    canvas.itemconfig(word,text=word_eng[reps],fill="black")
    w.after(3000,change)

# ---------------------------- CSV SETUP ------------------------------- #
try:
  data = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
  data = pd.read_csv("data/words.csv")
finally:
  word_eng = data.English.to_list()
  word_pt = data.Portuguese.to_list()

# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("Flash Card")
w.config(width=800,height=526,padx=50,pady=50,bg=BACKGROUND_COLOR)
w.after(3000,change)

#Cards
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400,263,image=front_img)
title = canvas.create_text(400,150,text="English",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text=word_eng[0],font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

#Buttons

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,borderwidth=0,command=wrong)
wrong_button.grid(column=0,row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0,borderwidth=0,command=right)
right_button.grid(column=1,row=1)

w.mainloop()
