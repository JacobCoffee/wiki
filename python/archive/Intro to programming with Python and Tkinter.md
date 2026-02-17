# Intro to programming with Python and Tkinter

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Introduction 

hello \....

The purpose of this project is to provide user an interactive environment for anyone interested in learning python. So far most of the tutorials are in text format. However, when I was learning python, I always wished somebody had taught an online video course. Thanks to ourmedia.org for storing my videos it is now possible to provide this service.

This effort is also a part of a much larger effort I am starting, The opensource University effort. Actually, I am building a free 3D University where everybody can get together learn take free classes.

If you have played 3d world computer games, you would know what type of 3d world i\'m talking about. Its kinda like that except its a school. You would run around and click on teachers instead of monster. And a video would pop out, and \"hopefully\" teach you something useful.

The website for this academy is [http://iamar.net](http://iamar.net). If you are interested to see what this school looks like, you can check out the demo videos. [http://iamar.net/subpages/video.html](http://iamar.net/subpages/video.html). In general, you can find all the course we teach here: [http://iamar.net/subpages/vidLectures.html](http://iamar.net/subpages/vidLectures.html)

*The Education Philosophy*

The problem with education is the lack of effort to make the contents inspiring and fun. For thousands of years, the education system has maintained an image that people can only learn new information through arduous work. When in reality this is not true. We all know that there are people that can recite the name of every star football and basketball player. There are people that memorized the energy damage of every sword in their computer and video game. And these knowledge were not obtained through painful work but for fun. There are probably less names to remember for all the presidents of United State than all the major star sports players. Yet people are able to achieve amazing learning never even considered it painful. That is possible for a very simple fact. People will learn what they \"want\" to learn. Learning itself only becomes painful when it is forced upon a person.

Our education system pays very little attention to the psychology of the audience. In this respect, they have much to learn from the entertainment industry. Of course, the entertainment industry makes its money by inspiring people to get engaged, and they have done an amazing job. The point here is that if the entertainment industry has engaged the population to learn an enormous amount of useless information, so can the education system engage the learners to learn useful information. By combining entertainment philosophies, education can turn arduous work into fun exercises. This is possible.

*The Iamar Experiment is but only the beginning of this philosophy.*

A lot of people have been asking for the first 2 lectures, well, I never recorded them. The first lecture was suppose to explain how python is and its general information, and the second lecture is for the installation of python. I never had the chance to record them, and most people learning seems to already know how to install them.

Due to the construction of the school, I have been rather late in replying, I have also changed my email address to [iamar.chieh@gmail.com](mailto:iamar.chieh@gmail.com)

Chieh Wu

## Intro to programming with Python in Tkinter 

Have you ever wanted to know how your application is programmed on the computer. This lecture will show you how easy it is to program.

Aimed at beginner programmers or people that has no programming experience. For you to watch this class, you must have python installed from python.org . Lecture 2 will show you how to install and run python. This lecture assumes that you already have python.

The python course series is designed to be short, fun, and concise. They are 10 minutes each with fun examples and easy instruction. If you want to learn programming this is the way to go.

### Lecture 1: Why is python so cool??? 

In this lecture I will convince you that python will eventually take over the world :). Actually we will discuss how the class will be conducted and how much fun we are going to have. This will be the last lecture I write.

### Lecture 2: How to download python 

I will show you where you download python. If you found this page, chances are that you already know how. I will also talk about different resources to help you program python.

### Lecture 3: Your first python program (10min) 

[http://iamar.net/subpages/pythonLect3.html](https://web.archive.org/web/20121126014531/http://iamar.net/subpages/pythonLect3.html)

Like all programming books, we kick off with a quick and simple non-hello world application.

**You will learn:** *importing Tkinter library, create a simple list, create a window, create a listbox, fill a listbox, parents of widgets*

**Example Code**:

- **lecture3 example 1**

<!-- -->

    from Tkinter import *           # Importing the Tkinter (tool box) library 
    root = Tk()                     # Create a background window
                                    # Create a list
    li = 'Carl Patrick Lindsay Helmut Chris Gwen'.split()
    listb = Listbox(root)           # Create a listbox widget
    for item in li:                 # Insert each item within li into the listbox
        listb.insert(0,item)

    listb.pack()                    # Pack listbox widget
    root.mainloop()                 # Execute the main event handler

- **lecture3 example 2**

<!-- -->

    from Tkinter import *           # Import the Tkinter library
    root = Tk()                    # Create a background window object
                                    # A simple way to create 2 lists
    li     = ['Carl','Patrick','Lindsay','Helmut','Chris','Gwen']
    movie  = ['God Father','Beauty and the Beast','Brave heart']
    listb  = Listbox(root)          # Create 2 listbox widgets
    listb2 = Listbox(root)
    for item in li:                 # Insert each item inside li into the listb
        listb.insert(0,item)

    for item in movie:              # Do the same for the second listbox
        listb2.insert(0,item)

    listb.pack()                    # Pack each listbox into the main window
    listb2.pack()
    root.mainloop()                 # Invoke the main event handling loop

### Lecture 4: Button are meant to be pushed(10min) 

[http://iamar.net/subpages/pythonLect4.html](https://web.archive.org/web/20130724053700/http://iamar.net/subpages/pythonLect4.html)

When you press a button, your program will say \"hi\"

**You will learn:** *create a button, create a label, link up a button with specific functions, the concept of functions, indentation of functions, changing the foreground and background of widgets*

**Example Code**

- **lecture4 example 1**

<!-- -->

    from Tkinter import *

    def Pressed():                          #function
            print 'buttons are cool'

    root = Tk()                             #main window
    button = Button(root, text = 'Press', command = Pressed)
    button.pack(pady=20, padx = 20)
    Pressed()
    root.mainloop()

- **lecture4 example 2**

<!-- -->

                                #Souce section   1

    #mandatory for unix and linux
    #---------------------------------------------------------------

    from Tkinter import *       #This library give us windows and buttons
    from random import *        #This library allows us to generate random numbers
                                #import library section   2

    #
    #What not to use??? 
    #---------------------------------------------------------------

    def one_to_ten():
        ran = uniform(1,10)
        print ran
        
    def GoWork():           # def starts a function, or define a function
        sum = 3*5 
        print sum               #Function section   3 
            
    #----------------------------------------------------------------


            
                                #Code section    4
        
    window = Tk()      #i am the parent, button = child

    stacy = Button(window, text = 'yoyo', command = one_to_ten)  
    #A rose with any other name would be just as sweet


    stacy.pack()        #you can name it after your fish (ignored)
    window.mainloop()         #you can use your fish's name 

- **lecture4 example 3**

<!-- -->

    from Tkinter import *


    def Call():
            lab= Label(root, text = 'You pressed\nthe button')
            lab.pack()
            button['bg'] = 'blue'
            button['fg'] = 'white'

    root = Tk()
    root.geometry('100x110+350+70')
    button = Button(root, text = 'Press me', command = Call)
    button.pack()

    root.mainloop()

- **lecture4 example 5**

<!-- -->

    from Tkinter import *           #This interface allow us to draw windows


    def DrawList():
            plist = ['Liz','Tom','Chi']

            for item in plist:
                    listbox.insert(END,item);
                    
            
    root = Tk()                     #This creates a window, but it won't show up

    listbox = Listbox(root)
    button = Button(root,text = "press me",command = DrawList)

    button.pack()
    listbox.pack()                  #this tells the listbox to come out
    root.mainloop()                 #This command will tell the window come out

### Lecture 5: Stealing is good in programming(10min) 

[http://iamar.net/subpages/pythonLect5.html](http://iamar.net/subpages/pythonLect5.html)

We will program something using other people\'s code ![:)](/wiki/europython/img/smile.png ":)")

**Your will learn:**How to program large programs, how to borrow other people\'s code(modules), basic concepts to functions

**Example Code**

- **lecture5 stacy.py 1**

<!-- -->

    def adder( num1 , num2):
            return num1 + num2

    def multiply( num1 , num2):
            return num1*num2


    print multiply(3,range(2)) # oh what fun it is!

    print(multiply(3,list(range(2)))) # python 3k.

- **lecture5 chieh.py**

<!-- -->

    from stacy import *

    #Find 3 +4 + (3*5)

    first = adder(3,4)
    second = multiply(3,5)
    answer = adder(first,second)

    print answer

### Lecture 6: How to create anything in Tkinter(10min) 

[http://iamar.net/subpages/pythonLect6.html](http://iamar.net/subpages/pythonLect6.html)

The needed text is at [http://ourmedia.org/node/6635](http://ourmedia.org/node/6635)

We will learn how to create everything in the Tkinter library, windows, buttons, listbox, entrybox, menus, etc.

**You will learn:***How to create any Tkinter widget, how to make stand alone modules.*

**Example Code** [lecture6_chieh.py](attachments/Intro(20)to(20)programming(20)with(20)Python(20)and(20)Tkinter/lecture6_chieh.py) [lecture6_stacy.py](attachments/Intro(20)to(20)programming(20)with(20)Python(20)and(20)Tkinter/lecture6_stacy.py)

### Lecture 7: Now let\'s make them do something(10min) 

[http://iamar.net/subpages/pythonLect7.html](http://iamar.net/subpages/pythonLect7.html)

Now that we have learned how to create widgets, we need to tell them to do something. In this lecture we will mainly focus on Entry boxes. We will create an entry box, a button, and a listbox. When we press the button the program will take the name in the entry and put them into the list.

**You will learn:** *insert text into a listbox, get text from Entry box, changing the size of the window, controlling where the window pop up, delete what\'s inside the entry box, controlling the padding between widgets*

**Example Code** [lecture7_homework.py](attachments/Intro(20)to(20)programming(20)with(20)Python(20)and(20)Tkinter/lecture7_homework.py) [lecture7_text.py](attachments/Intro(20)to(20)programming(20)with(20)Python(20)and(20)Tkinter/lecture7_text.py)

### Lecture 8: Let\'s make some decisions(7min) 

[http://iamar.net/subpages/pythonLect8.html](http://iamar.net/subpages/pythonLect8.html)

[https://archive.org/details/ChiehWuIntrotoprogramminginPythonandTkinterlecture8](https://archive.org/details/ChiehWuIntrotoprogramminginPythonandTkinterlecture8)

Learn how to use the if statements. Having a program that makes decisions for us will make our life much easier and our programs more powerful. In this program you will decide which girl we should go out with on a friday night and which car we should buy. ![:)](/wiki/europython/img/smile.png ":)")

**You will learn:** How to use if statements, examples are provided

**Example Code** [lecture8_ifexample.py](attachments/Intro(20)to(20)programming(20)with(20)Python(20)and(20)Tkinter/lecture8_ifexample.py)

### Lecture 9: Let\'s create a password system(11min) 

[http://iamar.net/subpages/pythonLect9.html](http://iamar.net/subpages/pythonLect9.html)

Learn how we can use the if statement to create a password system.

**You will learn:** how to focus on a widget, delete and insert text in an entry box, more examples of if else statement

**Example Code** [lecture9_password.py](attachments/Intro(20)to(20)programming(20)with(20)Python(20)and(20)Tkinter/lecture9_password.py)

### Lecture 10: Photo display Part A(15min) 

[http://iamar.net/subpages/pythonLect10.html](http://iamar.net/subpages/pythonLect10.html)

Learn how to create a photo display. The concentration of this lecture is about variables. Talk about the basic types of variables such as integer, float, string, and Booleans. Talk about local and global variables.

**You will learn:** The 4 basic different types of variables.(integer, float, string, boolean), learn the concept of global and local variables. How do you find out what type a variable is, when do you use single or double quotes for strings

**Example Code** [lecture10_pictures.py](attachments/Intro(20)to(20)programming(20)with(20)Python(20)and(20)Tkinter/lecture10_pictures.py)

### Lecture 11: Photo display Part B(9min) 

[http://iamar.net/subpages/pythonLect11.html](http://iamar.net/subpages/pythonLect11.html)

Actually creating the image viewer. We are going to create what I promised last lecture.

**You will learn:** How to use canvas widget to include a gif image, how to delete an image. A real example of the need for global variables.

### Lecture 12: Photo display Part C(9min) 

[http://iamar.net/subpages/pythonLect12.html](http://iamar.net/subpages/pythonLect12.html)

Improving the image viewer we had from the last class. This lecture will start talking about the os library. The 4 types of OS that most people have.

**You will learn:** The 4 types of OS most people use (windows, unix, apple, linux) , How do you find out your OS, How do you list all the files in a specific directory.

### Lecture 13: Photo display Part d (9min) 

[http://iamar.net/subpages/pythonLect13.html](http://iamar.net/subpages/pythonLect13.html)

We start learning about the string library. With these many libraries, you will also learn how to find all the tools inside the library using the IDLE interpreter. In this lecture, I am showing you how to fish.

### Lecture 14: Photo display Part e (9min) 

[http://iamar.net/subpages/pythonLect14.html](http://iamar.net/subpages/pythonLect14.html)

You will learn: We learn about for loops and the concept of range function in this lecture

### Lecture 15: Photo display Part f (9min) 

\[\[[http://iamar.net/subpages/pythonLect15.html](http://iamar.net/subpages/pythonLect15.html)\]

We finish up the project by learning about how to position the widgets inside the window and well as how we can create callback functions

You will learn: pack functions, position functions, grid functions, and callback functions

### Lecture 16: Photo display Part g (9min) 

[http://iamar.net/subpages/pythonLect16.html](http://iamar.net/subpages/pythonLect16.html)

We are now finally getting into more advanced topics such as reading text files. You can find the source code for this lecture at [http://ourmedia.org/node/29741](http://ourmedia.org/node/29741)

### Lecture 17: File reading and writing(9min) 

Here we are going to have a little practice with reading and writing files

Source code for this lecture at [http://www.ourmedia.org/node/32502](http://www.ourmedia.org/node/32502)

### 3D Python Computer graphics 

[http://vpython.erikthompson.com/](http://vpython.erikthompson.com/)

### Chieh\'s Blog and suggestion 

*That\'s incredible! I don\'t have any video equipment at home, but I should have some within 2 years.* \-- [LionKimbro](LionKimbro) 2005-04-15 20:16:00

Instead of making wiki pages named [lecture3 example 1](./lecture3(20)example(20)1.html) and what not, which is begging for a name clash, how about instead posting the files as attachments?

You can type `attachment:foo.txt`, and that becomes a text file attachment.

An example: [lecture3example1.txt](attachments/Intro(20)to(20)programming(20)with(20)Python(20)and(20)Tkinter/lecture3example1.txt)

![:)](/wiki/europython/img/smile.png ":)") \-- [LionKimbro](LionKimbro) 2005-04-27 19:29:44

really good!

\
\
Thanks for putting this information on the web. I wish that there were more poeple doing this type of thing.\
\

![:)](/wiki/europython/img/smile.png ":)") Robert C

Thank you very, very much. Your tutorial is OUTSTANDING! Thank you for the keeping things very simple. Keith Sweat

I\'m just wondering how much time did it take to make these videos. Anyway I like it. And I like your other stuff at ourmedia too.

Levente Zsíros

Good question: Here are the stats

- each video takes about 10 hours of \"actual\" work, (not counting me day dreaming and thinking about some girl)

writing script (3 hours) try to make it coherent ( 1 hour) try to make it fun ( 2 hours) reherse script (1 hour) recording video ( 1 hour) recording audio ( 1 hour) sync up video and audio (30 min) re - edit video (30 min)

watch video

- if i didn\'t like the video repeat above lecture 4 and 5 repeated 3 times lecture 8 repeated 2 times

<!-- -->

- yes, imagine i actually enjoy doing this : )

Question: Chieh would you have a website or email address that people can contact you on? I have a talented friend on dreamweaver8 who **really** enjoys learning python and watching your videos. If you are interested he may be able to put togehter a website for you on a domain, and upload all your videos to the website.

- Reply: Thank you so much for the offer ![:)](/wiki/europython/img/smile.png ":)") I think that is a great idea. The currently effort I am working on (the next series of lectures) will try to merge with it when it is done. One thing to note is that uploading videos are heavy on bandwidth, I hope your friend has enough bandwidth for it.

![:)](/wiki/europython/img/smile.png ":)") Martin

This tutorials are amazing!! Thank you so much for sharing you knowledge and making this tutorials so easy, even for a newbie at programming like myself. It shows all the hard work put in each of the lectures, it shows so much that i\'m getting addicted :). I\'m watching one lecture after the other(on lecture 8 right now) and I\'ve been able to make all the exercises and homework. I\'ve seen lots of video tutorials and this are by far the best. Thanks again, Martin.

Hmm. I can only watch the Flash format, and there it is too small to really follow anything\... \-- [ImperfectlyInformed](./ImperfectlyInformed.html).

- REPLY: it goes to full screen for me, i use linux and windows, i\'m not sure about other operating systems. You can also check out iamar.net , it has the same video posted on other sites which might work better for you.

Hi Chieh,

- These video\'s are great thanks for you time and effort. Zaheer

Hi Chieh,

Your videos are just E X C E L E N T !. Thank you very much for them. I\'m new to programing, and I can tell you that this is the greatest way to learn and enjoy!!!!! Santi

------------------------------------------------------------------------

Hi Chieh,

Can you fix \"lecture10_pictures.py?\" It is messed up. Thxks.

\-\-- Hi Chieh, The website [http://iamar.net/](http://iamar.net/) only shows

- The website you were trying to reach is temporarily unavailable. Please check back soon. If you are the owner of this website, please contact Technical Support as soon as possible.

Anyone have a copy any of the videos and code?
