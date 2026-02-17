# JythonClassesInJava

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**NOTE: This documents the pre [NewStyleClasses](NewStyleClasses) world \-- so this style should \*not\* be used for new development against Jython 2.2 or later.**

## Magic fields for Jython objects 

- `__class__`{.backtick}

- `__methods__`{.backtick} This is a list of methods initially exposed by the class. This list can be modified by an instance.

- `__members__`{.backtick} This is a list of attributes for a class. This list can be modified by an instance.

## Hiding functionality from Jython 

- Implement ClassDictInit and set the value of the attribute you wish to hide to null.

- Add the exception PyIgnoreMethodTag to the throws clause of a method for it to be masked by Jython.

## Example Code 

    public class JythonClass extends PyObject implements ClassDictInit {

      /** Field __class__ */
      public static PyClass __class__;

      /** Field __methods__ */
      protected static PyList __methods__;

      /** Field __members__ */
      protected static PyList __members__;

      /** Field exposedtojython */
      protected long exposedtojython;

      /** Field hiddenFromJython */
      protected long hiddenFromJython;

      static {
        PyObject[] m = new PyObject[1];

        m[0] = Py.newString("amethod");

        __methods__ = new PyList(m);
        m = new PyObject[1];
        m[0] = Py.newString("amember");

        __members__ = new PyList(m);
      }

      /**
       * Initializes the object's namespace.
       *
       * @param dict
       */
      static public void classDictInit(PyObject dict) throws PyIgnoreMethodTag {

        dict.__setitem__("ticks", new DateTimeFunc("ticks", 1, 1, 2, true, "ticks"));
        dict.__setitem__("gmtoffset", new DateTimeFunc("gmtoffset", 2, 0, 0, true, "gmtoffset"));

        // hide from python
        dict.__setitem__("classDictInit", null);
        dict.__setitem__("getPyClass", null);
        dict.__setitem__("hideFromJython", null);
        dict.__setitem__("otherHiddenMethod", null);
      }
