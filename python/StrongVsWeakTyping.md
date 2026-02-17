# StrongVsWeakTyping

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The following text is a summary by clips from posts in a thread on comp.lang.python, which was initiated by the following post:

- From: Gabriel Zachmann \<[zach@cs.uni-bonn.de](mailto:zach@cs.uni-bonn.de)\>\
  Newsgroups: comp.lang.python\
  Subject: strong/weak typing and pointers\
  Date: 28 Oct 2004 16:17:15 GMT Is it correct to say that strong/weak typing does not make a difference if one does not use any pointers (or adress-taking operator)? More concretely, I am thinking particularly of Python vs C++. So, are there any examples (without pointers, references, or adress-taking), which would have a different result in Python and in C++?

# Definitions 

GZ:

There seem to be two major lines along which strong/weak typing is defined:

1.  The more type coercions (implicit conversions) for built-in operators the language offers, the weaker the typing. (This could also be viewed as more built-in overloading of built-in operators.)
2.  The easier it is in a language, or the more ways a language offers, to reinterpret a memory block (associated with a data value) as a different type, the weaker the typing.

In the following, I\'ve cut-and-pasted several clips from the many responses (thanks to you all!), organized by the above two categories.

------------------------------------------------------------------------

From: Steven Bethard \<[steven.bethard@gmail.com](mailto:steven.bethard@gmail.com)\>

- I A language is \"weakly-typed\" if it allows code to take a block of memory that was originally defined as one type and reinterpret the bits of this block as another type. II A language is \"weakly-typed\" if it has a large number of implicit coercions. III A language is \"weakly-typed\" if it often treats objects of one type as other types.

Some points and problems addressed with each of these definitions:

Definition 1 is the definition most commonly used in Programming Languages literature, and allows a language to be called \"weakly-typed\" based only on the language definition. However, for all intents and purposes, it is only applicable to statically typed languages; no one on the list could come up with a dyamically typed language that allowed bit-reinterpretation.

Definition 2 seemed to be the definition most commonly used on the list, most likely because it is actually applicable to a dynamically typed language like Python. It has the problem that in a language that supports operator overloading (like Python), programmers can make their language more \"weakly-typed\" by simply providing additional coercions, thus whether or not a language is called \"weakly-typed\" depends both on the language definition and any code written in the language.

Definition 3 was an attempt to unify the first two definitions into a single definition by describing both coercion and bit-reinterpretation as treating \"objects of one type as other types\". This definition has the advantage of better coverage, but has all the disadvantages of Definition 2. It is also unclear as to how weak a \"weakly-typed\" language is if it both allows bit-reinterpretation and has a large number of implicit coercions. (For example, is a language that allows bit-reinterpretation and only a few implicit coercions more or less \"weakly-typed\" than a language that doesn\'t allow bit-reinterpretation, but has a large number of implicit coercions?)

# Definition based on number of type coercions 

From: Andrea Griffini \<[agriff@tin.it](mailto:agriff@tin.it)\>

You didn\'t mention C++. Try this \...

       std::string s = "Wow";
       s += 3.141592654; // Perfectly valid
       s = 3.141592654;  // Also valid

------------------------------------------------------------------------

From: Grant Edwards \<[grante@visi.com](mailto:grante@visi.com)\>

- *a = \"1\" + 2\
  as \"1\" is a string and 2 an integer.*

\"1\" is a pointer to a char.

- *And even though C is statically typed, it won\'t complain*

That\'s because \<pointer\> + \<integer\> has a well-defined meaning in C \-- just like \<float\> + \<integer\> does in Python (and in C).

- *- you just end up with an unexpected result.*

Only people who don\'t know how C pointer arithmatic works will get unexpected results.

------------------------------------------------------------------------

From: [mwilson@the-wire.com](mailto:mwilson@the-wire.com) (Mel Wilson)

One effect of weak typing is to put more reliance on operators. In Perl, for instance the string operator `lt`{.backtick} does a string compare to find that \"10\" is less than 2 (lexically) and the numeric operator `<`{.backtick} finds that \"10\" is not less than 2 (numerically). Nothing to do with pointers at all.

# Definition based on reinterpretation 

From: Jorgen Grahn \<[jgrahn-nntq@algonet.se](mailto:jgrahn-nntq@algonet.se)\>

Note though, that in the absense of casts, C and in particular C++ are pretty strongly typed for pointers.

------------------------------------------------------------------------

From: Steven Bethard \<[steven.bethard@gmail.com](mailto:steven.bethard@gmail.com)\>

- *Strong/weak typing is about how much you care of types at all - in php, its perfectly legal to add strings to numbers - the string simply gets converted to a number beforehand, that conversion yielding 0 when there is nothing useful and numberlike can be extracted from the string. So typing is weak, as it doesn\'t constrain the possible operations on variables with certain values.*

By this definition, Python is also weakly typed:

    >>> 2.0 + 1
    3.0

Your defintion above calls PHP weakly typed because it performs implicit string-\>number conversions. The Python code above performs an implicit int-\>float conversion.

This is not the definition of strongly- and weakly-typed that I\'m used to. When I use strongly-typed, I mean that a block of memory associated with an object cannot be reinterpreted as a different type of object. For example, in a weakly-typed language like C, we can do:

    struct A {
            char c;
            int i;
    };
    struct B {
            float f;
            char c;
    };
    int main(int argc, char* argv) {
            struct A a = {'c', 1024};
            struct B* b = (struct B*)&a;
            printf("'%c' %d %f '%c'\n", a.c, a.i, b->f, b->c);
    }

The point here is that I consider C weakly typed because, with no error of any sort, it allows me to reinterpret a block of memory in as many ways as I like. A strongly typed language like Python does not allow this. Even in my Python example above, we\'re not \*reinterpreting\* the block of memory representing 1 as a floating point value; we\'re \*coerceing\* the integer 1 into the floating point value 1.0 (which probably means allocating a new float variable at the C level) before performing the addition.

------------------------------------------------------------------------

From: JCM \<[joshway_without_spam@myway.com](mailto:joshway_without_spam@myway.com)\>

You\'ll find a lack of consensus here on what\'s meant by \"strong/weak typing\". In Python there\'s no way to re-interpret the bits of a value as if they were a different type. For example, code like this is impossible in Python:

      float x = 2.5;
      printf("%d\n", *(int*)&x);

------------------------------------------------------------------------

From: Duncan Booth \<[duncan.booth@invalid.invalid](mailto:duncan.booth@invalid.invalid)\>

Here\'s a trivial example that is almost identical in Python and C/C++ but gives totally different results. In a weakly typed language such as C or C++:

    #include <stdio.h>

    int main(int argc, char**argv)
    {
        float f = 3;
        printf("value is %d", f);
    }

I get the output (you may get different results):

    value is 0

In a fairly strongly typed language such as Python:

    >>> f = 3.0
    >>> print "value is %d" % f
    value is 3

In a really strongly typed language I would expect an exception to be thrown.

------------------------------------------------------------------------

From: Scott David Daniels \<[Scott.Daniels@Acm.Org](mailto:Scott.Daniels@Acm.Org)\>

Strong types provide strong protection for data types as their abstraction; weak types allow you to operate on data \"behind the wall of abstraction\". A Smalltalk programmer would say that Python is more weakly typed than Smalltalk for user-defined types.

------------------------------------------------------------------------

From: Steven Bethard \<[steven.bethard@gmail.com](mailto:steven.bethard@gmail.com)\>

- *If you do this:*

<!-- -->

     "a" + 10

- *you end with 10 - if the string doesn\'t contain something as number*

I would still call this coercion with an overloaded operator. A horrible language decision, certainly, but not a mark of weak typing \-- note that Python can give you exactly the same behavior if you want it:

    >>> class phpint(int):
    ...     def __add__(self, other):
    ...             try:
    ...                     other = int(other)
    ...             except ValueError:
    ...                     other = 0
    ...             return super(phpint, self).__add__(other)
    ...     __radd__ = __add__
    ...
    >>> i = phpint(10)
    >>> 5 + i
    15
    >>> "5" + i
    15
    >>> "a" + i
    10

This doesn\'t mean that Python has suddenly become a weakly-typed language. It just means that I\'ve implemented some poor coercion choices in the language.

Basically you would say that the more implicit coercions a language performs, the more weakly typed it is. This diverges from the common use of the terms strong and weak typing in the PL literature, which is why I was confused.

# Justification for weak typing 

From: Mike Meyer \<[mwm@mired.org](mailto:mwm@mired.org)\>

Now, as to why one would \*want\* languages that let you treat things as other than what they were.

It\'s much easier to write functions that convert 16, 32 and 64 bit quantities from network order to host order (and vice versa) if you can treat them as an array of bytes, even though you\'ll want to treat them as longer hunks while dealing with them. When talking to hardware, you can get some really \*strange\* things. You may have a location that is an address most of the time, but part of the time is a control register full of bits to toggle. When doing cryptography, you very often want to treat the string of characters you\'re encrypting as a string of words of some length, because that\'s the size chunk that the algorythm encrypts. Marshelling has already been mentioned on this thread. You may well want to marshal ints and floats in binary form, meaning you\'ll need to treat that array of bytes as being of that type.

Finally, I don\'t see that there\'s that much difference between the two different definitions of \'weakly typed\'. Both can be described as treating an object as if it were of some type other than what it really is. In one case, you abuse the raw bits, and in the other you coerce the object to a different type. Both amount to the same thing:

           a = "10"
           b = 5
           c = a + b

------------------------------------------------------------------------

From: [aleaxit@yahoo.com](mailto:aleaxit@yahoo.com) (Alex Martelli)

How would an operating system\'s filesystems store arbitrary sequences of bytes (which might be floats, int, whatever \-- only the application knows) into disk pages (blocks of, say , 4096 bytes each) otherwise? Or are you saying that operating systems\' kernels should all be implemented in dynamically-typed languages, or that the structureless filesystem concept that was the fortune of Unix (and is common today to other OSs, too), is not \"good\"?

------------------------------------------------------------------------

From: [mike@hobbshouse.org](mailto:mike@hobbshouse.org) (Michael Hobbs)

This example is a little weak, but may be sufficient. The in_addr structure used for sockets usually uses a union to provide different views to the underlying 32-bit address. You can access the address as 4 8-bit values, 2 16-bit values, or 1 32-bit value. Most code these days only use the 4 8-bit representation, but the interface is there.

------------------------------------------------------------------------

From: [aleaxit@yahoo.com](mailto:aleaxit@yahoo.com) (Alex Martelli)

Given a float, extract the (so-called) \"mantissa\" (what a misnomer!) and exponent. Can you see the usefulness of \_that\_? Can you see that treating the bits that compose the float as an int and using masking and shifting is the obvious way to perform this task?

Say I need to compute some unary float function, such as \'sin\', with high speed and precision. One reasonable approach: normalize the float input to a standard range (say 0 to pi/4, remembering what kind of sign inversions &c you need to perform at result time); get \"mantissa\" (pah!) and exponent and use the latter, partly to select the right lookup table and partly to shift the mantissa appropriately to make it an index into said result table, while keeping track of the bits that shifted out; read out the result base and the multiplier for interpolation, multiply the latter by the bits that shifted out and add the result to the result base; perform sign or other symmetry inversions as previously recorded.

# Comparisons 

From: Steven Bethard \<[steven.bethard@gmail.com](mailto:steven.bethard@gmail.com)\>

- *(1) Weakly-typed languages allow you to take a block of memory that was originally defined as one type and reinterpret the bits of this block as another type\[1\]. (This is the definition usually used in Programming Languages literature.)*

  \(2\) Weakly-typed languages have more implicit coercions than strongly-typed languages. (This seems to be the favored definition on this newsgroup.)

<!-- -->

- *Is either of them a subset of the other, generally speaking?*

Not really \-- they\'re pretty much orthogonal.

For example, C is weakly-typed (PL theory definition) but has only a few implicit coercions (e.g. int-\>float with the + operator). Of course, C only has a very few basic types so it doesn\'t have as many chances to support implicit coercions. For example, there is no string type in C (only arrays of characters), so it wouldn\'t really make sense to talk about some sort of string-\>int coercion.

Python is strongly-typed (PL theory definition) and also has only a few implicit coercions (e.g. int-\>float with the + operator).

ML is strongly-typed (PL theory definition) and has \*very\* few (perhaps none?) implicit coercions, e.g.:

      # 1 + 1.0;;

      Characters 4-7:
        1 + 1.0;;
            ^^^
      This expression has type float but is here used with type int

not even the int-\>float conversion common to C, Java, Python, etc. is supported.

\[\...\]

Examples in this thread suggest that both Perl and PHP have large numbers of implicit coercions.

- *From weakly-typed to strongly-typed (PL theory definition):*

C \< Java, Python, ML

Basically, there\'s no hierarchy, just weakly-typed and strongly-typed. You might get a hierarchy if you had some languages that allowed only some (but not all) objects to be reinterpreted.

- *From many implicit coercions to few implicit coercions:*

C, Java, Python \< ML
