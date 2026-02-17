# PythonVsHaskell

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

See also \[[LanguageComparisons](LanguageComparisons)\].

## Haskell 

Haskell is a modern functional language (like lisp). It\'s not commonly used but the language is used for some \"real\" projects (not just an experimental language) and is becoming more common in industry. For example, the [darcs](http://www.darcs.net/) version control system is written in Haskell. More information can be found at [http://www.haskell.org/](http://www.haskell.org/). (Please forgive or correct any errors here due to my not being very familiar with Haskell.)

------------------------------------------------------------------------

Haskell and Python are a somewhat odd pair to compare, because they are so different in many ways. But what most users of both languages would agree they DO share is a certain elegance of design.

### Functional vs Procedural: 

Haskell is a lazy (evaluate by need), so-called pure functional (no assignments or side-effects) language. It supports parametric polymorphism (ala C++ templates, but more powerful), and ad-hoc polymorphism ( operator overloading) through type classes (ala Java Interfaces). Python offers the programmer a profusion of styles, including procedural, functional, and object-oriented. Lazy programming can be accomplished using generators and itertools. Python has some support for a functional style of programming, but the profusion of side effects and the lack of built-in tail recursion optimization support, makes it an awkward style to use in Python. Haskell supports procedural programming through monads (from category theory) which are also Haskell\'s interface to the world of side effects (e.g. graphics, file systems, sockets, etc.). However, imperative programming is neither Haskell\'s intention nor strength (though this is debateable \-- many Haskell coders have been known to state that Haskell is their favourite imperative language).

### Compiled vs Interpreted: 

Python\'s primary implementation is an interpreter. Haskell has a handful of implementations, including some interpreters (Hugs) and some native-code compilers (GHC, nhc98). Haskell is a high-level language like python, so equal-to-C-or-asm performance should not be expected. The Haskell type system, however, does provide more compile-time information than python\'s does, meaning the optimizing native-code compilers have a speed advantage over python in many cases[http://shootout.alioth.debian.org/gp4/benchmark.php?test=all&lang=python&lang2=ghc](http://shootout.alioth.debian.org/gp4/benchmark.php?test=all&lang=python&lang2=ghc).

The pythonic philosophy of dropping into C for critical sections applies equally well to haskell. Through the foreign function interface, haskell functions can call and be called from C code. As an alternative, compiler-specific extensions (specifically, ghc\'s) and strictness annotations can be used to get closer to the metal.

### Static vs Dynamic Typing: 

Both Haskell and Python have strong (not weak) typing, meaning instances of a type cannot be cast into another type. Explicit conversions must be performed. The difference is that Haskell has static typing, while Python has dynamic typing. This means that in Haskell, the type of every expression and every variable is known at compile time (and strictly enforced), while in Python expressions and variables don\'t even HAVE a type \-- the objects they refer to have types, but that isn\'t known until runtime, and objects can pretend to be different types by providing the correct functions, e.g. \_ \_ len \_ \_, etc. Since typing is such a fundamental part of Haskell (it\'s part of what makes the language easy to reason about), this difference with Python is a fundamental one. However, for those python users who shudder to think of typing \"int i\" before every variable use, take heart: Haskell\'s compilers and interpreters are smart enough to infer the types of your expressions almost all the time, so you don\'t have to type them. Type inference is \"static typing done right.\" For example, to assign a value of 5 to the identifier \'a\', it\'s the exact same code in Python and Haskell:

    a = 5

The fact that it\'s an integer is inferred by the Haskell compiler.

There is also one similarity I feel compelled to point out:

### List Comprehension Syntax: 

Python\'s list comprehension syntax is taken (with trivial keyword/symbol modifications) directly from Haskell. The idea was just too good to pass up.

### Significant Whitespace: 

Both use indentation as syntax. In Python, tabs/spaces *are* the syntax, whereas in Haskell, tabs/spaces are simply well-defined sugar for converting to the braces/semi-colon block syntax. Some would say that Haskell\'s way is an improvement on the idea of significant whitespace by allowing the optional use of explicit braces/semi-colons for blocks, saving certain amounts of headache, e.g. when copy-pasting from web-pages.

### Learning Curve: 

Haskell has a much steeper learning curve for programmers who are not used to functional programming. In many cases, lazy evaluation seems counterintuitive to an imperative-trained mind and you must unlearn techniques to prevent your program from eating up memory.

For me (Nioate), learning [OCaml](http://caml.inria.fr/ocaml/) first smoothed the way into Haskell because ML has a very similar (though less flexible) type system. After understanding the type system, the jump to haskell is much less daunting: beyond new syntax, it only involves learning to utilize lazy evaluation, type classes, and monads. (Don\'t let monads scare you; learn about the list and Maybe monads first. Jeff Newbern\'s [All About Monads](http://horna.org.ua/books/All_About_Monads.pdf) is the best.)

Contributors: [MichaelChermside](MichaelChermside)

See also \[[LanguageComparisons](LanguageComparisons)\].

## Berp: a Python 3 Compiler implemented in Haskell 

Berp ([http://wiki.github.com/bjpop/berp/](http://wiki.github.com/bjpop/berp/)) is an implementation of Python 3. At its heart is a translator, which takes Python code as input and generates Haskell code as output. The Haskell code is fed into a Haskell compiler (GHC) for compilation to machine code or interpretation as byte code.

## Using both Python & Haskell with ctypes (-; 

You can have your cake and eat it too. This is a technique using ctypes to interface with a haskell library compiled with ghc:

### On Linux 

Most of this technique is thanks to Tomáš Janoušek\'s incredibly useful blog entry at [http://blog.haskell.cz/pivnik/building-a-shared-library-in-haskell/](http://blog.haskell.cz/pivnik/building-a-shared-library-in-haskell/). I will merely include the content of the files to show how it can be done. Please visit his site for more details:

First create a test haskell library (Test.hs):

    {-# LANGUAGE ForeignFunctionInterface #-}
    module Test where
     
    import Foreign.C.Types
    import Foreign.C.String
     
    add :: Num a => a -> a -> a
    add x y = x + y


    f1 :: CInt -> IO CInt
    f1 x = do
        return (42 + x)
     
    f2 :: CFloat -> IO CFloat
    f2 x = do
        return (10.0 + x)

    f3 :: CFloat -> IO CFloat
    f3 x = do
        return (add 10.0 x)
        
    f4 :: CString -> IO CString
    f4 s = do
        w <- peekCString s
        newCString (w  ++ " world!")

    foreign export ccall
        f1 :: CInt -> IO CInt

    foreign export ccall
        f2 :: CFloat -> IO CFloat

    foreign export ccall
        f3 :: CFloat -> IO CFloat

    foreign export ccall
        f4 :: CString -> IO CString

Now create Tomas\' shared library entry point (module_init.c):

    #define CAT(a,b) XCAT(a,b)
    #define XCAT(a,b) a ## b
    #define STR(a) XSTR(a)
    #define XSTR(a) #a

    #include <HsFFI.h>

    extern void CAT (__stginit_, MODULE) (void);

    static void library_init (void) __attribute__ ((constructor));
    static void
    library_init (void)
    {
      /* This seems to be a no-op, but it makes the GHCRTS envvar work. */
      static char *argv[] = { STR (MODULE) ".so", 0 }, **argv_ = argv;
      static int argc = 1;

      hs_init (&argc, &argv_);
      hs_add_root (CAT (__stginit_, MODULE));
    }

    static void library_exit (void) __attribute__ ((destructor));
    static void
    library_exit (void)
    {
      hs_exit ();
    }

Then create a build script to compile it all and clean up residuals (build.sh):

    ghc -O2 --make \
          -no-hs-main -optl '-shared' -optc '-DMODULE=Test' \
          -o Test.so Test.hs module_init.c

    rm *.hi *.h *.o
    rm Test_stub.c

You can now easily access the shared library using ctypes (test.py)::

    from ctypes import *

    lib = cdll.LoadLibrary('./Test.so')

    funcs = {
    #    name   restype    argtypes    input  expected value
        'f1':   (c_int,    [c_int],    (10,   52)),
        'f2':   (c_float,  [c_float],  (10.0, 20.0)),
        'f3':   (c_float,  [c_float],  (11.0, 21.0)),
        'f4':   (c_char_p, [c_char_p], ("hello", "hello world!")),
    }

    for func in funcs:
        f = getattr(lib, func)
        f.restype, f.argtypes, test = funcs[func]
        input, expected = test
        assert f(input) == expected
        print '{0}({1}) == {2}'.format(func, input, expected) 
        

you should get:

    f1(10) == 52
    f2(10.0) == 20.0
    f3(11.0) == 21.0
    f4(hello) == hello world!

Enjoy!

Contributers: [AliaKhouri](./AliaKhouri.html)

### On Windows 

Note: this technique may be dated.

First a test haskell program (mylib.hs):

    module Mylib where

    import Foreign.C.Types
    import Foreign.C.String

    adder :: Int -> Int -> IO Int
    adder x y = return (x+y)

    subtractor :: Float -> Float -> IO Float
    subtractor x  y = return (x - y)

    fact :: Int -> Int
    fact n = 
        if n == 1 then 1 else (n * fact (n-1))

    factorial :: Int -> IO Int
    factorial n = return (fact n)


    hello :: CString -> IO CString
    hello w 
     = do
       s <- peekCString w       
       newCString (s ++ "World!")

    mystring :: IO CString
    mystring = newCString "hello world!"

    foreign export stdcall adder :: Int -> Int -> IO Int
    foreign export stdcall subtractor :: Float -> Float -> IO Float
    foreign export stdcall factorial :: Int -> IO Int
    foreign export stdcall hello :: CString -> IO CString
    foreign export stdcall mystring :: IO CString

create file dllMain.c as entry point for the dll:

    #include <windows.h>
    #include <Rts.h>

    extern void __stginit_Mylib(void);

    static char* args[] = { "ghcDll", NULL };
                           /* N.B. argv arrays must end with NULL */
    BOOL
    STDCALL
    DllMain
       ( HANDLE hModule
       , DWORD reason
       , void* reserved
       )
    {
      if (reason == DLL_PROCESS_ATTACH) {
          /* By now, the RTS DLL should have been hoisted in, but we need to start it up. */
          startupHaskell(1, args, __stginit_Mylib);
          return TRUE;
      }
      return TRUE;
    }

compile everything by running this batch file (build.bat):

    REM test making haskell dll
    ghc -c mylib.hs -fglasgow-exts
    ghc -c dllMain.c
    dlltool -A -z mylib.def mylib_stub.o --export-all-symbols
    ghc --mk-dll -o mylib.dll mylib.o mylib_stub.o dllMain.o -optdll-def -optdll mylib.def

    REM cleanup
    rm mylib.o
    rm mylib_stub.o
    rm dllMain.o
    rm mylib.hi
    rm mylib_stub.c
    rm mylib_stub.h

and then having installed ctypes, run the following python script (test_mylib.py) to test it:

    from ctypes import *

    lib = windll.mylib

    api = {
        
    # func name restype argtypes
        'adder' : (c_int, [c_int, c_int]),
        'subtractor': (c_float, [c_float, c_float]),
        'factorial' : (c_int, [c_int]),
        'hello' : (c_char_p, [c_char_p]),
        'mystring' : (c_char_p, []),
    }
            

    for func in api:
        f = getattr(lib, func)
        f.restype, f.argtypes = api[func]
        globals()[func] = f
        
    print adder(1,2)
    print subtractor(10.5, 2.5)
    print factorial(10)
    print hello('hello')
    print mystring()
