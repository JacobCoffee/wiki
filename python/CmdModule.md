# CmdModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The `cmd` module makes it easy to make command line interfaces in your programs.

`cmd` is different than [OptParse](OptParse), in that [OptParse](OptParse) is a tool for making command line tools.

`cmd`, on the other hand, makes it so you can embed a command line within your program.

In these days of graphical user interfaces, a command line interpreter seems antique. I agree that GUIs are often more friendly (and in fact I\'m happy to have something other than \"ed\" to create this document). But a command line interface can have several advantages:

- **portability** almost any computer is able to drive a text terminal, so a command line interface can really run everywhere.

- **resources** the CPU and memory cost of a command line interface is far lighter than a GUI library.

- **speed** for advanced users, it\'s often faster to type a command than to dive into menus and windows.

- **development** It is far faster to create a text oriented interface.

- **driving** you can easily drive a text oriented program with the popen command. That means that the whole application can be tested automatically.

And even if you plan to create GUI software, it\'s often good to start with a text interface. This will allow you to focus on the applicative logic independently of the interface. This is often a good way to create modular software.

# cmd module basics 

The module defines only one class: the `Cmd` class. Creating a command line interpreter is done by sub-classing the `cmd.Cmd` class.

## Creating a command 

The main goal of an interpreter is to respond to commands. A command is the first part of a line of text entered at the interpreter prompt. This part is defined as the longest string of characters contained in the `identchars` member. By default `identchars` contains non accented letters, digits and the underscore symbol. The end of the line is the command\'s parameters.

Command handling is really easy: if you want to define the command spam, you only have to define the `do_spam` method in your derived class.

### parameters

The `do_xxx` method should only take one extra parameter. This parameter corresponds to the part of the string entered by the user after the command name. The job of `do_xxx` is to parse this string and to find the command parameter\'s values. Python provides many helpful tools to parse this string, but this is quite out of the scope of his how-to.

### errors

The interpreter uses the following format to signal errors:

    *** <error description>: <additional parameters>

It\'s generally a good idea to use the same format for application errors.

### return value 

In the most common case: commands shouldn\'t return a value. The exception is when you want to exit the interpreter loop: any command that returns a true value stops the interpreter.

### sample

The following function defines a command which takes two numerical arguments and prints the result of the addition:

    def do_add(self,s):
        l = s.split()
        if len(l)!=2:
           print "*** invalid number of arguments"
           return
        try:
           l = [int(i) for i in l]
        except ValueError:
           print "*** arguments should be numbers"
           return
        print l[0]+l[1]

Now if you run the interpreter, you will have:

    (Cmd) add 4
    *** invalid number of arguments
    (Cmd) add 5 4
    9

## Help 

Help support is another strength of the cmd module. You can provide documentation for the xxx command by defining the `help_xxx` method. For the add command, you could for example define:

    def help_add(self):
        print 'add two integral numbers'

And then, in the interactive interpreter you will have:

    (Cmd) help add
    add two integral numbers

You can also define help for topics that are not related to commands:

    def help_introduction(self):
        print 'introduction'
        print 'a good place for a tutorial'

The interpreter understands the ? character as a shortcut for the help command.

## Completion 

Completion is a very interesting feature: when the user presses the TAB key, the interpreter will try to complete the command or propose several alternatives. Completion will be available only if the computer supports the readline module. You can disable completion by passing the None value to the completekey attribute of the Cmd class constructor.

The interpreter is able to process completion for commands names, but for commands arguments you will have to help it. For the command xxx, this is done by defining a `complete_xxx` method. For example, if you have defined a color command, the completion method for this command could be:

    _AVAILABLE_COLORS = ('blue', 'green', 'yellow', 'red', 'black')
    def complete_color(self, text, line, begidx, endidx):
        return [i for i in _AVAILABLE_COLORS if i.startswith(text)]

The `complete_xxx` method takes four arguments:

- **text** is the string we are matching against, all returned matches must begin with it

- **line** is is the current input line

- **begidx** is the beginning index in the line of the text being matched

- **endidx** is the end index in the line of the text being matched

It should return a list (possibly empty) of strings representing the possible completions. The arguments begidx and endidx are useful when completion depends on the position of the argument.

## Starting the interpreter 

Once you have defined your own interpreter class, the only thing left to do is to create an instance and to call the mainloop method:

    interpreter = MyCmdInterpreter()
    interpreter.cmdloop()

In python 2.1 and 2.2 (and possibly some older, as well as future releases?) mainloop() has been renamed to cmdloop()

# Interface customization 

The cmd module provides several hooks to change the behavior of the interpreter. You should note that your users won\'t necessary thank you should you deviate from the standard behavior.

## Empty lines 

By default when an empty line is entered, the last command is repeated. You can change this behavior by overriding the `emptyline` method. For example to disable the repetition of the last command:

    def emptyline(self):
        pass

## Help summary 

When the help command is called without arguments, it prints a summary of all the documentation topics:

    (Cmd) help
    Documented commands (type help <topic>):
    ========================================
    EOF add exit macro shell test
    Miscellaneous help topics:
    ==========================
    intro
    Undocumented commands:
    ======================
    line help
    (Cmd)

This summary is separated into three parts:

- **documented commands** are commands which have `help_xxx` methods

- **miscellaneous help topics** contain the `help_xxx` methods without `do_xxx` methods

- **undocumented commands** contain the `do_xxx` methods without `help_xxx` methods

You can customize this screen with several data members:

- `self.ruler` define the character used to underline section titles

- `self.doc_header ` define the title of the *documented commands* section

- `self.misc_header ` define the title of the *miscelleanous help topics* section

- `self.undoc_header ` define the title of the *undocumented commands* section

## Introduction message 

At startup, the interpreter print the `self.intro` string. This string can be overridden via an optional argument to the `cmdloop()` method.

# Advanced material 

## Defaults handling 

- The `default` method can be overridden for handling commands for which there is no `do_xxx` method

- The `completedefault` method may be overridden to intercept completion for commands that have no `complete_xxx` methods.

Theses methods have the same parameters as the `do_xxx` and `complete_xxx` methods.

## Nested interpreters 

If your program becomes complex, or if your data structure is hierarchical, it can be interesting to define nested interpreters (calling an interpreter inside an other interpreter). In that case, I like having a prompt like:

    (Cmd) test
    (Cmd:Test) exit
    (Cmd)

You can do this by changing the prompt attribute of the nested interpreter:

    def do_test(self, s):
        i = TestCmd()
        i.prompt = self.prompt[:-1]+':Test)'
        i.cmdloop()

Note that it can be a better practice to do this in the constructor of the nested interpreter.

## Modal interaction 

Sometimes, it can be useful to have a more directed, interactive session with the users. The Cmd class allows you to use the `print` and `raw_input` functions without any problems:

    def do_hello(self, s):
        if s=='':
            s = raw_input('Your name please: ')
        print 'Hello',s

*FIXME: How to change completion behavior of raw_input?*

## The interpreter loop 

At the start of the interpreter loop the preloop method is called, and at the end of the loop the postloop method is called. These methods take no arguments, and return no values. The following shows how to make the interpreter more polite:

    class polite_cmd(cmd.Cmd,object):
        def preloop(self):
            print 'Hello'
            super(polite_cmd,self).preloop()
        def postloop(self):
            print 'Goodbye'
            super(polite_cmd,self).postloop()

## Command processing 

When a command line is processed, several methods are called:

- `precmd` method is called with the string corresponding to the line entered at the interpreter prompt as its argument, and returns a string which will be used as the parameter to the onecmd method.

- `onecmd` takes the return value of precmd and returns a boolean value (True will stop the interpreter). This is this method which does the real work: extracting the command, finding the corresponding do_xxx method and calling it.

- `postcmd` this method takes two parameters: the return value of the onecmd method and the string returned by precmd, and should return a true value to exit the interpreter loop.

The precmd and postcmd methods do nothing by default and are only intended as hooks for derived classes. In fact, with the Python 2.2 super method, they are useless because anything can be done by overriding the onecmd method, so you should probably avoid to use these two hooks:

    class dollar_cmd(cmd.Cmd, object):
        def onecmd(self, line):
            ''' define $ as a shortcut for the dollar command
                and ask for confirmation when the interpreter exit'''
            if line[:1] == '$':
                line = 'dollar '+line[1:]
            r = super (dollar_cmd, self).onecmd(line)
            if r:
                r = raw_input('really exit ?(y/n):')=='y'
            return r

However, if you want to simulate an interpreter entry, you should call these three methods in the proper order. For example if you want to print the help message at startup:

    interpreter = MyCmdInterpreter()
    l = interpreter.precmd('help')
    r = interpreter.onecmd(l)
    r = interpreter.postcmd(r, l)
    if not r:
        interpreter.mainloop()

This will prevent problems if you later want a class to inherit one which has modified the hooks.

## Creating components 

One other strengths of the cmd module is that it handles multiple inheritance. That means that you can create helper classes intended to provide additional features.

### Shell access 

    import os
    class shell_cmd(cmd.Cmd,object):
        def do_shell(self, s):
            os.system(s)
        def help_shell(self):
            print "execute shell commands"

By deriving from this class, you will be able to execute any shell command:

    (Cmd) shell date
    Thu Sep 9 08:57:14 CEST 2002
    (Cmd) ! ls /usr/local/lib/python2.2/config
    Makefile Setup.config config.c install-sh makesetup Setup
    Setup.local config.c.in libpython2.2.a python.o

By the way, the cmd module understands the ! character as a shortcut for the shell command.

### Exit 

    class exit_cmd(cmd.Cmd,object):
        def can_exit(self):
            return True
        def onecmd(self, line):
            r = super (exit_cmd, self).onecmd(line)
            if r and (self.can_exit() or
               raw_input('exit anyway ? (yes/no):')=='yes'):
                 return True
            return False
        def do_exit(self, s):
            return True
        def help_exit(self):
            print "Exit the interpreter."
            print "You can also use the Ctrl-D shortcut."
        do_EOF = do_exit
        help_EOF= help_exit

This class provides the exit command to abort the interpreter. You can protect exit by overriding the can_exit method.

### Gluing all together 

Now with a class that inherits both from `exit_cmd` and `shell_cmd` you will be able to define an interpreter that understands the shell and exit commands.

# References 

[cmd module reference](http://www.python.org/doc/current/lib/Cmd-objects.html)

# Example Code 

[listcmd.py](https://github.com/agroszer/komodo-python-dbgp/blob/master/dbgp/listcmd.py) - from Komodo Remote Debugger

# Discussion 

It would be cool if you could call these mini-command lines from \"the\" command line.

If there were some sort of default [OptParse](OptParse)-like behavior, that would totally rock.

That way, I could pass in instructions, scripts, and get back the results on stdout.

Something like \"-c\" for Python, where you can pass in a line, and get back the result, without seeing the intro text.

\-- [LionKimbro](LionKimbro) 2006-03-06 19:06:56

The `onecmd()` function may be what you\'re after. Write your interpreter as you normally would. Then, in main, parse the command line for a \'-c\' option. If you find it, call `onecmd()` with the string following the \'-c\' as the parameter, else call `cmdloop()`.

\-- Mark Workman 2026-02-14 16:07:16
