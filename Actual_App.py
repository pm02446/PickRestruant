from tkinter import *

import random

locations = ['at Home', 'Dine-In', 'Fast Food']
dine_in = ['Chillis', 'Texas Road House', 'Long Horn Stake House',
           'Red Lobster', 'Outback', 'Chick Fila-A']
fast_food = ['Sonic', 'Zazsby', 'Chik-Flia-A', 'Moes', 'Chipolte', 'Cook Out', 'Taco Bell']
home_food = ['Chicken', 'Pasta', 'Stake', 'Buggers', 'Seafood']


def random_choice(event):
    r = random.choice(locations)
    if r == locations[0]:
        x = (random.choice(home_food))
    elif r == locations[1]:
        x = random.choice(dine_in)
    else:
        x = random.choice(fast_food)
    z = [r, x]
    output_box = Label(w, text=z)
    output_box.pack()
    output_box.after(3000, output_box.destroy)


def fast(event):
    x = (random.choice(fast_food))
    output_box = Label(w, text=x)
    output_box.pack()
    output_box.after(3000, output_box.destroy)


def dine(event):
    x = (random.choice(dine_in))
    output_box = Label(w, text=x)
    output_box.pack()
    output_box.after(3000, output_box.destroy)


def home(event):
    x = (random.choice(home_food))
    output_box = Label(w, text=x)
    output_box.pack()
    output_box.after(3000, output_box.destroy)


w = Tk()

title = Label(w, text='Welcome, Where Are We Eating Today??', font=('', 20,))
title.pack()

random_btn = Button(w, text='Random', bg='black', fg='red', font=('', 15,))
home_btn = Button(w, text='At Home', bg='black', fg='red', font=('', 15,))
fast_btn = Button(w, text='Fast Food', bg='black', fg='red', font=('', 15,))
dine_btn = Button(w, text='Dine-In', bg='black', fg='red', font=('', 15,))

random_btn.pack()
home_btn.pack()
fast_btn.pack()
dine_btn.pack()


random_btn.bind('<Button-1>', random_choice)
home_btn.bind('<Button-1>', home)
fast_btn.bind('<Button-1>', fast)
dine_btn.bind('<Button-1>', dine)

w.mainloop()
