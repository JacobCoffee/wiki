#!/usr/bin/python

from Tkinter import *

def Check():
    input = ent.get()

    if input == 'pass' or input == 'hi' :
        print 'COrrect password'
    elif input == 'passe':
        print 'Close but not it'
    else:
        print 'wrong wrong wrong'

    ent.delete(0,END)
    ent.focus()





root = Tk()

ent = Entry(root, bg = 'white')
button = Button(root, text = 'Press', command = Check)

ent.pack(anchor = W)
button.pack(anchor = E)

ent.focus()

root.mainloop()
