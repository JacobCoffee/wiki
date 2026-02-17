# NeedForSpeed/Goals/Slowdown

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[FredrikLundh](FredrikLundh): The main culprit seems to be try/except. We see the same slowdown both on Intel (Windows XP, Linux) and on PowerPC, using both stock builds and local builds.

To compare, use

    $ python2.4 pybench.py -f out
    $ python2.5 pybench.py -c out

Here\'s what I get (Windows XP, Core Duo, using Tools/pybench from a Python 2.5 checkout):

    Tests:                              per run    per oper.    diff *)
    ------------------------------------------------------------------------
              BuiltinFunctionCalls:      47.58 ms    0.37 us    -4.28%
               BuiltinMethodLookup:      74.67 ms    0.14 us    +2.53%
                     CompareFloats:      44.79 ms    0.10 us    +5.84%
             CompareFloatsIntegers:      70.10 ms    0.16 us    +0.20%
                   CompareIntegers:      63.11 ms    0.07 us    +9.38%
            CompareInternedStrings:      43.49 ms    0.09 us    +6.39%
                      CompareLongs:      48.60 ms    0.11 us    +5.73%
                    CompareStrings:      69.44 ms    0.14 us    +5.53%
                    CompareUnicode:      66.14 ms    0.18 us    +3.92%
                     ConcatStrings:      88.52 ms    0.59 us   -18.14%
                     ConcatUnicode:     154.99 ms    1.03 us    +3.34%
                   CreateInstances:      62.09 ms    1.48 us    +0.56%
           CreateStringsWithConcat:      32.13 ms    0.16 us    +7.85%
           CreateUnicodeWithConcat:      85.84 ms    0.43 us    -0.90%
                      DictCreation:      43.10 ms    0.29 us    +3.89%
                 DictWithFloatKeys:     181.50 ms    0.30 us   +12.21%
               DictWithIntegerKeys:      59.95 ms    0.10 us    +7.29%
                DictWithStringKeys:      56.88 ms    0.09 us    +7.98%
                          ForLoops:      41.83 ms    4.18 us    +9.51%
                        IfThenElse:      59.35 ms    0.09 us    +6.87%
                       ListSlicing:      44.07 ms   12.59 us    -1.41%
                    NestedForLoops:      31.04 ms    0.09 us    +6.93%
              NormalClassAttribute:      68.99 ms    0.11 us    +6.40%
           NormalInstanceAttribute:      65.71 ms    0.11 us    +5.73%
               PythonFunctionCalls:      80.78 ms    0.49 us    +8.59%
                 PythonMethodCalls:      60.44 ms    0.81 us    +3.67%
                         Recursion:      51.86 ms    4.15 us    +3.97%
                      SecondImport:      33.63 ms    1.35 us   +16.05%
               SecondPackageImport:      35.59 ms    1.42 us   +14.56%
             SecondSubmoduleImport:      45.99 ms    1.84 us   +15.60%
           SimpleComplexArithmetic:      35.58 ms    0.16 us   -10.05%
            SimpleDictManipulation:      40.81 ms    0.14 us    +3.95%
             SimpleFloatArithmetic:      53.77 ms    0.10 us    +0.09%
          SimpleIntFloatArithmetic:      56.69 ms    0.09 us   +15.45%
           SimpleIntegerArithmetic:      56.54 ms    0.09 us   +15.52%
            SimpleListManipulation:      37.67 ms    0.14 us   +13.57%
              SimpleLongArithmetic:      31.53 ms    0.19 us    +7.92%
                        SmallLists:      73.81 ms    0.29 us    +3.72%
                       SmallTuples:      68.88 ms    0.29 us    +2.89%
             SpecialClassAttribute:      67.81 ms    0.11 us    +3.75%
          SpecialInstanceAttribute:     113.39 ms    0.19 us    +3.49%
                    StringMappings:     303.42 ms    2.41 us    +0.53%
                  StringPredicates:      87.84 ms    0.31 us    +1.66%
                     StringSlicing:      61.11 ms    0.35 us    +7.70%
                         TryExcept:      76.13 ms    0.05 us   +14.34%
                    TryRaiseExcept:      64.91 ms    4.33 us   +65.58%
                      TupleSlicing:      68.11 ms    0.65 us    +3.28%
                   UnicodeMappings:      70.37 ms    3.91 us    +1.85%
                 UnicodePredicates:      58.85 ms    0.26 us    +3.02%
                 UnicodeProperties:      81.38 ms    0.41 us    +1.87%
                    UnicodeSlicing:      77.97 ms    0.45 us    +0.23%
    ------------------------------------------------------------------------
                Average round time:    3843.92 ms               +5.07%

Here\'s what [SeanReifschneider](SeanReifschneider) gets comparing 2.4.3 to 2.5a2 on a Fedora Core 5 system running on a Dual Xeon 3.2:

    Tests:                              per run    per oper.    diff *)
    ------------------------------------------------------------------------
              BuiltinFunctionCalls:      41.81 ms    0.33 us    -2.43%
               BuiltinMethodLookup:      91.88 ms    0.18 us   -13.07%
                     CompareFloats:      49.91 ms    0.11 us    -5.19%
             CompareFloatsIntegers:      63.44 ms    0.14 us   -11.46%
                   CompareIntegers:      52.81 ms    0.06 us   -18.00%
            CompareInternedStrings:      44.85 ms    0.09 us    -8.47%
                      CompareLongs:      53.50 ms    0.12 us    +3.69%
                    CompareStrings:      71.35 ms    0.14 us    -9.69%
                    CompareUnicode:      55.72 ms    0.15 us    -7.21%
                     ConcatStrings:      82.08 ms    0.55 us    -6.36%
                     ConcatUnicode:     121.84 ms    0.81 us    -3.76%
                   CreateInstances:      68.49 ms    1.63 us    +2.84%
           CreateStringsWithConcat:      29.01 ms    0.15 us    -8.33%
           CreateUnicodeWithConcat:      76.91 ms    0.38 us   -11.24%
                      DictCreation:      47.75 ms    0.32 us   -14.34%
                 DictWithFloatKeys:     135.52 ms    0.23 us    -9.04%
               DictWithIntegerKeys:      57.26 ms    0.10 us   -13.23%
                DictWithStringKeys:      62.15 ms    0.10 us   -15.96%
                          ForLoops:      45.67 ms    4.57 us   -31.84%
                        IfThenElse:      53.73 ms    0.08 us    -6.22%
                       ListSlicing:      42.65 ms   12.18 us    +1.78%
                    NestedForLoops:      35.36 ms    0.10 us   -26.33%
              NormalClassAttribute:      67.79 ms    0.11 us   -10.22%
           NormalInstanceAttribute:      61.76 ms    0.10 us   -12.40%
               PythonFunctionCalls:      87.77 ms    0.53 us    -1.05%
                 PythonMethodCalls:      68.47 ms    0.91 us    +2.42%
                         Recursion:      60.93 ms    4.87 us    -2.75%
                      SecondImport:      38.83 ms    1.55 us    +8.18%
               SecondPackageImport:      39.83 ms    1.59 us    +2.38%
             SecondSubmoduleImport:      46.89 ms    1.88 us    +6.82%
           SimpleComplexArithmetic:      32.82 ms    0.15 us   -28.42%
            SimpleDictManipulation:      44.08 ms    0.15 us    -7.59%
             SimpleFloatArithmetic:      62.23 ms    0.11 us   -19.66%
          SimpleIntFloatArithmetic:      56.77 ms    0.09 us    -9.10%
           SimpleIntegerArithmetic:      56.55 ms    0.09 us   -10.59%
            SimpleListManipulation:      40.31 ms    0.15 us    -0.96%
              SimpleLongArithmetic:      43.67 ms    0.26 us   +25.68%
                        SmallLists:      63.76 ms    0.25 us    -2.36%
                       SmallTuples:      69.34 ms    0.29 us    -1.65%
             SpecialClassAttribute:      68.18 ms    0.11 us   -10.87%
          SpecialInstanceAttribute:     109.69 ms    0.18 us    -6.68%
                    StringMappings:      68.51 ms    0.54 us    -2.83%
                  StringPredicates:      69.00 ms    0.25 us    -0.93%
                     StringSlicing:      53.54 ms    0.31 us    -3.35%
                         TryExcept:      54.63 ms    0.04 us    -0.66%
                    TryRaiseExcept:      64.79 ms    4.32 us   +67.21%
                      TupleSlicing:      76.69 ms    0.73 us    +2.60%
                   UnicodeMappings:      60.11 ms    3.34 us    +1.12%
                 UnicodePredicates:      65.36 ms    0.29 us    +0.01%
                 UnicodeProperties:      71.37 ms    0.36 us    +2.61%
                    UnicodeSlicing:      75.52 ms    0.43 us    -5.89%
    ------------------------------------------------------------------------
                Average round time:    3555.70 ms               -9.29%

Here is a test result, 100 passes, on a FC5 system running on a Pentium M 1.8 laptop:

    Tests:                              per run    per oper.    diff *)
    ------------------------------------------------------------------------
              BuiltinFunctionCalls:      43.54 ms    0.34 us    +0.69%
               BuiltinMethodLookup:      88.30 ms    0.17 us    +0.18%
                     CompareFloats:      52.62 ms    0.12 us    -2.39%
             CompareFloatsIntegers:      75.50 ms    0.17 us    -1.37%
                   CompareIntegers:      83.05 ms    0.09 us    -3.10%
            CompareInternedStrings:      59.15 ms    0.12 us    -2.81%
                      CompareLongs:      58.83 ms    0.13 us    -0.93%
                    CompareStrings:      87.54 ms    0.18 us    -3.40%
                    CompareUnicode:      73.50 ms    0.20 us    -2.14%
                     ConcatStrings:      96.64 ms    0.64 us    +2.06%
                     ConcatUnicode:     142.22 ms    0.95 us    -0.52%
                   CreateInstances:      69.58 ms    1.66 us    +1.47%
           CreateStringsWithConcat:      41.00 ms    0.20 us    -1.49%
           CreateUnicodeWithConcat:      88.92 ms    0.44 us    +0.67%
                      DictCreation:      54.08 ms    0.36 us    -2.47%
                 DictWithFloatKeys:     160.19 ms    0.27 us    -1.63%
               DictWithIntegerKeys:      77.66 ms    0.13 us    -2.55%
                DictWithStringKeys:      75.78 ms    0.13 us    -3.58%
                          ForLoops:      56.91 ms    5.69 us    -4.59%
                        IfThenElse:      75.40 ms    0.11 us    +2.69%
                       ListSlicing:      35.32 ms   10.09 us    +5.15%
                    NestedForLoops:      40.57 ms    0.12 us    -0.23%
              NormalClassAttribute:      83.87 ms    0.14 us    -2.12%
           NormalInstanceAttribute:      78.37 ms    0.13 us    -0.90%
               PythonFunctionCalls:      87.62 ms    0.53 us    +7.32%
                 PythonMethodCalls:      67.41 ms    0.90 us    +4.96%
                         Recursion:      57.98 ms    4.64 us   +14.10%
                      SecondImport:      39.56 ms    1.58 us    +8.29%
               SecondPackageImport:      40.86 ms    1.63 us    +4.11%
             SecondSubmoduleImport:      49.53 ms    1.98 us    +3.31%
           SimpleComplexArithmetic:      41.83 ms    0.19 us   -11.53%
            SimpleDictManipulation:      49.75 ms    0.17 us    -2.89%
             SimpleFloatArithmetic:      70.28 ms    0.13 us    +2.43%
          SimpleIntFloatArithmetic:      72.95 ms    0.11 us    -0.38%
           SimpleIntegerArithmetic:      72.91 ms    0.11 us    -0.41%
            SimpleListManipulation:      44.63 ms    0.17 us    +3.13%
              SimpleLongArithmetic:      39.69 ms    0.24 us    +0.40%
                        SmallLists:      66.57 ms    0.26 us    +0.70%
                       SmallTuples:      72.00 ms    0.30 us    -1.55%
             SpecialClassAttribute:      83.38 ms    0.14 us    -1.04%
          SpecialInstanceAttribute:     135.28 ms    0.23 us    +1.88%
                    StringMappings:      80.21 ms    0.64 us    -0.61%
                  StringPredicates:      73.78 ms    0.26 us    -0.99%
                     StringSlicing:      58.81 ms    0.34 us    -4.23%
                         TryExcept:      89.54 ms    0.06 us    -2.44%
                    TryRaiseExcept:      67.26 ms    4.48 us   +51.57%
                      TupleSlicing:      68.09 ms    0.65 us    +1.16%
                   UnicodeMappings:      69.74 ms    3.87 us    -1.10%
                 UnicodePredicates:      64.22 ms    0.29 us    -0.38%
                 UnicodeProperties:      73.78 ms    0.37 us    +1.02%
                    UnicodeSlicing:      78.28 ms    0.45 us    -1.74%
    ------------------------------------------------------------------------
                Average round time:    4000.30 ms               +0.26%
