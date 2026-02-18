# WikiLikeSyntax

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here\'s a way to make wiki-like syntaxes in Python.

## Lines as Tokens 

Usually, you tokenize input word-by-word.

For a wiki-like syntax, it can be easier to go *line by line.*

### Data Flow 

We start with:

    = Hello, world! =
    This is an example.

    We want to demonstrate how you take text with
    multiple lines, and turn it into one paragraph.

\...turn it into\...

:::: 
::: 
``` 
   1 [("HEADER", ("=", " Hello, world! ")),
   2  ("TEXT", ("This is an example.",)),
   3  ("BLANK", ()),
   4  ("TEXT", ("We want to demonstrate how you take text with",)),
   5  ("TEXT", ("multiple lines, and turn it into one paragraph.",)),
   6 ]
```
:::
::::

\...and from there into\...

:::: 
::: 
``` 
   1 [("HEADER", ("=", " Hello, world! ")),
   2  ("PARAGRAPH", ["This is an example."]),
   3  ("BLANK", ()),
   4  ("PARAGRAPH", ["We want to demonstrate how you take text with",
   5                 "multiple lines, and turn it into one paragraph."]),
   6 ]
```
:::
::::

\...and finally into:

    <h1> Hello, world! </h1>
    <p>This is an example.</p>
    <p>We want to demonstrate how you take text with multple lines, and turn it into one paragraph.</p>

### Spec out Types of Lines 

Our first task is to spec out the types of lines that exist.

Use [RegularExpression](../people/RegularExpression)s!

Let\'s start with just three types of lines. (It\'ll be clear how to add more.)

We\'ll have *header lines,* (like in wiki,) *blank lines* (seperating paragraphs,) and *text lines,* which will be anything that doesn\'t match the others.

Examples:

    == Level 2 Heading ==

    Here's paragraph 1.
    Ladee dah dee dah.

    Here's paragraph 2.

    === Level 3 Header ===
    Look, a paragraph without a blank line above it!
    No problem, we can parse it!

Here are our [RegularExpression](../people/RegularExpression)s:

:::: 
::: 
``` 
   1 header = re.compile(r"^(=+)(.+?)\1$")
   2 blank = re.compile(r"^(\s*)$")
   3 text = re.compile(r"^(.+)$")  # if nothing else matched, use this
```
:::
::::

(Note that we store interesting information in regex groups. This is so we can get to it later on.)

This is good to start with. You can add more types now, if you want, though!

### Tokenize a Line 

Now, we\'ll teach Python how to tokenize a line.

It goes like so:

:::: 
::: 
``` 
   1 def tokenize_line(line):
   2     """Tokenize a line, returning the token type and recognized groups."""
   3     mo = header.match(line)
   4     if mo is not None:
   5         return ("HEADER", mo.groups())
   6     mo = blank.match(line)
   7     if mo is not None:
   8         return ("BLANK", mo.groups())
   9     mo = text.match(line)
  10     if mo is not None:
  11         return ("TEXT", mo.groups())
  12     return ("ERROR", "this should never happen")
```
:::
::::

There\'s a pattern in the expression above; If you make a lot of line types, *exploit it.* But it\'s easier for me explaining this to show it all to you unrolled.

Okay! We can tokenize a line.

Next up, read all the lines in a string.

### Tokenize All Lines 

:::: 
::: 
``` 
   1 tokens = [tokenize_line(line) for line in text.split_lines()]
```
:::
::::

Uuuuuuunh-hunh!

Well, that about wraps that one up.

Of course, you\'re going to have to get some text on your own. Not my concern.

## Isolating Paragraphs 

### Lines and Paragraphs 

We\'ve done all the tokenizing. Now comes the trickier part.

We don\'t want text to just be a series of *lines.* If we do that, then we can\'t have anything like the following:

    This is some text with ''some parts
    italic'' and with '''some parts that
    are bold.'''

You see the problem, right? The problem here is that \"some parts italic\" spans *across lines.* If you want your nifty bold-izing, italic-izing, link-izing, whatever-itizing magic substitutions to work on paragraphs, you\'re going to have to transcend *the boundary of the line.*

That, and: We want to put paragraph markers around *paragraphs,* not *every single line they type.*

But we can\'t just be naive, and just work on blank lines; Because, there are headers nestled right against paragraphs, and we want to recognize, \"No, this is a header, and this is a paragraph, and even thought they are sitting right next to one another, they are actually very different things.\"

What we\'re going to do is: Whever text lines follow one another in series- roll that whole thing up into one big paragraph.

### Turn Text into Paragraphs 

There are probably better ways to do this. Please adjust this text here, if you know one. But, this is how I did it.

:::: 
::: 
``` 
   1 def text_to_paragraph(tokens):
   2 
   3     """Group TEXTs into PARAGRAPHs."""
   4 
   5     result = []
   6     texts = []
   7 
   8     for token in tokens:
   9         (token_type, token_groups) = token
  10         if token_type == "TEXT":
  11             texts.append(token_groups[0])
  12         else:
  13             if len(texts) > 0:
  14                 result.append("PARAGRAPH", "".join(texts))
  15                 texts = []
  16             result.append(token)
  17 
  18     if len(texts) > 0:
  19         result.append("PARAGRAPH", ("".join(texts),))
  20         texts = []
  21     return result
  22 
  23 tokens = text_to_paragraph(tokens)
```
:::
::::

There!

Now you have all your texts together!

### Throw Out the Blanks 

Now that we\'ve grouped our text, we can huck our blank lines! They\'ve served their purpose.

:::: 
::: 
``` 
   1 tokens = [x for x in tokens if x[0] != "BLANK"]
```
:::
::::

## Render HTML 

Now we can output some nice HTML. ![:)](/wiki/europython/img/smile.png%20":)")

:::: 
::: 
``` 
   1 def tokens_to_html(tokens):
   2     result = []
   3     for (token_type, token_groups) in tokens:
   4         if token_type == "HEADER":
   5             (level, content) = token_contents
   6             level = len(level)  # Turn == into the number 2
   7             result.append("<h%d>%s</h%d>" % (level, content, level))
   8         elif token_type == "PARAGRAPH":
   9             (text,) = token_groups
  10             result.append("<p>%s</p>" % text)
  11     return "\n".join(result) + "\n"
  12 
  13 print tokens_to_html(tokens)
```
:::
::::

### Celebrate 

Ta-da! That\'s basically it!

\...

So, there\'s some things you might want to do.

## Extensions and Alternatives 

### Escape for HTML 

You might want to escape \< and \> and \" to \< and \> and \" before you output your paragraph text.

There\'s a page on this wiki about how to do it; The mis-named [EscapingHtml](../people/EscapingHtml), or something like that.

### Italics, Bold, Links 

Regexes, my friend, regexes.

But, it\'s a little more complicated, because you have to put \<i\> and \</i\> in the text in matching pairs in your paragraphs, you can\'t just substitute one type in.

The following function may help you, but there ought be a better way.

:::: 
::: 
``` 
   1 def join_by_pairs(lst, start, end):
   2     """
   3     if   lst = [1,2,3,4,5,6,7,8],
   4     and  start = "a" and end = "b",
   5 
   6     result = [1,"a",2,"b",3,"a",4,"b",5,"a",6,"b",7,8]
   7 
   8     Notice that nothing is started that isn't ended.
   9     """
  10     num_links = len(lst)-1
  11     stops_lst = [start,end]*(num_links/2)
  12     result = []
  13     while len(stops_lst)>0:
  14         # add an item from  lst
  15         result.append(lst[0])
  16         lst = lst[1:]
  17         # add an item from  stops_lst
  18         result.append(stops_lst[0])
  19         stops_lst = stops_lst[1:]
  20     # copy over whatever is left
  21     result.extend(lst)
  22     return "".join(result)
```
:::
::::

Use it with this:

:::: 
::: 
``` 
   1 def bold_and_italics(text):
   2     """Perform '''bold''' and ''italics'' replacements.
   3 
   4     Note that, this assumes you've already called html_escape.
   5     """
   6     L = text.split("&apos;&apos;&apos;")
   7     text = join_by_pairs(L, "<b>", "</b>")
   8     L = text.split("&apos;&apos;")
   9     text = join_by_pairs(L, "<i>", "</i>")
  10     return text
```
:::
::::

### Link Patterns 

Link patterns are easier than bold or italic.

:::: 
::: 
``` 
   1 def hyperlink(text):
   2 
   3     """Turn links into <a href>'s."""
   4 
   5     all_links = link_re.findall(text)
   6 
   7     def make_ahref(matchobj):
   8         link_url, link_text = matchobj.groups()
   9         if link_text == "":
  10             link_text = link_url
  11         return '<a href="%s">%s</a>' % (link_url, link_text)
  12 
  13     text = link_re.sub(make_ahref, text)
  14     return text
```
:::
::::

\'Course, you\'ll need a link pattern.

Here\'s one:

:::: 
::: 
``` 
   1 link_regex = r"[[(.+?)](.*?)]"  # As we think it
   2 link_regex = link_regex.replace("[", "\\[")  # [ isn't a character class
   3 link_regex = link_regex.replace("]", "\\]")  # ] isn't a character class
   4 link_re = re.compile(link_regex)
```
:::
::::

That let\'s you write stuff like:

    [[http://freshmeat.net/] Fresh Meat:] Don't worry- it's work safe.

### Regions 

By \"regions,\" I mean things like:

     /*   # Region begins
     ...
     ...
     */   # Region ends

If you want to support *special regions of text,* you might not want line recognition, since the text within the region will parse as something other than \"text-within-this-region.\"

The secret to dealing with regions, by this approach of coding, is to tokenize the entire region *as one line.*

So, make a special regex pattern, and suck up all the lines. This means you\'ll have to go to a positional system of regexing, though, which is a little more complicated than this page explains. But you should be able to figure it out, if you are so motivated.

Hint: Make your tokens of the form: (token_type, token_groups, start_pos, end_pos).

Another alternative is to, in your token, keep track of the original line. Then perform a grouping action, like we did when we grouped text lines into paragraphs. Only here, you\'ll ignore whatever type it thought the token was originally, when you come across the region.

## See Also 

- [TextFilter](http://c2.com/cgi/wiki?TextFilter "Wiki") \-- inventory of text filters like this

## Discussion 

This is how I figured out how to do these things. If you know of better ways, please- by all means, list them here, point to them, or- probably best, just edit this text in-place. ![:)](/wiki/europython/img/smile.png%20":)")

\-- [LionKimbro](../people/LionKimbro) 2005-05-06 20:03:23

A whole book is dedicated to it: [TextProcessingInPython](TextProcessingInPython). But thank you for this page which is very useful. I think that kind of thing should be also directly plugged into the official documentation a bit like the PHP doc. That might help a lot. A full [HowToCreateaWiki](./HowToCreateaWiki.html) with extensive code would be good too. It would help to have a modular architecture of it.

\-- [KarlDubost](../people/KarlDubost)

Here\'s an alternate way to classify lines of text:

    class LineClassifier(object):
      """classify a line according to its type"""

      def __init__(self, table):
        """build a table of tags and regular expressions"""
        self.table = ( (tag, re.compile(str)) for tag, str in table )

      def catagorize(self, line):
        """find the first regex that matches the line"""
        for tag, regex in self.table:
          mo = regex.match(line)
          if mo: return (tag, mo.groups())
        return (None, line)

And here\'s how to use it:

      groups = LineClassifier((
        ('HEADER', r"^(=+)(.+?)\1$"),
        ('BLANK',  r"^\s*$"),
        ('TEXT',   r"^(.+)$"),
        ))

      tokens = [ groups.catagorize(line)
          for line in text.split_lines() ]

The class definition may seem more complicated, but adding a new type of line only requires one line of code (actually, one line of data). For example, here are some more types of lines similar to those used by this wiki:

        ('HR',        r"^----*$"),
        ('LIST_ITEM', r"^ \*\s*(.*)$"),
        ('TABLE_ROW', r"^\|\|(.*)\|\|$"),

Now you just need to add some code to text_to_paragraph to handle the new types of lines; or even better, we could fix things so that runs of one or more XXX_YYY tokens get turned into a single XXX token containing multiple YYY tokens. I\'ll leave that last bit as an exercise for the reader. ![;-)](/wiki/europython/img/smile4.png%20";-)")

\-- [SamDenton3](./SamDenton3.html)

It\'s been almost 3 years now. I have found a better technique for doing wiki-like syntax. I don\'t recall seeing this technique in [TextProcessingInPython](TextProcessingInPython). (I suspect the [RegularExpression](../people/RegularExpression) `(?P<...>)` form didn\'t exist yet.)

The technique involves automatically turning `(?P<...>)` capture results into functions, and then recursing back into regexes.

[Sheep:WikiCreole_parser_in_python](http://oink.sheep.art.pl/WikiCreole_parser_in_python) demonstrates it, and is how I discovered it.

From a high level, the technique is:

\* Make an object that emits parse tree nodes. \* Write your grammar in regular expressions. (One big grammar.) \* Use `(?P<...>)` in your grammar, to name significant parts of the regexes. \* Call `re.sub`, starting with the S production, and instead of substituting with a string, substitute with a function (\"\_replace\", described below.)

**\_replace is the trick.**

\_replace will read off the `(?P<...>)` captures via `match.groupdict()`, and **turn them into function names.** The function names are methods on the object that is emitting the parse tree.

The methods are called, and they use the match object to construct the node. This often times involves calling `re.sub` again on matched context, and this is where the recursive element comes in.

\-- [LionKimbro](../people/LionKimbro)

Note also, that you can use re.finditer instead of re.sub if you want to have a little more control on the flow (for example, if you want to use yield to return partial parse as you go). Here is a nicer `_replace` function:

:::: 
::: 
``` 
   1     def _replace(self, match):
   2         """Process a single match by calling an apropriate _repl method."""
   3 
   4         groups = {}
   5         for name, text in match.groupdict().iteritems():
   6             if text is not None:
   7                 groups[str(name)] = text
   8         for name, text in groups.iteritems():
   9             repl = getattr(self, '%s_repl' % name, None)
  10             if repl:
  11                 return repl(**groups)
```
:::
::::

I use unicode strings, so I had to convert the group names to strings first to use them as argument names. It expects the `_repl` methods to accept keyword arguments named the same as the groups contained in respective patterns. For example:

:::: 
::: 
``` 
   1   pattern = ur"(?P<link>\[\[(?<link_target>[^\]|]+)(|(?P<link_text>[^\]]+))?\]\])"
   2   def link_repl(self, link, link_target, link_text=None):
   3      if link_text is None:
   4          link_text = link_target
   5      return u'<a href="%s">%s</a>' % (cgi.escape(link_target, quote=True), cgi.escape(link_text))
```
:::
::::

Note how the `link_text` group is optional, so the corresponding argument needs a default value. \-- [RadomirDopieralski](../people/RadomirDopieralski)

See also: [Sheep:2007-10-25_Wiki_parser_in_python](http://sheep.art.pl/2007-10-25_Wiki_parser_in_python)

Key techniques:

- dynamic linking by way of `re.sub`

- tree construction via `DocNode`

- re nesting (order & method)

- comfort w/ [RegularExpression](../people/RegularExpression) re.X, re.U, re.M, multilining

questions:

- are the block-level regex\'s huge (representing whole tree) or small (representing tree high level)?
- what\'s a diagram of the nesting look like?

ideas:

- GUI for construction of grammar
- stack match-object groups
- doc-node creation generic / automatic, modification manual; mirror the successful parse
- link not only to functions, but also to other regexes

\-- [LionKimbro](../people/LionKimbro)
