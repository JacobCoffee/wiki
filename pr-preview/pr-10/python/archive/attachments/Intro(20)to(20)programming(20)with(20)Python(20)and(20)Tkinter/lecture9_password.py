#!/usr/bin/python

from Tkinter import *


def GetValue():
    password = ent.get()
    if password == 'Elaine':
        button['bg'] = 'yellow'
    else:
        ent.insert(0,'wrong password')

    



root = Tk()


lab = Label(root, text = 'Password')
ent = Entry(root, bg = 'white')
button = Button(root, text = 'Enter Password', command = GetValue)


ent.focus()

lab.pack(anchor = W)
ent.pack(anchor = W)
button.pack(ancho = E)


root.mainloop()
