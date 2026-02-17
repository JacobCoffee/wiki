# boost.python/list

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Introduction 

\<boost/python/list.hpp\> defines the list class, which \...

## Classes 

Class list \...

## Class list synopsis 

    namespace boost { namespace python { 

    class list : public object
    {
     public:
        list(); 
        explicit  list(object_cref sequence);
        template <class T> explicit list(T const& sequence);

        void append(object_cref);
        template <class T>
        void append(T const& x)
        
        long count(object_cref value) const; 
        template <class T>
        long count(T const& value) const;
        
        void extend(object_cref sequence);
        template <class T>
        void extend(T const& x);
        
        long index(object_cref value) const;
        template <class T>
        long index(T const& x) const;
        
        void insert(int index, object_cref);
        void insert(object const& index, object_cref);
        template <class T>
        void insert(int index, T const& x);
        template <class T>
        void insert(object const& index, T const& x);
        
        object pop();
        object pop(long index);
        object pop(object const& index);

        void remove(object_cref value); // remove first occurrence of value
        template <class T>
        void remove(T const& value);
        
        void reverse(); 

        void sort(); 
        void sort(object_cref cmpfunc);
        template <class T>
        void sort(T const& value)
    };

## Class listconstructors 

list();

Requires:: ??? Effects:: ???

explicit list(object_cref sequence);

Requires::??? Effects::???

## Class list functions 

void append(object_cref); template \<class T\> void append(T const& x)

Requires::??? Effects::???

long count(object_cref value) const; template \<class T\> long count(T const& value) const;

Requires::??? Effects::???

void extend(object_cref sequence); template \<class T\> void extend(T const& x);

Requires::??? Effects::???

long index(object_cref value) const; template \<class T\> long index(T const& x) const;

Requires::??? Effects::???

void insert(int index, object_cref); void insert(object const& index, object_cref); template \<class T\> void insert(int index, T const& x); template \<class T\> void insert(object const& index, T const& x);

Requires::??? Effects::???

object pop(); object pop(long index); object pop(object const& index);

Requires::??? Effects::???

void remove(object_cref value); // remove first occurrence of value template \<class T\> void remove(T const& value);

Requires::??? Effects::???

void reverse();

Requires::??? Effects::???

void sort(); void sort(object_cref cmpfunc); template \<class T\> void sort(T const& value)

Requires::??? Effects::???

## Example(s) 

\...
