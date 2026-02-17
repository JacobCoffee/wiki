# CAPI CookBook

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Describe CAPI [CookBook](./CookBook.html) here.

## Functions for returning an error with one call 

    PyObject *EXPP_ReturnPyObjError( PyObject * type, char *error_msg )
    {                               /* same as above, just to change its name smoothly */
            PyErr_SetString( type, error_msg );
            return NULL;
    }

    int EXPP_ReturnIntError( PyObject * type, char *error_msg )
    {
            PyErr_SetString( type, error_msg );
            return -1;
    }

## Return in incremented reference 

    PyObject *EXPP_incr_ret( PyObject * object )
    {
            Py_INCREF( object );
            return ( object );
    }

## Check sequence type 

    /*****************************************************************************/
    /* Description: Checks whether all objects in a PySequence are of a same  */
    /*              given type.  Returns 0 if not, 1 on success.             */
    /*****************************************************************************/
    int EXPP_check_sequence_consistency( PyObject * seq, PyTypeObject * against )
    {
            PyObject *ob;
            int len = PySequence_Length( seq );
            int i, result = 1;

            for( i = 0; i < len; i++ ) {
                    ob = PySequence_GetItem( seq, i );
                    if( ob == Py_None )
                            result = 2;
                    else if( ob->ob_type != against ) {
                            Py_DECREF( ob );
                            return 0;
                    }
                    Py_DECREF( ob );
            }
            return result;          /* 1 if all of 'against' type, 2 if there are (also) Nones */
    }

## Tuple Prepend 

    /*
     * Helper function for subtypes that use the base types methods.
     * The command below needs to have args modified to have 'self' added at the start
     * ret = PyObject_Call(PyDict_GetItemString(PyList_Type.tp_dict, "sort"), args, keywds);
     *
     * This is not easy with the python API so adding a function here,
     * remember to Py_DECREF the tuple after
     */
    PyObject * EXPP_PyTuple_New_Prepend(PyObject *tuple, PyObject *value)
    {
            PyObject *item;
            PyObject *new_tuple;
            int i;

            i = PyTuple_Size(tuple);
            new_tuple = PyTuple_New(i+1);
            PyTuple_SetItem(new_tuple, 0, value);
            Py_INCREF(value);
            while (i) {
                    i--;
                    item = PyTuple_GetItem(tuple, i);
                    PyTuple_SetItem(new_tuple, i+1, item);
                    Py_INCREF(item);
            }
            return new_tuple;
    }

## Methods into dictionary 

    /* this function adds methods to a dictionary.
     * in cases where the methods do not go into a module as is useual
     * - for instance if you want to add methods to a type
     */
    void EXPP_PyMethodsToDict(PyObject *dict, struct PyMethodDef *meth)
    {
            PyObject *value;
            while (meth->ml_name) {
                    value = PyCFunction_New(meth, NULL);
                    PyDict_SetItemString(dict, meth->ml_name, value);
                    Py_DECREF(value);
                    meth++;
            }
    }

## Anonymous Pointer Comparison 

**add to the header\...**

    /* for anonymous comparisons */
    typedef struct {
            PyObject_HEAD
            void * pointer;
    } BPyAnonymousObject;

**comparison function\...**

    /*
     * This is to compare any 2 types that have a pointer directly after the
     * PyObject in their struct, this covers quite a few.
     * */

    int EXPP_Anonymous_compare( BPyAnonymousObject * a, BPyAnonymousObject * b )
    {
            return ( a->pointer == b->pointer) ? 0 : -1;
    }

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
