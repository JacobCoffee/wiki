# GoogleGroupsPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Posting from Google Groups 

Many people find reading the comp.lang.python newsgroup / python-list mailing list on [Google Groups](https://groups.google.com/forum/#!forum/comp.lang.python) to be simple and convenient. It is also possible to post messages to the list from there. But please be aware that your message will be read by many people using mail or Usenet clients, not Google Groups. Posts from Google Groups have some problems that may make your post difficult or annoying to read by these other list participants, and all would appreciate it if you would fix them before clicking the Post button.

1\. **Please remove extra blank \"\>\" lines.**

- When you reply to a message Google Groups includes the message you are replying to prefixed (aka \"quoted\") with \"\>\" characters. This context helps the reader of your reply understand what the discussion is about. The problem is that Google Groups adds a number of empty lines with nothing but \"\>\" characters. For example:

      >
      > When I changed it so that it said class Foo(object) it gave me
      >
      > a traceback error when printing out the results. Any ideas?
      >
      > >
      >
      > > The code is at http://somewhere/strange
      >

  When reading messages on Google Groups, such quoted text will often be collapsed in a \"-show quoted text-\" link and not bothersome but others will see them all the time. Reading a message formatted this way is annoying and there are readers who will ignore it or complain about it. You should remove the excess quoted blank lines before posting. There are several way to do this.

  1.  If the quoted text is short, just removed the excess quoted blank lines by hand. (Proper netiquette requires you to remove parts of the quoted text that aren\'t relevant to your reply anyway which will lessen what you need to fix.)
  2.  Open a New Mail Message compose window in your favorite email program. Then copy the text of the original message (not the screwed up quoted message in the Google Groups compose window) and use your email program\'s \"Paste as quotation\" function to paste into the email window. You can then copy and paste the properly quoted message back into the Google Groups post window.
  3.  Do the same as above but with your favorite text editor program and use your editor\'s Replace function to add the quote markers yourself.

  However you do it, the context lines above should end up looking something like:

      > When I changed it so that it said class Foo(object) it gave me
      > a traceback error when printing out the results. Any ideas?
      >
      > > The code is at http://somewhere/strange

  Please do not simply remove all the context \-- in a moderate to high-volume group, context is very important to readers of your post who may have long since forgotten the message you are replying to.

2\. **Please don\'t remove attributions.**

- Attributions are at the top of the context lines and say who posted the message(s) you are replying to. They look like:

      On Saturday, October 26, 2013 7:02:19 AM UTC-6, Ben Finney wrote:
      > On Saturday, October 26, 2013 10:33:10 PM UTC-6, ru...@yahoo.com wrote:

3\. **Not all list readers may see your post.**

- Because of the above problems, the amount of spam posted via Google Groups and other reasons, there are some regular and knowledgeable list participants that filter out posts made from Google Groups. It is not clear that more than a few people do this and most posters from Google Groups get good responses. If you want every possible person to see your post you may want to try posting using one of the other methods described in [CompLangPython](CompLangPython).

4\. **Follow accepted mailing list netiquette.** These are conventions that all posters should try to follow, they are not specific to Google Groups posters. See for example [http://linux.sgms-centre.com/misc/netiquette.php](http://linux.sgms-centre.com/misc/netiquette.php). Three in particular often complained about when ignored are:

- Please don\'t top post. Either put your reply text below any context text, not above it, or interleave your reply text within the context text by inserting each part of your reply immediately below the particular part of the context text to which it applies.

- Please don\'t type in lines longer than about 70 characters or so; type your \<enter\> key when your line gets around that length. Older mail clients and the Python maillist archives won\'t automatically wrap such long lines making them hard for others to read. Exceptions of course are things like long urls which would be broken by manually wraping, or quoted text (you are responsible for your text, not that of others.)

- Remove (trim) context that is not relevant to your reply.

# Automatic correction 

::: caution
This section is as yet experimental
:::

The following is one way of automatically correcting two of GG\'s nuisances:

1.  Double spacing quoted blocks
2.  Excessively long lines

Please note that

- It has mostly been tested out on linux, though windows also seems to work
- Browser used was firefox
- No experience with macs so far or other browsers
- Assumes a python executable is available

## Instructions 

1\. Install the firefox plugin [Its all text](https://addons.mozilla.org/en-US/firefox/addon/its-all-text/)

2\. Save the script below as a python file say `~/clean-gg.py` and make it executable. Also adjust the python3 first line to whatever is your executable

:::: 
::: 
``` 
   1 #!/usr/bin/env python3
   2 
   3 # As far as I know both python2 and 3 work
   4 # Windows/Mac no idea :-)
   5 
   6 # A script to drop-in as an editor for firefox addon "Its all text"
   7 # It cleans up two google-group nuisances:
   8 # 1. Useless blank lines
   9 # 2. Excessively long lines
  10 # No efforts at error reporting as stderr is not available in any
  11 # easy way (I know) to firefox (other browsers?)
  12 # To test separately:
  13 # Compose a mail (preferably reply) in GG
  14 # Copy-paste the stuff (maybe with some long lines added without the >)
  15 # Run this script with that filename as argv[1]
  16 
  17 from sys import argv
  18 from re import sub
  19 import re
  20 
  21 # Clean double spacing
  22 def cleands(s):
  23     # Assumption: ASCII 025 (NAK) never occurs in input
  24     s1 = sub("^> *\n> *$", "\025"  , s , flags=re.M)
  25     s2 = sub("^> *\n"    , ""      , s1, flags=re.M)
  26     s3 = sub("\025\n"    , ">\n"   , s2, flags=re.M)
  27     return s3
  28 
  29 # Maximum length that (new) lines should attain
  30 Maxlen = 75
  31 
  32 # clean all long lines, s is the whole file/text
  33 def cleanall_ll(s):
  34     lines = (cleanll(l) for l in s.split("\n"))
  35     return "\n".join(lines)
  36 
  37 # clean one long line
  38 def cleanll(line):
  39     return ( line if line.startswith(">") else cleanll_rec(line) )
  40 
  41 def cleanll_rec(line):
  42     if len(line) <= Maxlen : return line
  43     pos = line.rfind(" ", 0, Maxlen)
  44     if pos == -1 : #Failed due to no spaces
  45         return line
  46     return line[0:pos] + "\n" + cleanll_rec(line[pos+1: ])
  47 
  48 def clean(s):
  49     return cleanall_ll(cleands(s))
  50 
  51 def main():
  52     with open(argv[1])      as f: s = f.read()
  53     with open(argv[1], "w") as f: f.write(clean(s))
  54 
  55 if __name__ == '__main__' :
  56     main()
```
:::
::::

3\. In firefox go to the tools → addons → extensions → Its all text preferences and set the editor to `~/clean-gg.py` (expanding \~ to your actual home directory)

## Usage 

After the above, in firefox, when editing a text box in google groups a small edit button should appear at bottom right of text box.

Clicking on it does two cleanups:

- a\. Removing double-spacing of old quoted text
- b\. Wrapping newly written lines after 70 columns

So the optimal way of using it is

1.  After clicking reply, first click edit to clean-up (a)
2.  Trim what is not relevant to your post
3.  Write your comments at the appropriate place
4.  Click edit again to clean up the long lines (b)
5.  Post!

In short you need do 2 clicks more than what you would otherwise do.

For fresh posts (not replys) you dont need the first click as there is nothing to clean up.

## Windows 

::: caution
Not really tested on windows
:::

Evidently Its all text only accepts \'executables\' for editors. Putting the following into a bat file and pointing Its all text to that seems to work.

    pythonw c:\clean-gg.py %1
