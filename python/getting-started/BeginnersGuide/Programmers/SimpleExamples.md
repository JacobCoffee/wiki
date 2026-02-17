# BeginnersGuide/Programmers/SimpleExamples

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here are some samples to help get a better idea of Python\'s syntax:

Hello World (the traditional first program)

:::: 
::: 
``` 
print('Hello world!')
```
:::
::::

String formatting

:::: 
::: 
``` 
name = 'Monty'
print('Hello, %s' % name)  # string interpolation
print('Hello, {}'.format(name))  # string formatting
```
:::
::::

Defining a function

:::: 
::: 
``` 
def add_one(x):
    return x + 1
```
:::
::::

Testing variable equality

:::: 
::: 
``` 
x = 1
y = 2
print 'x is equal to y: %s' % (x == y)
z = 1
print 'x is equal to z: %s' % (x == z)
names = ['Donald', 'Jake', 'Phil']
words = ['Random', 'Words', 'Dogs']
if names == words:
    print 'Names list is equal to words'
else:
    print "Names list isn't equal to words"
new_names = ['Donald', 'Jake', 'Phil']
print 'New names list is equal to names: %s' % (new_names == names)
```
:::
::::

Defining a class with two methods

:::: 
::: 
``` 
class Talker(object):
    def greet(self, name):
        print 'Hello, %s!' % name
    def farewell(self, name):
        print 'Farewell, %s!' % name
```
:::
::::

Defining a list

:::: 
::: 
``` 
dynamic_languages = ['Python', 'Ruby', 'Groovy']
dynamic_languages.append('Lisp')
```
:::
::::

Defining a dictionary

:::: 
::: 
``` 
numbered_words = dict()
numbered_words[2] = 'world'
numbered_words[1] = 'Hello'
numbered_words[3] = '!'
```
:::
::::

Defining a while loop

:::: 
::: 
``` 
while True:
    if value == wanted_value:
        break
    else:
        pass
```
:::
::::

Defining multiline strings

:::: 
::: 
``` 
string = '''This is a string with embedded newlines.
Also known as a tripled-quoted string.
    Whitespace at the beginning of lines is included,
so the above line is indented but the others are not.
'''
```
:::
::::

Splitting a long string over several lines of source code

:::: 
::: 
``` 
string = ('This is a single long, long string'
          ' written over many lines for convenience'
          ' using implicit concatenation to join each'
          ' piece into a single string without extra'
          ' newlines (unless you add them yourself).')
```
:::
::::

Defining a for loop

:::: 
::: 
``` 
for x in xrange(1, 4):
    print ('Hello, new Python user!'
           'This is time number %d') % x
```
:::
::::

List comprehension

:::: 
::: 
``` 
l = [x**2 for x in range(4)]
print(l)
# [0, 1, 4, 9]
```
:::
::::

Set comprehension with condition

:::: 
::: 
``` 
squares = {x**2 for x in [0,2,4] if x < 4}
print(squares)
# {0, 4}
```
:::
::::

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
