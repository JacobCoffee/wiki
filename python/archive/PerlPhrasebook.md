# PerlPhrasebook

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Introduction 

This phrasebook contains a collection of idioms, various ways of accomplishing common tasks, tricks and useful things to know, in Perl and Python side-by-side. I hope this will be useful for people switching from Perl to Python, and for people deciding which to choose. The first part of the phrasebook is based on Tom Christiansen\'s [Perl Data Structures Cookbook](http://www.perl.com/perl/pdsc/).

I have only been working on this for a short time, so many of the translations could probably be improved, and the format could be greatly cleaned up.

I will get the data-structures cookbook translated first and then go back to clean up the code. Also, since I have been using Python for far less time than Perl, there are certainly idioms I don\'t know or that I will misuse. Please feel free to fix and update.

\--

Other references: [PLEAC](http://pleac.sourceforge.net/).

\--

Thanks to David Ascher, Guido van Rossum, Tom Christiansen, Larry Wall and Eric Daniel for helpful comments.

\--

TODO:

- break up into multiple smaller pages
- use modern Python idioms
- use modern Perl idioms
- add more points of comparison
- Use sorted() where appropriate
- Get rid of map() where possible.
- Simple types (strings, lists, dictionaries, etc.)
- Common tasks (reading from a file, exception handling, splitting strings, regular expression manipulation, etc.)
- Sections 4 and 5 of the Perl Data Structures Cookbook.
- Vertical whitespace needs fixing.

QUESTIONS:

- Should function and data structure names for python code be in python_style (and more appropriate/informative)?

## The obvious 

Python don\'t need no steenking semicolons.

## The not so obvious 

There are many Integrated Development Environments, (IDEs), for Python that are usually recommended to new users and used by seasoned Python programmers alike. The Idle IDE is a TK based GUI providing language-aware editing, debugging and command line shell for Python that is part of the Python distribution. Many of the python examples shown can be experimented with in the Idle IDE.

## Simple types 

### Strings 

#### Creating a string 

    $s = 'a string';

    s = 'a string'

The `$`{.backtick} in Perl indicates a scalar variable, which may hold a string, a number, or a reference. There\'s no such thing as a string variable in Python, where variables may *only* hold references.

- You can program in a Pythonesque subset of Perl by restricting yourself to scalar variables and references. The main difference is that Perl doesn\'t do implicit dereferencing like Python does.

#### Quoting 

    $s1 = "some string";
    $s2 = "a string with\ncontrol characters\n";
    $s3 = 'a "quoted" string';
    $s4 = "a 'quoted' string";
    $s5 = qq/a string with '" both kinds of quotes/;
    $s6 = "another string with '\" both kinds of quotes";
    $s7 = 'a stri\ng that au\tomatically escapes backslashes';

    foreach my $i ($s1, $s2, $s3, $s4, $s5, $s6, $s7)
    {
      print "$i\n";
    }

    s1 = "some string"
    s2 = "a string with\ncontrol characters\n"
    s3 = 'a "quoted" string'
    s4 = "a 'quoted' string"
    s5 = '''a string with '" both kinds of quotes'''
    s6 = "another string with '\" both kinds of quotes"
    s7 = r"a stri\ng that au\tomatically escapes backslashes"

    for i in (s1, s2, s3, s4, s5, s6, s7):
      print(i)

In both languages, strings can be single-quoted or double-quoted. In Python, there is no difference between the two except that in single- quoted strings double-quotes need not be escaped by doubling them, and vice versa. In Perl, double-quoted strings have control characters and variables interpolated inside them (see below) and single-quoted strings do not.

Both languages provide other quoting mechanisms; Python uses triple quotes (single or double, makes no difference) for multi-line strings; Python has the `r` prefix (`r"some string"` or `r'some string'` or `r"""some string"""` or `r'''some string'''`) to indicate strings in which backslash is automatically escaped \-- highly useful for regular expressions. Perl has very elaborate (and very useful) quoting mechanisms; see the operators `q`, `qq`, `qw`, `qx`, etc. in the [PerlManual](./PerlManual.html).

Quoting is definitely one of the areas where Perl excels.

Note that in Perl you can always replace `foreach`{.backtick} with `for`{.backtick}, which is shorter; but explicitly writing `foreach`{.backtick} is clearer, so you don\'t confuse it with the other kind of `for`{.backtick}.

#### Interpolation 

    $name    = "Fred";
    $header1 = "Dear $name,";
    $title   = "Dr.";
    $header2 = "Dear $title $name,";

    print "$header1\n$header2\n";

    name = "Fred"
    header1 = f"Dear {name},"
    title = 'Dr.'
    header2 = f'Dear {title} {name},'  # Single quote f-strings also interpolate.

    print(f"{header1}\n{header2}")  # Don't need final \n.

Perl\'s interpolation is slightly more convenient (don\'t need a special string modifier), though slightly less powerful than Python\'s `%`{.backtick} operator. Remember that in Perl variables are interpolated within double-quoted strings, but not single-quoted strings.

Perl has a function `sprintf`{.backtick} that uses the % conversion á la C; so the above lines could have been written:

    $name    = "Fred";
    $header1 = sprintf "Dear %s,", $name;
    $title   = "Dr.";
    $header2 = sprintf "Dear %s %s,", $name, $title;

Python\'s `%`{.backtick} (format) operator is generally the way to go when you have more than minimal string formatting to do (you can use `+`{.backtick} for concatenation, and `[:]`{.backtick} for slicing). It has three forms. In the first, there is a single `%`{.backtick} specifier in the string; the specifiers are roughly those of C\'s sprintf. The right-hand side of the format operator specifies the value to be used at that point:

    x = 1.0/3.0
    s = 'the value of x is roughly %.4f' % x

If you have several specifiers, you give the values in a list on the right hand side:

    x = 1.0/3.0
    y = 1.0/4.0
    s = 'the value of x,y is roughly %.4f,%.4f' % (x, y)

Finally, you can give a name and a format specifier:

    x = 1.0/3.0
    y = 1.0/4.0
    s = 'the value of x,y is roughly %(x).4f,%(y).4f' % vars()

The name in parentheses is used as a key into the dictionary you provide on the right-hand side; its value is formatted according to the specifier following the parentheses. Some useful dictionaries are `locals()`{.backtick} (the local symbol table), `globals()`{.backtick} (the global symbol table), and `vars()`{.backtick} (equivalent to `locals()`{.backtick} except when an argument is given, in which case it returns `arg.__dict__`).

[PEP215](http://www.python.org/peps/pep-0215.html) proposed a `$"$var"` substitution mode as an alternative to `"%(var)s" % locals()`, but was rejected in favour of the explicit Template class proposed in [PEP292](http://www.python.org/peps/pep-0292.html), which required no syntax changes.

#### Modifying a string 

    $s1 = "new string";        # change to new string
    $s2 = "new\nstring\with\nnew\nlines"; # change to new string
    $s2 =~ s/\n/[newline]/g;   # substitute newlines with the text "[newline]"
    $s2 = substr $s2, 0, 3,''; # extract the first 3 chars: "new"

    print "$s1\n$s2\n";

    s1 = "new string"          # change to new string
                               # substitute newlines with the text "[newline]"
    s2 = s2.replace("\n", "[newline]")
    s2 = s2[:3]

    print(f"{s1}\n{s2}")

In Perl, strings are mutable; the third assignment modifies `s2`{.backtick}. In Python, strings are immutable, so you have to do this operation a little differently, by slicing the string into the appropriate pieces.

A Python string is just an array of characters, so all of the array operations are applicable to strings. In particular, if `a`{.backtick} is an array, `a[x:y]`{.backtick} is the slice of `a`{.backtick} from index `x`{.backtick} up to, but not including, index `y`{.backtick}. If `x`{.backtick} is omitted, the slice starts at the beginning of the array; if `y`{.backtick} is omitted, the slice ends at the last element. If either index is negative, the length of the array is added to it. So a\[-4:\] is the last four characters of a.

In Perl, slicing is performed by giving the array a list of indices to be included in the slice. This list can be any arbitrary list and by using the range operator `...`{.backtick}, you can get Python like slicing. If any of the indices in the list is out of bounds an `undef`{.backtick} is inserted there.

    @array = ('zero', 'one', 'two', 'three', 'four')

    # slicing with range operator to generate slice index list
    @slice = @array[0..2]  # returns ('zero', 'one', 'two')

    # Using arbitary index lists
    @slice = @array[0,3,2] # returns ('zero', 'three', 'two')
    @slice = @array[0,9,1] # returns ('zero', undef, 'one')

Note: Perl range operator uses a closed interval. To get the range to the end of the array, the last index must be used as

    @a=(1,2,3,4,5);
    $#a;           # last index, 4, because the firs index is 0 as in Python.
    @a[ 2..$#a ]   # as Python's a[2:]

## Importing 

In Perl a module is simply a package with a package name. ( see: perldoc -f package ). The symbols exported by the module depends on the module itself. The module may export symbols - mostly functions - by default, on request or none of them. In the latter case the module usually a class or has special access, like File::Spec. In Perl the module interfaces may vary - see the doc of the particular module.

    use Module;  # imports module. It module exports symbols by default, those appeare in the package namespace.

    use Module qw(symbol1 symbol2 symbol3); # preferred
    or
    use Module "symbol1";

    from module import symbol1, symbol2, symbol3

    # Allows mysymbol.func()
    from module import symbol1 as mysymbol

    # Unless the module is specifically designed for this kind of import, don't use it
    from module import *

    module.func()

## Common tasks 

### Reading a file as a list of lines 

    my $filename = "cooktest1.1-1";
    open my $f, $filename or die "can't open $filename: $!\n";
    @lines = <$f>;

    filename = "cooktest1.1-1"
    f = open(filename) # Python has exceptions with somewhat-easy to
                       # understand error messages. If the file could
                       # not be opened, it would say "No such file or
                       # directory: %filename" which is as
                       # understandable as "can't open $filename:"
    lines = f.readlines()

In Perl, variables are always preceded by a symbol that indicates their type. A `$`{.backtick} indicates a simple type (number, string or reference), an `@`{.backtick} indicates an array, a `%`{.backtick} indicates a hash (dictionary).

In Python, objects must be initialized before they are used, and the initialization determines the type. For example, `a = []`{.backtick} creates an empty array `a`{.backtick}, `d = {}`{.backtick} creates an empty dictionary.

### looping over files given on the command line or stdin 

The useful Perl idiom of:

    while (<>) {
        ...                 # code for each line
    }

loops over each line of every file named on the commandline when executing the script; or, if no files are named, it will loop over every line of the standard input file descriptor.

The Python fileinput module does a similar task:

    import fileinput
    for line in fileinput.input():
        ...                 # code to process each line

The fileinput module also allows inplace editing or editing with the creation of a backup of the files, and a different list of files can be given instead of taking the command line arguments.

In more recent python versions, files can act as iterators, so you would just write:

    for line in open(filename):
        ...                 # code to process each line

If you want to read from standard in, then use it as the filename:

    import sys
    for line in open(sys.stdin):
        ...                 # code to process each line

If you want to loop over several filenames given on the command line, then you could write an outer loop over the command line. (You might also choose to use the fileinput module as noted above).

    import sys
    for fname in sys.argv[1:]
        for line in open(fname):
            ...                 # code to process each line

## Some general comparisons 

This section is under construction; for the moment I am just putting random notes here. I will organize them later.

- Perl\'s regular expressions are much more accessible than those of Python being embedded in Perl syntax in contrast to Pythons import of its re module.

- Perl\'s quoting mechanisms are more powerful than those of Python.

- I find Python\'s syntax much cleaner than Perl\'s

- I find Perl\'s syntax too flexible, leading to silent errors. The -w flag and `use strict`{.backtick} helps quite a bit, but still not as much as Python.

- I like Python\'s small core with a large number of standard libraries. Perl has a much larger core, and though many libraries are available, since they are not standard, it is often best to avoid them for portability.

While most of the concerns are subjective here this one is obviously wrong. Perl has standard modules - eg. File::Spec -, and in general the module portability does not second to Python\'s. On the other hand, the CPAN - central module library - is a central module repository with elaborat interfaces.

- Python\'s object model is very uniform, allowing you, for example, to define types that can be used wherever a standard file object can be used.

- Python allows you to define operators for user-defined types. The operator overloading facility in Perl is provided as an add-on\-\--the `overload`{.backtick} module.

## Lists of lists 

The Perl code in this section is taken, with permission, almost directly from Tom Christiansen\'s [Perl Data Structures Cookbook](http://www.perl.com/perl/pdsc/), part 1, release 0.1, with a few typos fixed.

### Lists of lists: preliminaries 

    sub printSep { print "=" x 60, "\n" }

    sub printLoL
    {
      my ($s, $lol) = @_;
      print "$s\n";
      foreach my $l (@$lol) {
        print "@{$l}\n";
      }
      printSep();
    }

    # which is longhand for:
    sub printLoL {
      print "$_[0]\n";
      print "@$_\n" foreach @{$_[1]};
      printSep();
    }

    # or even:
    sub printLoL {
      print "$_[0]\n", map("@$_\n" , @{$_[1]}), "=" x 60, "\n";
    }

    # return numeric (or other) converted to string
    sub somefunc { "". shift }

    def printSep():
        print('=' * 60)

    def printLoL(s, lol):
        out = [s] + [" ".join(str(elem)) for elem in lol]
        print("\n".join(out))
        printSep()

    def somefunc(i):
        return str(i)  # string representation of i

`printLoL`{.backtick} pretty-prints a list of lists.

`printSep`{.backtick} prints a line of equal signs as a separator.

`somefunc`{.backtick} is a function that is used in various places below.

#### Lost in the translation 

In converting Perl examples so directly to Python, whilst initially useful, the casual browser should be aware that the task of `printLoL` is usually accomplished by just

      print lol

As Python can print default string representations of all objects.

An import of the pprint at the beginning of a module would then allow

      pprint(lol)

to substitute for all cases of printLol in a more \'pythonic\' way. (`pprint` gives even more formatting options when printing data structures).

### requires/imports 

    import sys

Perl\'s `use`{.backtick} is roughly equivalent to Python\'s `import`{.backtick}.

Perl has much more built in, so nothing here requires importing.

- \"Some people, when confronted with a problem, think \'I know, I\'ll use regular expressions.\' Now they have two problems.\" - Jamie Zawinski

For many simple operations, Perl will use a regular expression where Pythonic code won\'t. Should you really need to use regular expressions, import the `re`{.backtick} module.

### Declaration of a list of lists 

    @LoL = (
           [ "fred", "barney" ],
           [ "george", "jane", "elroy" ],
           [ "homer", "marge", "bart" ],
         );
    @LoLsave = @LoL; # for later

    printLoL 'Families:', \@LoL;

    LoL = [["fred", "barney"],
           ["george", "jane", "elroy"],
           ["homer", "marge", "bart"]]
    LoLsave = LoL[:] # See comment below

    printLoL('Families:', LoL)

In Python, you are always dealing with references to objects. If you just assign one variable to another, e.g.,

    a = [1, 2, 3]
    b = a

you have just made `b`{.backtick} refer to the same array as `a`{.backtick}. Changing the values in `b`{.backtick} will affect `a`{.backtick}.

Sometimes what you want is to make a copy of a list, so you can manipulate it without changing the original. In this case, you want to make a new list whose elements are copies of the elements of the original list. This is done with a full array slice \-\-- the start of the range defaults to the beginning of the list and the end defaults to the end of the list, so

    a = [1, 2, 3]
    b = a[:]

makes a separate copy of a.

Note that this is not necessarily the same thing as a deep copy, since references in the original array will be shared with references in the new array:

    a = [ [1, 2, 3], [4, 5, 6] ]
    b = a[:]
    b[0][0] = 999
    print(a[0][0])   # prints 999

You can make a deep copy using the copy module:

    import copy

    a = [[1, 2, 3], [4, 5, 6]]
    b = copy.deepcopy(a)
    b[0][0] = 999
    print(a[0][0])   # prints 1

### Generation of a list of lists 

#### Reading from a file line by line 

    open my $f, "cookbook.data1" or die $!;
    my @LoL;
    while (<$f>) {
      push @LoL, [ split ];
    }
    printLoL "read from a file: ", \@LoL;

    LoL = []
    for line in open('cookbook.data1'):
        LoL.append(line[:-1].split())
    printLoL('read from a file: ', LoL)

Unless you expect to be reading huge files, or want feedback as you read the file, it is easier to slurp the file in in one go.

In Perl, reading from a file-handle, e.g., `<STDIN>`{.backtick}, has a context-dependent effect. If the handle is read from in a scalar context, like `$a = <STDIN>;`{.backtick}, one line is read. If it is read in a list context, like `@a = <STDIN>;`{.backtick}the whole file is read, and the call evaluates to a list of the lines in the file.

#### Reading from a file in one go 

    open my $f, "cookbook.data1" or die $!;
    @LoL = map [split], <$f>;
    printLoL "slurped from a file: ", \@LoL;

    LoL = [line[:-1].split() for line in open('cookbook.data1')]
    printLoL("slurped from a file: ", LoL)

Thanks to Adam Krolnik for help with the Perl syntax here.

### Filling a list of lists with function calls 

    foreach my $i ( 0 .. 9 ) {
        $LoL[$i] = [ somefunc $i ];
    }
    printLoL("filled with somefunc:", \@LoL);

    LoL = [0] * 10  # populate the array -- see comment below

    for i in range(10):
      LoL[i] = somefunc(i) # assuming that somefunc(i) returns the list that we want

    printLoL('filled with somefunc:', LoL)

Or:

    LoL = []

    for i in range(10):
      LoL.append( somefunc(i) )

    printLoL('filled with somefunc:', LoL)

Alternatively, you can use a list comprehension:

    LoL = [somefunc(i) for i in range(10)]
    printLoL('filled with somefunc:', LoL)

In python:

- You have to populate the matrix \-- this doesn\'t happen automatically in Python.
- It doesn\'t matter what type the initial elements of the matrix are, as long as they exist.

### Filling a list of lists with function calls, using temporaries 

    foreach my $i (0..9) {
        @tmp = somefunc $i;
        $LoL[$i] = [ @tmp ];
    }

    printLoL ("filled with somefunc via temps:", \@LoL);

    for i in range(10):
        tmp = somefunc(i)
        LoL[i] = tmp

    printLoL('filled with somefunc via temps:', LoL)

    @LoL = map [ somefunc $_ ], 0..9;
    printLoL 'filled with map', \@LoL;

    LoL = map(lambda x: somefunc(x), range(10))
    printLoL('filled with map', LoL)

Both Perl and Python allow you to map an operation over a list, or to loop through the list and apply the operation yourself.

I don\'t believe it is advisable to choose one of these techniques to the exclusion of the other \-\-- there are times when looping is more understandable, and times when mapping is. If conceptually the idea you want to express is \"do this to each element of the list\", I would recommend mapping because it expresses this precisely. If you want more precise control of the flow during this process, particularly for debugging, use loops.

Tom Christiansen suggests that it is often better to make it clear that a function is being defined, by writing:

    @LoL = map {[ somefunc($_) ]} 0..9;

rather than

    @LoL = map [ somefunc($_) ], 0..9;

or

    @LoL = map ([ somefunc($_)], 0..9);

### Adding to an existing row in a list of lists 

    @LoL = @LoLsave;  # start afresh
    push @{$LoL[0]}, "wilma", "betty";
    printLoL ('after appending to first element:', \@LoL);

    LoL = LoLsave[:]  # start afresh
    LoL[0] += ["wilma", "betty"]
    printLoL('after appending to first element:', LoL)

In python, the `+`{.backtick} operator is defined to mean concatenation for sequences. The `+`{.backtick} operator returns a new list object. Alternative to the above code that modify the original list object is to append each element of the list to `LoL[0]`{.backtick}:

    LoL[0].append("wilma")
    LoL[0].append("betty")

Or to extend:

    LoL[0].extend(["wilma", "betty"])

### Accessing elements of a list of lists 

#### One element 

    $LoL[0][0] = "Fred";
    print ("first element is now $LoL[0][0]\n");
    printSep();

    LoL[0][0] = "Fred"
    print('first element is now', LoL[0][0])
    printSep()

#### Another element 

    # upcase the first letter of each word
    # s/(\w)/\u$1/ is almost equivalent to Python .capitalize() [.capitalize() also lowercases the remaining letters]

    $LoL[1][1] =~ s{\b(\w)}{\u$1}g;
    print ("element 1, 1 is now $LoL[1][1]\n");
    printSep();

    LoL[1][1] = LoL[1][1].title()
    print('element 1, 1 is now', LoL[1][1])
    printSep()

Perl\'s regexp matching and substitution is enormously powerful; see especially the new syntax for comments and whitespace inside regular expressions. Python replaced its original regular expression module some years ago with one that closely matches the capabilities of Perls, including being able to do advanced RE tasks such as calling a function to provide the data for an RE substitution, and the optional inclusion of whitespace and comments in REs.

In Python, string methods are often used where Perl would use a regex. Among these string methods are `title()`{.backtick} and `capitalize()`{.backtick}.

In the context of names, `title()`{.backtick} will be used as it correctly changes \"smith-jones\" to \"Smith-Jones\" whereas `capitalize()`{.backtick} would produce \"Smith-jones\".

`str2 = str1.capitalize()`{.backtick} in Python is equivalent to `$str2 = ucfirst(lc($str1))`{.backtick} in Perl.

Python\'s `str2 = str1.title()`{.backtick} is equivalent to Perl\'s:

    $str2 = $str1;
    $str2 =~ s{\b(\w)(\w*)\b}{\u$1\L$2\E}g;

This is because regular expression search and replace operations modify the string in place (Perl strings are mutable).

### Printing a list of lists 

#### Print a list of lists using references 

    foreach my $aref ( @LoL ) {
        print "\t [ @$aref ],\n";
    }
    printSep();

    for a in LoL:
        print(f"\t [ {a} ],")
    printSep()

#### Print a list of lists using indices 

    foreach my $i ( 0 .. $#LoL ) {
        print "\t [ @{$LoL[$i]} ],\n";
    }
    printSep();

    for i in range(len(LoL)):
      print("\t [ {Lol[i]} ],"
    printSep()

The highest valid index of an array `A`{.backtick}:

- Perl: `$#A`{.backtick}.

- Python: `len(A) - 1`{.backtick}.

But note: The highest valid upper bound to a python range is len(A) as in

    A[0:len(A)]

Size of an array `A`{.backtick}:

- Perl: `scalar(@A)`{.backtick}

- Python: `len(A)`{.backtick}

Note: Perl does not really have a length operator like Python. `scalar()`{.backtick} simply provides a scalar context, and in a scalar context an array returns its size. (Perl is context-sensitive and things behave differently based on their context.)

Generate range of numbers:

- Perl: `(0..9)`{.backtick}

- Python: `range(0, 10)`{.backtick} or simply `range(10)`{.backtick} (assumes 0 as initial)

Note: Perl uses a closed interval, while Python uses a closed-open interval. You will notice that this pattern is quite consistently applied in both languages.

\[Link to details of the range function\]

#### Print a list of lists element by element 

    foreach my $i ( 0 .. $#LoL ) {
        foreach my $j ( 0 .. $#{$LoL[$i]} ) {
            print "elt $i $j is $LoL[$i][$j]\n";
        }
    }
    printSep();

    for i, mylist in enumerate(LoL):
        for j, elem in enumerate(mylist):
            print(f'elt {i} {j} is {elem}')
    printSep()

#### Print a list of lists using map 

    sub printLine { print "@{shift()}\n" }
    map printLine($_), @LoL;
    printSep();

    # This is legal but Do Not Do This
    def printLine(l):
        print(" ".join(l))
    map(printLine, LoL)
    printSep()

#### Print a list of lists using map and anonymous functions 

    print map "@$_\n", @LoL;
    printSep();

    # This is legal but Do Not Do This
    map(lambda x: sys.stdout.write(" ".join(x)), LoL)
    printSep()

The lack of true lambda expressions in Python is not really a problem, since all it means is that you have to provide a name for the function. Since you can define a function within another function, this does not lead to namespace clutter.

In Perl, a function can be defined inside another function, but it is defined in the namespace of the current package. If you need Python-like scoping of functions, you can create an anonymous subroutine and assign it to a lexically scoped variable:

    # A Python function with its own private function
    def lolprint(LoL):
       # Private function
       def lprint(alist):
          print(" ".join(str(alist)))
       map(lprint, LoL)

    # Achieving the same in Perl
    sub lolprint {
       # Private function
       # (function reference stored in a lexically scoped variable)
       my $lprint = sub {
          my $list = shift;
          print "@$list";
       };
       map $lprint->($_), @_;
    }

    # In Perl, if you did this, the function is no longer private.
    sub lolprint {
       # This is not a private function
       sub lprint {
          my $list = shift;
          print "@$list";
       };

       map lprint($_), @_;
    }

## Hashes/dictionaries of lists 

The Perl code in this section is taken, with permission, almost directly from Tom Christiansen\'s [Perl Data Structures Cookbook](http://www.perl.com/perl/pdsc/), part 2, release 0.1, with a few typos fixed.

Associative arrays are containers that hold pairs of elements. The first element of a pair is the *key*, the second is the *value*. In Python, the key may be of any type which is *hashable* (mutable data structures, like lists, sets, dictionaries, are no hashable). In Perl, the keys of a hash are converted into strings, which means if you try to use a reference as a key, it will get converted to some string representation, and you will not be able to use it as a reference anymore.

Associative arrays are sometimes called maps, dictionaries (Python, Smalltalk), or hashes (Perl).

### Preliminaries 

    sub printSep { print "=" x 60, "\n" }

    sub printHoL {
      my ($s, $hol) = @_;
      print "$s\n";
      foreach my $k (sort keys (%$hol))
      {
        my ($v) = $hol->{$k};
        print "$k: @$v\n";
      }
      printSep();
    }

    sub get_family {
      my ($group) = @_;
      $group =~ s/s$//;
      $group = "\u$group";
      return ("Mr-$group", "Mrs-$group", "$group-Jr");
    }

    def printSep():
        print('=' * 60)

    def printHoL(s, hol):
        print(s)
        for key, value in sorted(hol.items()):
            print key, ':', " ".join(value)
        printSep()

    def get_family(group):
      group = group.title()
      return ["Mr-" + group, "Mrs-" + group, group + "-Jr"]

`printHoL`{.backtick} pretty-prints a hash/dictionary of lists.

`printSep`{.backtick} prints a line of equal signs as a separator.

`get_family`{.backtick} makes a list of names from a \"group name\", e.g., `flintstones`{.backtick} becomes `[ "Mr-Flintstone", "Mrs-Flintstone", "Flintstone-Jr" ]`{.backtick} This is for generating lists to fill a hash/dictionary.

hol.items()\` converts a dictionary to a list of (key, value) pairs, eg: `[('flintstones', ['fred', 'barney']), ('jetsons', ['george', 'jane', 'elroy']), ('simpsons', ['homer', 'marge', 'bart'])]`{.backtick} This list is then sorted (sorting is in-place in python) and then the pairs in the list are unpacked and used.

If you didn\'t care for the results to be sorted (which is often true), you would simply do this:

    sub printHoL {
      my ($s, $hol) = @_;
      print "$s\n";
      while (my ($k, $v) = each (%$hol))
      {
        print "$k: @$v\n");
      }
      printSep();
    }

    def printHoL(s, hol):
        print(s)
        for key, value in hol.items():
            print(key, ':', " ".join(value))
        printSep()

### Declaration of a hash of lists 

    %HoL = (
           flintstones        => [ "fred", "barney" ],
           jetsons            => [ "george", "jane", "elroy" ],
           simpsons           => [ "homer", "marge", "bart" ],
         );

    printHoL 'names', \%HoL;

    HoL = { 'flintstones' : ['fred', 'barney'],
            'jetsons' : ['george', 'jane', 'elroy'],
            'simpsons': ['homer', 'marge', 'bart'], }

    printHoL('names', HoL)

In python, the print statement has very good default semantics \-\-- most of the time, it does exactly what you want, putting a space between the arguments, and a newline at the end. If you want more control over the formatting, use the `%`{.backtick} operator \[link to % operator\]: rather than

    print(k, ':', " ".join(v))

you could use

    print("%s: %s" % (k, " ".join(v)))

to avoid the space before the colon.

Note that both Perl and python let you have a comma after the last element of a list. This is especially useful for automatically generated lists, where you don\'t want to have to worry about a special case at the end.

Larry Wall says:

- The Perl code can be written in a more Pythonesque way, and means pretty much the identical thing. Perl always uses scalar variables for references. Note the brackets rather than the parens to get an anonymous hash constructor.

<!-- -->

    $HoL = {
           flintstones => [ "fred", "barney" ],
           jetsons     => [ "george", "jane", "elroy" ],
           simpsons    => [ "homer", "marge", "bart" ],

    };
    printHoL (\'names\', $HoL);

Note that since `$HoL`{.backtick} is already a ref, the `\\`{.backtick} is no longer necessary.

### Initializing hashes of lists 

#### Initializing hashes of lists from a file 

The file is assumed to consist of a sequence of lines of the form:

    flintstones: fred barney wilma dino

    my %HoL;
    open my $f, "cookTest.2" or die $!;
    while ( <$f> ) {
        next unless s/^(.*?):\s*//;
        $HoL{$1} = [ split ];
    }
    printHoL 'read from file cookTest.2', \%HoL;

    HoL = {}
    for line in open('cookTest.2'):
        try:
            surname, people = line.split(":", 1)
        except ValueError:             # can't split on ":" so no ":" in the line
            continue
        HoL[surname] = people.split()

    printHoL('read from file cookTest.2', HoL)

Note that the Perl hash doesn\'t need to be initialized.

#### Reading into a hash of lists from a file with temporaries 

    # flintstones: fred barney wilma dino
    open my $f, "cookTest.3" or die $!;
    my %HoL;
    while ( defined(my $line = <$f>) ) {
        next unless $line =~ /:/;
        ($who, $rest) = split /:\s*/, $line, 2;
        @fields = split ' ', $rest;
        $HoL{$who} = [ @fields ];
    }

    printHoL 'read from cookTest.3', \%HoL;

    HoL = {}
    for line in open('cookTest.3'):
        try:
            n = line.index(":")
        except ValueError:         # ":" not found
            continue
        who, rest = line[:n], line[n+1:]  # n+1 skips the colon
        fields = rest.split()
        HoL[who] = fields

    printHoL ('read from cookTest.3', HoL)

#### Initializing a hash of lists from function calls 

For each key of the hash, we call a function that creates a list, and associate the key with this list.

    my %HoL;
    foreach my $group (qw/simpsons jetsons flintstones/) {
        $HoL{$group} = [get_family $group];
    }

    printHoL 'filled by get_family', \%HoL;

    HoL = {}
    for group in ("simpsons", "jetsons", "flintstones"):
        HoL[group] = get_family(group)

    printHoL ('filled by get_family', HoL)

The python section could \[but should NOT\] have been written:

    HoL={}
    def set(group, hol=HoL):
        hol[group] = get_family(group)
    map(set, ("simpsons", "jetsons", "flintstones" ))

    printHoL ('filled by get_family', HoL)

The Perl section could have been written:

    my %Hol;
    map {$HoL{$_} = [ get_family $_ ]} qw/simpsons jetsons flintstones/;

The Perl section could also have been written like this (each of the control statements, `if`{.backtick}, `unless`{.backtick}, `while`{.backtick}, `until`{.backtick}, `foreach`{.backtick}, etc., can be written as a \"modifier\" at the end of a statement):

    my %HoL;
    $HoL{$_} = [get_family $_] foreach (qw/simpsons jetsons flintstones/);

#### Initializing a hash of lists from function calls with temporaries 

For each key of the hash, we call a function that creates a list, and associate the key with this list. The list is assigned to a local variable (where it could be modified, for example).

    my %HoL;
    foreach my $group (qw/simpsons jetsons flintstones/) {
        my @members = get_family $group;
        $HoL{$group} = [@members];
    }

    printHoL 'by get_family with temps', \%HoL;

    HoL = {}
    for group in ("simpsons", "jetsons", "flintstones"):
        members = get_family(group)
        HoL[group] = members

    printHoL ('by get_family with temps', HoL)

### Append to a list in a hash of lists 

We want to add two strings to the list of strings indexed by the name `flintstones`{.backtick}.

    push @{ $HoL{flintstones} }, "wilma", "betty";
    print "@{$HoL{flintstones}}\n");
    printSep();

    HoL['flintstones'].extend(['wilma', 'betty'])
    print(" ".join(HoL['flintstones']))
    printSep()

Note: There is a big difference between the above two examples, which create a new list, leaving the original list object unchanged; and the following two examples, which modify the original list.

    HoL['flintstones'] += ['wilma', 'betty']
    print(" ".join(HoL['flintstones']))
    printSep()

    $HoL{'flintstones'} = [ @{ $HoL{'flintstones'} }, "wilma", "betty" ];
    print "@{$HoL{flintstones}}\n");
    printSep();

### Access elements of a hash of lists 

#### Access a single element 

Assign to the first element of the list indexed by `flintstones`{.backtick}.

    $HoL{flintstones}[0] = "Fred";
    print $HoL{flintstones}[0], "\n";
    printSep();

    HoL['flintstones'][0] = "Fred"
    print(HoL['flintstones'][0])
    printSep()

Tom Christiansen explains when you don\'t need quotes around strings in Perl:

- It\'s whenever you have a bareword (identifier token) in braces. Thus

  `${blah} and $something{blah}`{.backtick} don\'t need quotes.

If blah were a function then you would have to use `$something{blah()}`{.backtick} to overwrite the stringificiation. Barewords are autoquoted in braces and as the LHS operand of `=&rt;`{.backtick} as well.

#### Change a single element 

This upcases the first letter in the second element of the array indexed by `simpsons`{.backtick}.

\# another element

    $HoL{simpsons}[1] =~ s/(\w)/\u$1/;

    printHoL 'after modifying an element', \%HoL;

    HoL['simpsons'][1] = HoL['simpsons'][1].title()

    printHoL ('after modifying an element', HoL)

### Print a hash of lists 

Various different ways of printing it out.

#### Simple print 

Printed sorted by family name, in the format:

    family1: member1-1 member1-2...
    family2: member2-1 member2-2...
    ...

    foreach my $family ( sort keys %HoL ) {
        print "$family: @{ $HoL{$family} }\n";
    }
    printSep();

    families = sorted(HoL.items())
    for surname, members in families:
        print('%s: %s' % (surname, " ".join(members)))
    printSep()

#### Print with indices 

    for my $family ( sort keys %HoL ) {
        print "family: ";
        for my $i ( 0 .. $#{ $HoL{$family}} ) {
            print " $i = $HoL{$family}[$i]";
        }
        print "\n";
    }
    printSep();

    for surname in sorted(HoL.keys()):
        print('surname: ', end="")
        for i, member in enumerate(HoL[surname]):
            print('%d = %s' % (i, member), end="")
        print
    printSep()

#### Print sorted by number of members 

    push (@{$HoL{simpsons}}, 'Lisa');
    for my $family ( sort { @{$HoL{$b}} <=> @{$HoL{$a}} } keys %HoL ) {
        print "$family: @{ $HoL{$family} }\n";
    }

    HoL['simpsons'] += ['Lisa']

    def keyNumberMembers(x):
      return len(x[1])

    families = HoL.items()
    families.sort(key=keyNumberMembers)
    for surname, members in families:
        print("%s:" % surname, " ".join(members))

You can use a lambda expression in python here, too, though I don\'t find it very readable:

    HoL['simpsons'] += ['Lisa']
    families = HoL.items()
    families.sort(key=lambda x: len(x[1]))
    for surname, members in k:
        print("%s:" % surname, " ".join(members)))

#### Print sorted by number of members, and by name within each list 

    foreach my $family ( sort { @{$HoL{$b}} <=> @{$HoL{$a}} } keys %HoL ) {
        print "$family: @{[ sort @{ $HoL{$family}} ]}\n";
    }

    families = HoL.items()
    families.sort(key=lambda x: len(x[1]))
    for surname, members in families:
        members.sort()
        print("%s: %s" % (family, ", ".join(members)))

Do it more like the Perl version:

    for surname, members in sorted(HoL.items(), key=lambda x: len(x[1])):
       print("%s: %s" % (family, ", ".join(sorted(members))))

## Lists of hashes/dictionaries 

The Perl code in this section is taken, with permission, almost directly from Tom Christiansen\'s [Perl Data Structures Cookbook](http://www.perl.com/perl/pdsc/), part 3, release 0.1, with a few typos fixed.

### Lists of hashes: preliminaries 

    sub printSep { print "=" x 60, "\n"; }

    sub printLoH
    {
      my ($s, $loh) = @_;
      print "$s\n";
      foreach my $h (@$loh)
      {
        print "[\n";
        foreach my $k (sort keys %$h)
        {
          print "  $k => $h->{$k}\n";
        }
        print "]\n";
      }
      printSep();
    }

    import sys

    def printSep():
        print('=' * 60)

    def printLoH(s,loh):
        print(s)
        for h in loh:
            print("[")
            items = h.items()
            items.sort()
            for key, val in items:
                print('  %s => %s' % (key, val))
            print("]")
        printSep()

The only reason I sort the keys here is to make sure that python and Perl print the elements of the dictionary in the same order.

Note that sorting in Perl generates a new list, while in python sorting is done in-place. This means that you can avoid making a copy while sorting in python. The disadvantage is a clumsier syntax for the common case where you *do* want a copy. Larry Wall says that in Perl, you almost always do want the copy; I am not sure whether this is true in Python.

If you wanted to do the copy, you would just do this (in Python 2.4+):

    import sys

    def printSep():
        print('=' * 60)

    def printLoH(s,loh):
        print(s)
        for h in loh:
            print("[")
            for key, val in sorted(h.items()):
                print('  %s => %s' % (key, val))
            print("]")
        printSep()

### Declaration of a list of hashes 

    @LoH = (
           {
              Lead      => "fred",
              Friend    => "barney",
           },
           {
               Lead     => "george",
               Wife     => "jane",
               Son      => "elroy",
           },
           {
               Lead     => "homer",
               Wife     => "marge",
               Son      => "bart",
           }
     );

    printLoH ('initial value', \@LoH);

    LoH = [
           {  "Lead"      : "fred",
              "Friend"    : "barney"
           },
           {
               "Lead"     : "george",
               "Wife"     : "jane",
               "Son"      : "elroy"
           },
           {
               "Lead"     : "homer",
               "Wife"     : "marge",
               "Son"      : "bart"
           }
          ]

    printLoH ('initial value', LoH)

### Generation of a list of hashes 

#### Reading a list of hashes from a file 

The format of the file is expected to be:

    LEAD=fred FRIEND=barney
    LEAD=homer WIFE=marge
    ...

    my @LoH;
    open my $f, "cooktest.4" or die $!;
    while ( <$f> ) {
        my $rec = {};
        for my $field ( split ) {
            ($key, $value) = split /=/, $field;
            $rec->{$key} = $value;
        }
        push @LoH, $rec;
    }

    printLoH 'after reading from file cooktest.4', LoH;

    LoH = []
    for line in open("cooktest.4")
        rec = {}
        for field in line.split():
            key, value = field.split('=', 1)
            rec[key] = value
        LoH.append (rec)

    printLoH ('after reading from file cooktest.4', LoH)

#### Reading a list of hashes from a file without temporaries 

    my @LoH;
    open my $f, "cooktest.4" or die $!;
    while ( <$f> ) {
        push @LoH, { split /[\s=]+/ };
    }

    printLoH ('direct read from file', \@LoH);

    # This builds a list of (key, value) pairs, and then creates the
    # dictionary from those.  A temporary pairs is used for readability
    LoH = []
    for line in open("cooktest.4")
        pairs = [field.split("=", 1) for field in line.split()]
        LoH.append(dict(pairs))

    printLoH ('direct read from file', LoH)

If you really want no temporaries at all, you could (but shouldn\'t) use the one line list comprehension (line breaks for legibility):

    LoH = [dict([field.split("=", 1)
                 for field in line.split()])
                     for line in open("cooktest.4")]

    printLoH ('direct read from file', LoH)

#### Generation of a list of hashes from function calls 

##### Preliminaries 

For convenience, these functions and variables are global. getnextpairset returns the elements of the array \_getnextpairsetdata. I don\'t know why Tom chose to make this return a list in Perl, rather than a reference to a hash. Perhaps to keep the order. You can still initialize a hash with the result. In python, returning a dictionary is definitely the way to go.

    $_getnextpairsetcounter = 0;
    @_getnextpairsetdata =
      ( ["lead", "fred", "daughter", "pebbles"],
        ["lead", "kirk", "first_officer", "spock", "doc", "mccoy"]);

    sub getnextpairset{
      if ($_getnextpairsetcounter > $#_getnextpairsetdata) { return (); }
      return @{$_getnextpairsetdata[$_getnextpairsetcounter++]};
    }

    sub parsepairs{
    my $line = shift;
    chomp $line;
    return split (/[= ]/, $line);
    }

    _getnextpairsetcounter = 0
    _getnextpairsetdata =\
      [ {"lead" : "fred", "daughter" : "pebbles"},
        {"lead" : "kirk", "first_officer" : "spock", "doc" : "mccoy"} ]

    def getnextpairset():
      global _getnextpairsetcounter
      if _getnextpairsetcounter == len(_getnextpairsetdata) : return ''
      result = _getnextpairsetdata[_getnextpairsetcounter]
      _getnextpairsetcounter += 1
      return result

    def parsepairs(line):
      line = line[:-1]   # chop last character off
      dict = {}
      pairs = regsub.split (line, "[= ]")
      for i in range(0, len(pairs), 2):
        dict[pairs[i]] = pairs[i+1]
      return dict

This would be much more elegant as a class, both in python and Perl. \[add a pointer to classes when we get there\]

##### Generation 

Call a function returning a list (in Perl) or a dictionary (in python). In Perl, the list is of the form `("lead","fred","daughter","pebbles")`{.backtick}; in python, the dictionary is of the form `{"lead" : "fred", "daughter" : "pebbles"}`{.backtick}.

    # calling a function  that returns a key,value list, like

    my @LoH;
    while ( my %fields = getnextpairset() ) {
       push @LoH, { %fields };
    }
    printLoH ('filled with getnextpairset', \@LoH);

    LoH = []
    while True:
      fields = getnextpairset()
      if not fields: break
      LoH.append (fields)

    printLoH ('filled with getnextpairset', LoH)

##### Generation without temporaries 

    my @LoH;
    open my $f, "cooktest.4" or die $!;
    while (<$f>) {
        push @LoH, { parsepairs($_) };
    }

    printLoH 'generated from function calls with no temps', \@LoH;

    LoH = [parsepairs(line) for line in open("cooktest.4")]

    printLoH ('generated from function calls with no temps', LoH)

### Adding a key/value pair to an element 

    $LoH[0]{PET} = "dino";
    $LoH[2]{PET} = "santa's little helper";

    printLoH ('after addition of key/value pairs', \@LoH);

    LoH[0]["PET"] = "dino"
    LoH[2]["PET"] = "santa's little helper"

    printLoH ('after addition of key/value pairs', LoH)

### Accessing elements of a list of hashes 

    $LoH[0]{LEAD} = "fred";
    print $LoH[0]{LEAD}, "\n";

    s/(\w)/\u$1/, print "$_\n"
      for $LoH[1]{LEAD};

    printSep();

    LoH[0]["LEAD"] = "fred"
    print((LoH[0]["LEAD"]))

    LoH[1]["LEAD"] = LoH[1]["LEAD"].title()
    print((LoH[1]["LEAD"]))

    printSep()

### Printing a list of hashes 

#### Simple print 

    for my $href ( @LoH ) {
        print "{ ";
        for my $role ( sort keys %$href ) {
            print "$role=$href->{$role} ";
        }
        print "}\n";
    }

    for href in LoH:
        print("{", end="")
        items = href.items();
        items.sort()
        for role, val in items:
            print("%s=%s" %(role, val), end="")
        print("}")

Note the end=\"\" in the python segment \-- this means \"don\'t add a newline\".

#### Print with indices 

    for my $i ( 0 .. $#LoH ) {
        print "$i is { ";
        for my $role ( sort keys %{ $LoH[$i] } ) {
            print "$role=$LoH[$i]{$role} ";
        }
        print "}\n";
    }

    for i, elem in enumerate(LoH):
        print(i, "is {", end="")
        items = elem.items();
        items.sort()
        for role, val in items:
            print("%s=%s" % (role, val), end="")
        print("}")

Note the end=\"\"in the python segment \-- this means \"don\'t add a newline\". It does, however, add a space.

#### Print whole thing one at a time 

    for my $i ( 0 .. $#LoH ) {
        for my $role ( sort keys %{ $LoH[$i] } ) {
            print "elt $i $role is $LoH[$i]{$role}\n";
        }
    }

    for i, elem in enumerate(LoH):
        items = elem.items();
        items.sort()
        for role, val in items:
            print(f"elt {i} {role) is {val}")

# Interface to the Tk GUI toolkit 

The Perl versions of this code have not been tested, as we don\'t currently have a working version of Perl and Tk.

\[Links to tkinter doc\]

[Perl/Tk Documentation](http://search.cpan.org/~srezic/Tk/)

## Preliminaries 

All the following code snippets will need these declarations first:

    use Tk;

    from Tkinter import *
    import sys

## Hello world label 

    $top = MainWindow->new;
    $hello = $top->Button(
        '-text'    => 'Hello, world',
        '-command' => sub {print STDOUT "Hello, world\n";exit 0;}
    );
    $hello->pack;
    MainLoop;

    top = Tk()
    def buttonFunction () :
        print('Hello, world')
        sys.exit (-1)

    hello = Button(top, {'text' : 'Hello, world', 'command' : buttonFunction})
    hello.pack()
    top.mainloop()

------------------------------------------------------------------------

[CategoryAdvocacy](CategoryAdvocacy)
