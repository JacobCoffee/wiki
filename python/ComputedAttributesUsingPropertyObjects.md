# ComputedAttributesUsingPropertyObjects

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Computed Attributes, Using Property Objects 

John Posner

This document describes computed attributes and introduces the easiest way to implement computed attributes in Python: using **property** objects.

## Kinds of Attributes 

In Python, an object\'s contents are accessed as **attributes**, using dot-notation. Some attributes provide access to stored data: integers, strings, lists, user- or system-defined objects, etc:

    wgt.color
    employee.first_name
    team.positions

Other attributes provide access to functions (more correctly in this context: \"methods\"), which can be called with an argument list to execute code:

    wgtlist.darkest_color()
    employee.full_name(salutation=True, caps=False)
    team.best_hitter(baseball.SLUGGING)

Python also provides a mechanism for blurring the distinction between these standard ways of using attributes. A **computed attribute** (or \"managed attribute\") *looks like* it directly accesses storage, but *works like* a function. That is, you code a computed attribute without parentheses or arguments, but accessing the attribute causes a function to be executed. Example:

- If `color`{.backtick} is a computed attribute of object `wgt`{.backtick}, then in these statements \...

      save_me = wgt.color
      top_edge_color = (255,) + wgt.color[1:]

- \... evaluating `wgt.color`{.backtick} causes a function to be invoked. The function\'s return value is used in the right-hand-side expression.

The easiest way to implement a computed attribute is with an object of type **property**, introduced in Python 2.2. Depending on the way you access a property object, it dispatches a function to perform either a \"get the value\" operation or a \"set the value\" operation (or even \"delete the attribute\"). You specify the dispatch functions when you create the property object; it\'s up to you to ensure that the work they do makes sense. The following diagram illustrates how a property works.

[py-props.png](attachments/ComputedAttributesUsingPropertyObjects/py-props.png)

## Creating a Computed Attribute 

Here\'s a scenario that calls for a computed attribute that implements \"get the value\" and \"set the value\" operations \... To model your company\'s widgets, which come in a variety of colors, you use a class named `Widget`{.backtick}, with instance attribute `color`{.backtick}:

    class Widget(object):
        def __init__(self, arg=None):
            if arg:
                self.color = arg
            else:
                self.color = (0,0,0)

In the past, all Widget colors were specified as *(R,G,B)* tuples, so programs could make simple references to, and assignments to, the `color`{.backtick} attribute. But now, there\'s a business need to support colors specified as *#rrggbb* strings, also. Management decides that a Widget object must store the color in its originally specified format (string or tuple), but must always report the color as an *(R,G,B)* tuple. Moreover, existing programs using the `color`{.backtick} attribute must continue to work, without modification.

These requirements can be handled by turning `color`{.backtick} into a computed attribute:

- At the instance level, rename the attribute that stores the color value, from `self.color`{.backtick} to `self.color_data`{.backtick}. This frees up the attribute name `color`{.backtick}.

- At the class level, assign the attribute name `color`{.backtick} to a property object that can dispatch two functions, `get_color`{.backtick} and `set_color`{.backtick}.

The following code implements `get_color`{.backtick} and `set_color`{.backtick} as methods of the Widget class. Alternatively (but less object-orientedly), they could be implemented as functions outside the class definition.

    class Widget(object):
        def __init__(self, arg=None):
            if arg:
                self.color_data = arg
            else:
                self.color_data = (0,0,0)

        def get_color(self):
            if type(self.color_data) is tuple:
                return self.color_data
            else:
                return str_to_tuple(self.color_data)

        def set_color(self, arg):
            self.color_data = arg

        # create property object to dispatch 'get' and 'set' methods
        # NOTE: "color" is a class attribute, not an instance attribute
        color = property(get_color, set_color)

The `get_color`{.backtick} method uses a utility function, `str_to_tuple`{.backtick}:

    def str_to_tuple(color_string):
        return (int(color_string[1:3], 16),   # red
                int(color_string[3:5], 16),   # green
                int(color_string[5:], 16))    # blue

Now, when a program makes a reference to the attribute `color`{.backtick} through a Widget instance `wgt`{.backtick}, the property object dispatches `get_color`{.backtick}, which retrieves the `color_data`{.backtick} value and returns an *(R,G,B)* tuple. Similarly, when a program makes an assignment to the attribute `color`{.backtick}:

    wgt.color = "#ff80ff"

\.... the property object dispatches `set_color`{.backtick} with the argument `"#ff80ff"`{.backtick}, causing the value to be stored in `color_data`{.backtick}.

Some coding details:

- The property object must be assigned to a class attribute. (This assignment gives the computed attribute its name; the property object itself doesn\'t know the name of the computed attribute that it implements.) The property \"performs\" as a computed attribute only when it is accessed through an instance of the class. Working at Python\'s interactive prompt shows this:

      >>> Widget.color
      <property object at 0x00D8F5A0>
      >>> Widget("#1020fe").color
      (16, 32, 254)

- When an attribute reference causes the property object to dispatch `get_color`{.backtick}, the Widget instance is passed as the sole argument to this function.

- When an assignment statement causes the property object to dispatch `set_color`{.backtick}, two arguments are passed to this function: the Widget instance, and the statement\'s right-hand-side value.

## References 

We haven\'t finished the story on property objects \-- for example, we haven\'t discussed how to implement a computed attribute that handles the statement `del wgt.color`{.backtick}. But if you\'ve gotten this far, it probably makes sense to switch to the official **property** documentation:

- [http://docs.python.org/library/functions.html#property](http://docs.python.org/library/functions.html#property)

Or see a revision of the official documentation, at [AlternativeDescriptionOfProperty](AlternativeDescriptionOfProperty).

(Don\'t get fooled \-- as I was! \-- by the classification of **property** in the documentation as a built-in function. **property** is a built-in data type, like **int**. In Python, data types are directly callable, and so look like functions.)
