from tkinter import *

# button1 = Button(topFrame, text="Button 1", fg='red')
# location, text, color: bg- background and fg- text color,

# title = Label(window, text="Where to Eat??")
# this creates text, 1st parameter is the location and second is the text
# title.pack()
# pack, places it onto the window

# UserName = Label(window, text='name')
# Password = Label(window, text='Password')
# textblock_1 = Entry(window)
# textblock_2 = Entry(window)
# UserName.grid(row=0, sticky=W)
# you use sticky in grid to represent  East, West, North, and South
# Password.grid(row=1, sticky=W)
# textblock_1.grid(row=0, column=1)
# textblock_2.grid(row=1, column=1)
# check_box = Checkbutton(window, text='Keep me logged in')
# check_box.grid(columnspan=2)

# topFrame = Frame(window)
# this is to put a invisible container in window
# topFrame.pack()
# the parameter is the location, fill- fills either x or y axis

# use command call to call a function

# bind, use to bind a function to a event
# object.bind(event, function)

# using a classes:
# create calss, create object and call the root
# __init__ : once class is called, all methods will be called

# create a menu
# menu = Menu(window)
# window.config(menu=menu)
# subMenu = Menu(menu)
# menu.add_cascade(label='File', menu=subMenu)
# subMenu.add_command(label='New Project...', command=doNothing)
# subMenu.add_separator()
# subMenu.add_command(label='New', command=doNothing)

############################


def printSomething():
    for x in range(9):
        label = Label(window, text=str(x))
        label.pack()


window = Tk()
# this creates a blank window

btn = Button(window, text='Print Me', command=printSomething)
btn.pack()

window.mainloop()
# this keeps the window open till you close it
