# EasyAsPy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This probably shouldn\'t be the first example, but it\'s a nice one:

------------------------------------------------------------------------

My requirement was

I want a list of all ordered permutations of a given length of a set of tokens. Each token is a single character, and for convenience, they are passed as a string in ascending ASCII order.

For example

permute(\"abc\",2)

should return ` ["aa","ab","ac","ba","bb","bc","ca","cb","cc"] `

and permute(\"13579\",3) should return a list of 125 elements

` ["111","113", ... ,"997","999"] `

------------------------------------------------------------------------

Ask the experienced coder to code this up in the language of his or her choice. Then show them this (contributed by castironpi):

     def p(a,b):
            if not b: return ['']
            return [i+j for i in a for j in p(a,b-1)]

------------------------------------------------------------------------

[CategoryAdvocacy](CategoryAdvocacy)
