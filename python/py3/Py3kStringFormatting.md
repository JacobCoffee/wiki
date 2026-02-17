# Py3kStringFormatting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# String formatting methods in Python 3000, based on PEP 3101

  --------- ------------------
  Author:   Andrea Bucciotti
  --------- ------------------

::: 
### Current formatting methods

Python 3.0 currently provides two methods of string interpolation:

> - The \'%\' operator for strings.
> - The string.Template module.

The first one has been removed because, as a binary operator, it can take at most 2 arguments of which one is already dedicated to the format string. This makes \'%\' operator quite unflexible and constraining.

On the other hand the string.Template module is felt that serves a distinct need and for that reason is not going to be removed or changed.
:::

::: 
### Get started: the new method, format!

The built-in string class (and also the Unicode class in 2.6) will gain a new method, \'format\', which takes an arbitrary number of positional and keyword arguments.

This method can also be \"customized\", but we\'ll treat about this later.

Each argument can be identified with a positional number starting from 0, or with a keyword name:

    "My name is {0}, and this is a {whatsthis} about string formatting in {2}".format('Andrea',whatsthis = 'tutorial','Python')

Which gives:

    "My name is Andrea, and this is a tutorial about string formatting in Python"

instead of the old:

    "My name is s%, and this is a s% about string formatting in s%" % ('Andrea','tutorial','Python')

Brace characters (\'curly braces\') are used to indicate a replacement field within the string:

    "Hello, {0}.".format('world')

Braces can be escaped by doubling:

    "Curly {0}: {{}}".format('braces')

The new string is:

    "Curly braces: {}"

The element within the braces is called a \'field\'. Fields consist of a \'field name\', which can either be simple or compound, and an optional \'format specifier\'.
:::

::: 
### Simple and Compound field names

A simple field name is a valid base-10 integer, or a valid Python identifier.

A compound field name is a combination of multiple simple field names in an expression. For example, a field whose field width is itself a parameter could be specified via:

    "{0:{1}}".format(a, b)

By design you cannot embed arbitrary expressions in format strings.

Only two operators are supported: the \'.\' (getattr) operator, and the \'\[\]\' (getitem) operator.

This example shows the use of the \'getattr\' or \'dot\' operator in a field expression.

The dot operator allows an attribute of an input value to be specified as the field value. ..

> \"My name is {0.name}\".format(open(\'out.txt\', \'w\'))

This code creates a new empty file \'out.txt\' in the current directory and returns the string:

    "My name is out.txt"

Where \'out.txt\' is the complete path to the file.

An example of the \'getitem\' syntax:

    "My name is {0[name]}".format(dict(name='Fred'))

It should be noted that the use of \'getitem\' within a format string is much more limited than its conventional usage.

In the above example, the string \'name\' really is the literal string \'name\', not a variable named \'name\'.

Because keys are not quote-delimited, it is not possible to specify arbitrary dictionary keys (e.g., the strings \"10\" or \":-\]\") from within a format string.
:::

::: 
### Format Specification

If an object does not define its own format specifiers, a standard set of format specifiers is used.

- The general form of a standard format specifier is:

      format_spec ::=  [[fill]align][sign][0][width][.precision][type]
      fill        ::=  <a character other than '}'>
      align       ::=  "<" | ">" | "=" | "^"
      sign        ::=  "+" | "-" | " "
      width       ::=  integer
      precision   ::=  integer
      type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "x" | "X" | "%"

  The fill character can be any character other than `}` (which signifies the end of the field).

  The presence of a fill character is signaled by the next character, which must be one of the alignment options.

  If the second character of format_spec is not a valid alignment option, then it is assumed that both the fill character and the alignment option are absent.

- Then the optional align flag can be one of the following:

  > 
  >
  > \'\<\'
  >
  > :   Forces the field to be left-aligned within the available space (this is the default.)
  >
  > \'\>\'
  >
  > :   Forces the field to be right-aligned within the available space.
  >
  > \'=\'
  >
  > :   Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form \'+000000120\'. This is only valid for numeric types.
  >
  > \'\^\'
  >
  > :   Forces the field to be centered within the available space.

  Note that unless a minimum field width is defined, the field width will always be the same size as the data to fill it, so that the alignment option has no meaning in this case.

  Some examples:

      # right alignment, plus 10 empty spaces
      >>> "Hello {0:>10}".format('Python')
      'Hello     Python'

      # fill with 20 '=', center the name 'Python' in those '='
      >>> "{0:=^20}".format('Python')
      '=======Python======='

      # '=' with another meaning
      >>> "A number with 10 '0': {0:0=10}".format(-66)
      'A number with 10 '0': -000000066'


      ### A script that prints the contents of 3 lists

      name = ['Christin','Heinrich', 'Giovanni']
      city = ['Cork', 'Jena', 'Roma']
      state = ['Irlanda', 'Germania', 'Italia']

      for x in range(3):
          print ("{0:<}{1:^12}{2:>}".format(name[x],city[x],state[x]))

      ### Output:

       Christin    Cork    Irlanda
       Heinrich    Jena    Germania
       Giovanni    Roma    Italia

- The \'sign\' option is only valid for numeric types, and can be one of the following:

  > 
  >
  > \'+\'
  >
  > :   indicates that a sign should be used for both positive as well as negative numbers
  >
  > \'-\'
  >
  > :   indicates that a sign should be used only for negative numbers (this is the default behavior)
  >
  > \' \'
  >
  > :   indicates that a leading space should be used on positive numbers

  Some examples:

      >>> "The function limit is {0:-}".format(6)
      "The function limit is 6"

      >>> "The function limit is {0:+}".format(6)
      "The function limit is +6"

      >>> "The function limit is {0: }".format(6) # one space between 'is' and '{'
      "The function limit is  6" # results in two spaces, because 6 is positive

      >>> "The function limit is {0: }".format(-6) # negative number
      "The function limit is -6" # no leading space

- \'width\' is a decimal integer defining the minimum field width. If not specified, then the field width will be determined by the content.

  If the width field is preceded by a zero (\'0\') character, this enables zero-padding. This is equivalent to an alignment type of \'=\' and a fill character of \'0\'.

- The \'precision\' is a decimal number indicating how many digits should be displayed after the decimal point in a floating point conversion.

- Finally, the type determines how the data should be presented.

  The available integer presentation types are:

  > ------------------------------------------------------------------------------------------------------
  >   Type    Meaning
  >   ------- ----------------------------------------------------------------------------------------------
  >   \'b\'   Binary. Outputs the number in base 2.
  >
  >   \'c\'   Character. Converts the integer to the corresponding Unicode character before printing.
  >
  >   \'d\'   Decimal Integer. Outputs the number in base 10.
  >
  >   \'o\'   Octal format. Outputs the number in base 8.
  >
  >   \'x\'   Hex format. Outputs the number in base 16, using lower- case letters for the digits above 9.
  >
  >   \'X\'   Hex format. Outputs the number in base 16, using upper- case letters for the digits above 9.
  >
  >   None    the same as \'d\'
  >   ------------------------------------------------------------------------------------------------------

  The available presentation types for floating point and decimal values are:

  > --------------------------------------------------------------------------------------------------------------------------------------------------
  >   Type    Meaning
  >   ------- ------------------------------------------------------------------------------------------------------------------------------------------
  >   \'e\'   Exponent notation. Prints the number in scientific notation using the letter \'e\' to indicate the exponent.
  >
  >   \'E\'   Exponent notation. Same as \'e\' except it uses an upper case \'E\' as the separator character.
  >
  >   \'f\'   Fixed point. Displays the number as a fixed-point number.
  >
  >   \'F\'   Fixed point. Same as \'f\'.
  >
  >   \'g\'   General format. This prints the number as a fixed-point number, unless the number is too large, in which case it switches to \'e\'.
  >
  >   \'G\'   General format. Same as \'g\' except switches to \'E\' if the number gets to large.
  >
  >   \'n\'   Number. This is the same as \'g\', except that it uses the current locale setting to insert the appropriate number separator characters.
  >
  >   \'%\'   Percentage. Multiplies the number by 100 and displays in fixed (\'f\') format, followed by a percent sign.
  >
  >   None    the same as \'g\'
  >   --------------------------------------------------------------------------------------------------------------------------------------------------

  Integer example:

  > ``` doctest-block
  >
  > >>> 'The decimal {0} in base 2 looks like {0:b}, its Unicode is {0:c}.'.format(666)
  > 'The decimal 666 in base 2 looks like 1010011010, its Unicode is \u029a.'
  > >>> 'You can also have the octal {0:o} and the hex {0:x} formats.'.format(666)
  > 'You can also have the octal 1232 and the hex 29a formats.'
  > ```

  Float example:

  > ``` doctest-block
  >
  > >>> 'An exp notation for {0} is {0:e}'.format(15000000.659741)
  > 'An exp notation for 15000000.6597 is 1.500000e+007'
  > ```
:::

::: 
### Explicit Conversion Flag

The explicit conversion flag is used to transform the format field value before it is formatted. Currently, two explicit conversion flags are recognized:

- `!r` - convert the value to a string using `repr()`.
- `!s` - convert the value to a string using `str()`.

These flags are placed before the format specifier:

    >>> "{0!r:20}".format("Hello")  # Double quotes
    >>> "'Hello'             "

    >>> "{0!s:20}".format("Hello")  # Single quote
    >>> 'Hello               '
:::

::: 
### Customize the format method

The new, global built-in function \'format\' simply calls this special method:

    def format(value, format_spec):
        return value.__format__(format_spec)

Any class can override the `__format__` method to provide custom formatting for that type:

    class AST:
        def __format__(self, format_spec):
            ...
:::

::: 
### A final Example

Now, how do we stitch all this stuff toghether?

I\'ll try to give you an example script that sum quite everything we saw:

    # the following script generates random numbers and, using compound
    # fields left aligns odd numbers and right aligns even numbers

    import random

    while True:
        a = random.randint(1, 10000000000)
        b = '<'
        if a % 2 == 0: # if it's even
            b = '>'

        print('{0: {1}20g}'.format(a,b))
:::
