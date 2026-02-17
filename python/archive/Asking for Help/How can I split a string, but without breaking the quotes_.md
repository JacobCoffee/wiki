# Asking for Help/How can I split a string, but without breaking the quotes?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How can I split a string, but without breaking the quotes 

I\'m trying to split a string, but without breaking the quotes

    x = '"a,b", c, d, "e,f,h", "i,j,k"'
    re.sub('"([^"]*)"', "\g<1>", x) 
    -> 'a,b, c, d, e,f,h, i,j,k' # Ok for me

    re.sub('"([^"]*)"', "|\g<1>|", x)
    -> '|a,b|, c, d, |e,f,h|, |i,j,k|'   # To show the separation of the groups, also Ok

    re.sub('"([^"]*)"', "\g<1>".replace(",", "|"), x)
    -> 'a,b, c, d, e,f,h, i,j,k' # The same result!
    -> 'a|b, c, d, e|f|h, i|j|k' # It doesn't suppose to replace all "," with "|" like here?

Answer: No, it is doing what you told it to do. To realize this you must know that arguments are evaluated before they are passed to the functions. But what is the value of this\...?

    "\g<1>".replace(",", "|")

It is `"\g<1>"`{.backtick}, of course, as there are no commas to replace in `"\g<1>"`{.backtick}. re.sub therefore receives `'"([^"]*)"'`{.backtick} and `"\g<1>"`{.backtick} as arguments, which is the exact equivalent of the first call.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
