# CodingStandards

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

When contributing code or patches to Jython, please try to follow these guidelines.

## Python Code 

In general, follow [PEP 8](http://www.python.org/dev/peps/pep-0008/). When importing Java code, always use fully qualified class names, not package names ie from java.lang import String instead of from java import lang.

## Java Code 

- Javadoc on any publicly exposed method or field.

- 4 spaces for indentation, no tabs.

- No nested ternary statements (no ternary statments inside other ternarys).

- A luxurious 100 characters per line.

- No copy and pasted, repeated code: if you\'re doing the same thing twice, make a method.

- Braces on all loops and if else statements

- A space between an if and its parenthesis i.e. `if (`{.backtick} instead of `if(`{.backtick}.

- Spaces between annotation element-value pairs. i.e. `@ExposedType(name = "unicode", base = PyBaseString.class)`{.backtick} instead of `@ExposedType(name="unicode",base=PyBaseString.class)`{.backtick}

- Methods longer than 10 lines should have whitespace and comments breaking them up into coherent operations.

- Descriptive names for fields and methods.

- [No \@author tags in code.](http://producingoss.com/en/managing-volunteers.html#territoriality)

- Any field on an object that isn\'t modified after construction should be final.

- Fields at the top of the class.

- Don\'t declare fields with their default values ie `private Object blah;`{.backtick} instead of `private Object blah = null;`{.backtick} and `int i;`{.backtick} instead of `int i = 0;`{.backtick}

- Comments begin with a space unless they\'re commented out code:

<!-- -->

       Wrong:
       //XXX: Foo needs refactoring
       // bar.bar()
       Correct:
       // XXX: Quux is flakey
       //Baz baz = new Baz()

Beyond these rules, follow the [Sun Java standards](http://www.oracle.com/technetwork/java/javase/documentation/codeconvtoc-136057.html).

[Eclipse_Formatting.xml](attachments/CodingStandards/Eclipse_Formatting.xml) can be imported into Eclipse to get it to follow the standards.

### Example (adapted from Sun document) 

    package org.jython.blah;
    import org.jython.blah.BlahBlah;
    /**
     * Class description goes here.
     */
    public class Blah extends SomeClass {
        /* A class implementation comment can go here. */
        /** classVar1 documentation comment */
        public static int classVar1;
        /**
         * classVar2 documentation comment that happens to be
         * more than one line long
         */
        private static Object classVar2;
        /** instanceVar1 documentation comment */
        public Object instanceVar1;
        /** instanceVar2 documentation comment */
        protected int instanceVar2;
        /** instanceVar3 documentation comment */
        private Object[] instanceVar3;
        /**
         * ...constructor Blah documentation comment...
         */
        public Blah() {
            // ...implementation goes here...
        }
        /**
         * ...method doSomething documentation comment...
         */
        public void doSomething() {
            // ...implementation goes here...
        }
        /**
         * ...method doSomethingElse documentation comment...
         * @param someParam description
         */
        public void doSomethingElse(Object someParam) {
            // ...implementation goes here...
        }
    }
