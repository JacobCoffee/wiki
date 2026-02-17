# tk md5

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Description 

Create an MD5 Hash with this little script that comes with a simple TKinter GUI. Get more info on creating MD5 hashes at [Md5Passwords](Md5Passwords)

# Code 

    from Tkinter import *
    import hashlib

    def doitnow():
        salt = insalt.get()
        textstr = text_str.get()
        hash = hashlib.md5( salt + textstr ).hexdigest()
        hashtext.delete(0,END)
        hashtext.insert(0,hash)
        return 0

    root = Tk()
    lab1 = Label(root, text = 'Salt:')
    lab2 = Label(root, text = 'Key String:')
    lab3 = Label(root, text = 'Hash:')

    insalt = Entry(root, bg = 'white')
    text_str= Entry(root, bg = 'white')
    hashtext = Entry(root, bg = 'white')

    button = Button(root,text = "Hash It", command = doitnow)

    insalt.focus()

    lab1.pack(anchor = W)
    insalt.pack(anchor = W)
    lab2.pack(anchor = W)
    text_str.pack(anchor = W)
    lab3.pack(anchor = W)
    hashtext.pack(anchor = W)
    button.pack(ancho = E)


    root.mainloop()
