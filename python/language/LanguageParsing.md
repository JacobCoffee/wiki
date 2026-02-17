# LanguageParsing

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Small discussion and evaluation of different parsers.

![(!)](/wiki/europython/img/idea.png "(!)") Please keep wiki links as wiki links, use external links only if there is no existing page for the tool.

::: {}
  --------------------------------------------------------------------------------------------- ----------------------------------------------------------------------- -------------- --------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                          Grammar                                                                 Module         Python                            Comment
  [shlex](http://docs.python.org/lib/module-shlex.html)                                                                                                          C                                                included in the main Python distribution
  [Grako](Grako)                                                                         [PEG](http://en.wikipedia.org/wiki/Parsing_expression_grammar)   Python         2.7+, 3.3+, [PyPy](PyPy)   Tool that takes grammars in EBNF variant & and outputs memoizing (Packrat) PEG parsers in Python. Grako is different from other PEG parser generators in that the generated parsers use Python\'s very efficient exception-handling system to backtrack.
  [reparse](http://reparse.readthedocs.org/en/latest/)                                                                                                           Python/Regex   2.x, 3.x                          Combines Regular Expressions
  [Plex](http://packages.python.org/plex/)                                                                                                                       C                                                lexical analysis module for Python, foundation for [Pyrex](Pyrex) and [Cython](http://cython.org). Plex 2.0.0 is Python 2 only, the version embedded in Cython works in Python 3.x. There is also an [experimental port to Python 3 (tested on Python 3.3)](https://github.com/uogbuji/plex3)
  [Spark](http://pages.cpsc.ucalgary.ca/~aycock/spark/)                                  Earley Parser                                                           Python         2.3+, 3.2+, [PyPy](PyPy)   [PyPI package](https://pypi.org/project/spark-parser/); [github project](https://github.com/rocky/python-spark). This parser is notably used in decompilers like [uncompyle6](https://pypi.org/project/uncompyle6/) where using an *ambigous* grammar is desirable.
  [Yapps](Yapps)                                                                         LL(1)                                                                   Python         1-any, 2-1.5+                     
  [PyLR - (broken link)](http://starship.python.net/crew/scott/PyLR.html)                LR(1) LALR(1)                                                           C                                                
  [kwParsing](http://gadfly.sourceforge.net/kwParsing.html)                                                                                                                                                       
  [PyBison](PyBison)                                                                                                                                             C                                                bison grammar with python code actions
  [Trap](http://www.ercim.org/publication/Ercim_News/enw36/ernst.html)                   LR                                                                                     1.5.1+                            
  [PLY](http://www.dabeaz.com/ply/)                                                      SLR LALR(1)                                                             Python                                           Python Lex-Yacc
  [ToyParserGenerator](http://christophe.delord.free.fr/tpg/index.html)                                                                                                         2.2+                              
  [DParser](http://dparser.sourceforge.net/)                                             GLR                                                                     C              2.2+                              grammar in doc strings
  [PyGgy - (broken link)](http://www.lava.net/~newsham/pyggy/)                           GLR                                                                     Python         2.2.1                             
  [pyPEG](http://fdik.org/pyPEG)                                                         PEG                                                                     Python         2.5+                              
  [parsimonious](http://github.com/erikrose/parsimonious)                                PEG                                                                     Python         2.5+                              
  [SimpleParse](http://simpleparse.sourceforge.net/)                                     \-                                                                                     2.0+                              requires mxTextTools
  [Martel](http://www.biopython.org/DIST/docs/api/public/Martel-module.html)                                                                                     Python         2.0+                              requires mxTextTools
  [mxTextTools](http://www.lemburg.com/files/python/mxTextTools.html)                    \-                                                                      C                                                is not exactly a parser like we\'re used to, but it is a fast text-processing engine
  [pyparsing](https://pyparsing-docs.readthedocs.io/en/latest/)                         PEG, LR                                                                 Python         3.9+                              
  [parcon](http://me.opengroove.org/2011/06/parcon-new-parser-combinator-library.html)                                                                           Python         2.6+                              Parser combinator library, similar to pyparsing
  [ANTLR](http://www.antlr.org/)                                                         LL1+                                                                    Python                                           stand-alone tool in Java. Latest version can produce Python code
  [Yappy](http://www.ncc.up.pt/FAdo/Yappy)                                               LR(0) LR(1) SLR LALR(1)                                                 Python         2.2+                              
  [ZestyParser](http://pypi.python.org/pypi/ZestyParser)                                                                                                         Python                                           Object-oriented, Pythonic parsing
  [Parsing](http://www.canonware.com/Parsing/)                                           LR(1)                                                                   Python         2.5+                              
  [aperiot](http://msdl.cs.mcgill.ca/people/eposse/projects/aperiot)                     LL(1)                                                                   Python                                           uses separate grammar files
  [yeanpypa](http://bitbucket.org/namenlos/yeanpypa)                                                                                                             Python                                           inspired by pyparsing and boost::spirit
  [Wisent](http://seehuhn.de/pages/wisent)                                               LR(1)                                                                   Python         2.4+                              has separate parser input file, parser output is a parse tree
  [RP](http://lparis45.free.fr/rp.html)                                                  na                                                                      Python         2.6+                              Simple parser using rule defined in BNF format
  [LEPL](http://www.acooke.org/lepl/)                                                    Any                                                                     Python         2.6+,3+                           Recursive descent with full backtracking and optional memoisation (which can handle left recursive grammars). So equivalent to GLR, but based on LL(k) core.
  [modgrammar](http://pypi.python.org/pypi/modgrammar)                                   GLR                                                                     Python         3.1+                              Recursive descent parser with full backtracking. Grammar elements and results are defined as Python classes, so are fully customizable. Supports ambiguous grammars.
  [funcparserlib](http://code.google.com/p/funcparserlib/)                               LL(\*)                                                                  Python         2.4+                              Recursive descent parsing library for Python based on functional combinators
  [pydsl](http://pydsl.org)                                                              \-                                                                      Python         2.7+ 3+                           
  [lrparsing](http://pypi.python.org/pypi/lrparsing)                                     LR(1)                                                                   Python         2.6+                              A fast parser, lexer combination with a concise Pythonic interface. Lots of documentation, include example parsers for SQL and Lua.
  [Arpeggio](https://github.com/textX/Arpeggio)                                         PEG                                                                     Python         2.7+, 3.2+                        Packrat parser. Works as interpreter. Multiple syntaxes for grammar definition. Lots of docs, examples and tutorials.
  [textX](https://github.com/textX/textX)                                                                                                                       Python         2.7+, 3.2+                        A high-level meta-language/parser for Domain-Specific Language implementation. Built on top of Arpeggio parser. Inspired by XText. Documentation, examples and tutorials available.
  [pyleri](https://github.com/cesbit/pyleri)                                            LR                                                                      Python         3.2+                              A fast, stand-alone parser which can export a grammar to [JavaScript](./JavaScript.html) ([jsleri](https://github.com/cesbit/jsleri)), Go ([goleri](https://github.com/cesbit/goleri)), C ([libcleri](https://github.com/cesbit/libcleri)) or Java ([jleri](https://github.com/cesbit/jleri)).
  [parglare](https://github.com/igordejanovic/parglare)                                 LR/GLR                                                                  Python         2.7+, 3.3+                        A pure Python LR/GLR parser with integrated scanner (scannerless). Grammar in BNF format. Automata/GLR trace visualization. Full documentation and examples available.
  [lark](https://github.com/lark-parser/lark)                                           LALR(1), CFG                                                            Python         2.7, 3.4+                         LALR(1) for speed or Earley parser for any context-free grammar.
  --------------------------------------------------------------------------------------------- ----------------------------------------------------------------------- -------------- --------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

For faster performance, one may use other parser generator systems and plug them in as modules.

For example:

- [Spirit](./Spirit.html) ([http://spirit.sourceforge.net/](http://spirit.sourceforge.net/)) framework for writing EBNF as C++ code

- [FlexBisonModule](./FlexBisonModule.html) ([http://www.crsr.net/Software/FBModule.html](http://www.crsr.net/Software/FBModule.html))

- [cocktail compiler tools](http://groups.google.com/groups?hl=en&amp;lr=&amp;ie=UTF-8&amp;selm=61g0ff$39g$1@vishnu.jussieu.fr) approach

Example of such usage is [SeeGramWrap](SeeGramWrap) available from Edward C. Jones [Python page](http://members.tripod.com/~edcjones/pycode.html), which is a heavily revised and upgraded version of the ANTLR C parser that is in [cgram](http://members.tripod.com/~edcjones/cgram.tar.gz) (broken link). The lastest verson has been refactored to move some of the complexity from ANTLR to Python.

Martin von Loewis presented a paper at Python10, titled [\"Towards a Standard Parser Generator\"](http://www.python.org/sigs/parser-sig/towards-standard.html) that surveyed the available parser generators for Python.

Additional information on these and other parsers at [Python Parsing Tools](https://github.com/webmaven/python-parsing-tools).

## Books 

- Complete online textbook, titled [\"Parsing: A Practical Guide\"](http://dickgrune.com/Books/PTAPG_1st_Edition/).
