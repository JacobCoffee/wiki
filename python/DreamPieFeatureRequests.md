# DreamPieFeatureRequests

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page is intended as a place to suggest features for [DreamPie](http://dreampie.sourceforge.net/).

[DreamPie](http://dreampie.sourceforge.net/) is a graphical interactive Python shell which is designed to be reliable and fun. Check it out at [http://dreampie.sourceforge.net/](http://dreampie.sourceforge.net/)

## Richer function documentation 

This is a feature from IPython which is frequently requested. I think that the model should be Eclipse - when you type a paren after a function name it opens a yellow popup window which displays its argument and a bit of documentation, and lets you make it a real window by pressing F2.

## Complete module names 

This was a bug report by cool-RR: [https://bugs.launchpad.net/dreampie/+bug/525610](https://bugs.launchpad.net/dreampie/+bug/525610)

IPython completes module names. That\'s a good idea.

bpython does this too.

## More by cool-RR: Complete things that aren\'t defined yet 

Imagine I\'m writing this function:

    def factorial(n):
        import random
        random.whatever()
        return n * factorial(n-1)

I\'d want [DreamPie](./DreamPie.html) to autocomplete both the `whatever`{.backtick} thing and the use of `factorial`{.backtick} inside the definition. Probably hard, I know.

As you said, this is really hard and complicated. I don\'t see this happening. Sorry! Noam

## Magic commands 

Chris Colbert gave the example of the Ipython\'s %timeit command.

## Shell support 

Probably by prefixing with a \'!\'. some common commands can work without it.

There shouldn\'t be a technical problem, as output from processes created by the subprocess is directed to DreamPie.

## Debugging support 

IPython provides enhanced tracebacks and pdb support. Should check out what this exactly means and what should be implemented.

## Save code history between sessions 

An idea by Regev: save the last executed code sections, so that history search will include those too. It\'s useful if there are lines which are executed many times - for example \'execfile\'.

Another suggestion roughly about the same subject, by Per Dalgaard Rasmussen: On exit, ask whether to save the history.

I (Noam) think that we can use the \"changed\" flag of the text buffer for that - it\'s pretty standard in applications. We should also add a \"recent files\" menu. The only difference from standard apps is that we should warn even if the history was saved, and note that although the history was saved all the variables will be lost.

## Pasting clipboard datas using the mouse middle button 

On Windows with the standard interactive Python shell it\'s very useful to paste clipboard data with a simple mouse right-click.

Since in [DreamPie](./DreamPie.html) the right mouse button is used by the context menu, it\'ll be good to have the same feature with the middle mouse button (or the wheel one).

## Setting the bottom box area height 

The bottom box area have a fixed height at startup. Saving and restoring will be useful.

## Saving window position and size 

Setting window position and size every time is a pain in the neck.

Saving and restoring window position and size at startup will be an appreciate feature.

## Notify new versions 

Let [DreamPie](./DreamPie.html) check and notify if a new version is available at startup (or programmatically).

## Autocomplete keyword arguments 

Imagine I\'m typing this:

    x = sum(my_list, sta

In this case we have the `sum`{.backtick} function, which takes a keyword argument `start`{.backtick}. It\'d be nice if [DreamPie](./DreamPie.html) could autocomplete the keyword argument itself. (Ram \"cool-RR\" Rachum.)

## Behavior of Ctrl+Something not good enough 

I often use ctrl+arrow or ctrl+delete to move through or delete a word. In programmer-friendly editors (Like Wing, Eclipse, Aptana, etc.) this works great. In non-programmer friendly editors (like Notepad, IDLE (shamefully), or textareas in browsers), the cursor often jumps too far in one stroke. Unfortunately it happens in [DreamPie](./DreamPie.html) as well.

## Display version in caption bar on Windows 

On Windows, [DreamPie](./DreamPie.html) creates launch shortcuts for each version of Python on the system. This is great, because it makes [DreamPie](./DreamPie.html) very useful for doing A/B comparisons between versions. It would be even better if the window caption contained the Python version\--for example, instead of just \"[DreamPie](./DreamPie.html)\", \"[DreamPie](./DreamPie.html) - Python 2.7\".

They don\'t automatically contain the version number? Because on my system, they do, and they should. Can you please post a bug report, with the version of [DreamPie](./DreamPie.html) you\'re using? \--Noam

Done: [https://bugs.launchpad.net/dreampie/+bug/610160](https://bugs.launchpad.net/dreampie/+bug/610160) \-- tlesher

## Highlight all occurrences of the word(token) under the caret 

Notepad++ has this feature and I miss it a lot. Very helpful for seeing all uses of a variable, catching misspellings, etc. Should be easy to add.

I agree it\'s a nice feature sometimes, but you know that saying that it\'s easy to add is something that I\'m supposed to say, not you, unless you\'re going to implement it. \--Noam

## Allow cycling through history without ctrl modifier 

Currently [DreamPie](./DreamPie.html) requires the \'ctrl\' key along with up or down arrows to cycle through history. Perhaps this could be done with arrow keys alone like this:

When up arrow pressed:

- if we\'re at the first line in the editing window:
  - show the previous item in history

  else:
  - move cursor up one line

and when down arrow pressed:

- if we\'re at the last line in the editing window:
  - show the next item in history

  else:
  - move cursor down one line

We should retain the current \'ctrl\'-based scheme, too. When the editing window contains several lines, the user can use \'ctrl+arrow\' to immediately move to next or previous history item without having to first scroll through all those lines.

In my view using arrows alone will make the navigation more fluid. Also most new users will already know it because that\'s how all popular shells (of any kind) implement this feature. \-- Gurry

Thanks for the suggestion! However, I don\'t think it will work well with multi-line sections. Say you press \'up\' and you get a multi-line section. Pressing \'down\' will go to the next line, instead of giving you back the last section. I think that up and down should always cancel one another. So I still think that using ctrl is the best solution. \-- Noam

## Let \'esc\' clear the editing window if in the middle of history 

Imagine you\'re going through history items looking for some command and eventually discover it is not there. Now in order to go back to the empty editing window, you have to cycle all the way back. Perhaps it would help in such situations if pressing escape took us back to the end/bottom of the history queue (the empty window that is).

\-- Gurry

Again, thanks for your thought and suggestion! You don\'t need to scroll all the way down - just press ctrl-a (to select all) and the Delete key. I don\'t think it\'s worth to add another shortcut just to keep you two keystrokes, especially since most people won\'t find this feature. \-- Noam

## Color-coding decorators 

It seems that decorators are currently not color-coded. I suggest they should be. (I\'d recommend a gold-like color.) \-- Ram

## Output format handlers 

implement Reinteract like output handlers to customize the console output. I\'ve seen such a feature in Monos csharprepl too where you can hook in a handler. Another quick hack would be to implement a default handler with based on a template engine like jinja, where the output widget is render with a template (model view control like separation) \-- Rainer

## Snippet templates 

another usage for jinjas template would be a snippet like shortcut system for accessing a list of templates to format the bound data \-- Rainer

## Allow bold fonts 

\--Rainer

## docstring shortcut 

shortcut to show the docstring of an object, like ? in IPython

## Line Numbers! 

\--Ilia Zaslavsky

## Automatic code per python version 

In the preferences under the shell tab you are able to set code that automatically executes when an instance of the shell is fired up.

I have different versions of python installed and would like to customize scripts for each version.

A use case is code like \"print()\" which would fail on Python 2.6 \--benjamin

## Two behaviours for path auto-completion 

I love dreampie\'s feature to press tab and get a list to auto-complete the path I\'m currently typing in. I\'d like to see a small tweak, though. Sometimes I have directories with several thousand files which takes extremely long for dreampie to load and put in the auto-completion pop-up. So I suggest the following: When the pop-up list is open, selecting an entry and pressing enter should just fill in that path without following the contents of that directory. Pressing tab on the other hand should fill in that path and scan the contents for further paths that could be followed.

\-- Moritz

## Clear Output 

Very often, I like to clear the interpreter output. Python interpreter provides a Ctrl+L shortcut. In [PythonWin](PythonWin), I can select all text and delete. Can we have something like that (Ctrl+L would be better; not making (or having an option for) the output pane read-only is a substitute). Currently, I can to that if I clear all history. But I would like to retain the history and only clear the output. Also, it would be nice to have an option for a standard history file so that users don\'t need to be prompted to do that for every session.

\-- Ravi

You can press ctrl-minus to fold the last output. I think that\'s good enough. I plan to improve the \"recent files\" in the history menu, so that you\'ll be able to press alt-h, 0 and get the last history you saved.

\-- Noam

\> You can press ctrl-minus to fold the last output. I think that\'s good enough.

Not really (at least for me). Ctrl-Minus only seems to fold output of one statement. I am referring to starting a fresh slate, visually. In any case, if this is not interesting to you, I can always fix that in my copy. Thanks.

\-- Ravi

==Portability==

It would be awesome if the application could be installed and run from an external drive with either its own portable python install or the native one on the computer. Thank you!

\--Jeremiah

## Faster history searching using Ctrl-up/Ctrl-down 

It is nice to have a separate buffer keep track of the previous command for user to call back using Ctrl-up/Ctrl-down. Currently I have to type multiple ctrl-up for a same command to search up from history.

For example

        >>>show_detail()
        >>>increase_by_one()
        >>>increase_by_one()
        >>>increase_by_one()
        >>>increase_by_one()

When I type Ctrl-up, it should show increase_by_one(), then the next Ctrl-up should show show_detail() instead of the same increase_by_one() line.

\-- Shin Guey

## Show tab and space characters symbols 

Sometimes I mix up leading tabs and spaces. This causes errors when running the python code. It is difficult to determine which code lines have the error.

Showing an transparent tab or space character is very helpful in this case.

Checkout Notepad++ for a good implementation of this feature.

\-- [JamesThomasMoon1979](./JamesThomasMoon1979.html)

## Enable manual removal of elements from history 

Sometimes code won\'t work as intended (typo, indexing issue, logical mistake, etc.) and the attempts to correct it might be many. This clutters the history with all sorts of wrong or incomplete or superfluous code.

It would be nice to have a feature to remove all those code snippets that didn\'t work from history. It would make the reuse of previous interactive sessions much easier.

I remember that matlab has this feature.

\-- Thomas

## Collapsed text/code in saved history 

When saving history as HTML, I would like to be able to expand/collapse collapsed text/code as in [DreamPie](./DreamPie.html) itself.
