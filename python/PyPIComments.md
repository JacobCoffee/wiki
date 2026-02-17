# PyPIComments

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The Python Package Index currently provides a feature where users can comment on individual packages. Some package maintainers are opposed to such a feature, and would like to leave activation of the feature up to the maintainer. Along with comments, there is also support for rating the package with a number from 0 to 5. This page discusses arguments in favor and against per-package comments.

There is also a discussion on [Catalog-SIG](http://mail.python.org/mailman/listinfo/catalog-sig) starting with [an email by Martin](http://mail.python.org/pipermail/catalog-sig/2009-October/002236.html) (who implemented the feature) and continuing in the [November archive](http://mail.python.org/pipermail/catalog-sig/2009-November/thread.html).

# Pro comments 

- users posting a rating not only want to indicate whether they like or dislike the package, but also why they rated the package in the way they did.
- restricting users (not allowing them comment on certain packages) can be considered as a form of censorship
- spam is largely prevented by requiring user to login; if spam (i.e. completely unrelated comments) are made, they can be deleted.
- if users use the facility to report bugs, the package author should have more clear directions to point users to the bug reporting channels
- new comments will be emailed to the maintainers to notify them

# Contra comments 

- maintainers need to check one more place for discussion of the package, in addition to mailing lists and fora that they already operate; people are too lazy to research what the proper comment reporting channel is.
- if PyPI would allow individual packages to opt out of commenting, then comments would still be possible on packages that want them (or don\'t mind receiving them).
- if comments get posted, the maintainer should have the ability to delete comments that are inappropriate.
- preventing commenting isn\'t censorship; people are free to comment on as many other websites, blogs, forums, as they like\... and if relevant to the package, they\'ll be found by Google
- Requiring spam handling to go through a central authority makes two people (author + PyPI maintainer) do the work that could be done by one\... or not at all.
- \"Completely unrelated\" comments are only one form of spam; consider, for example the Twitter campaign urging people to post negative comments on setuptools to express a political viewpoint about its maintenance process, rather than commenting on the software itself
- The feature itself does not encourage quality comments, due to the small space and lack of formatting/editing.
- Early use of the comment feature suggests that low-quality comments are likely to be the norm: providing little useful information to users and poor feedback to package authors.
- MvL notes that the comment feature was specifically requested as a way for people to leave public \*negative\* comments about packages - not to provide informative discussion or feedback.
- Contra MvL\'s arguments, users do not have a \"right\" to display their gripes on a package\'s listing, any more than they have a \"right\" to scrawl grafitti on a restaurant wall to criticize the food. They have a right to comment and complain, but that can be equally served by simply sending their feedback directly to the package author, rather than permanently displaying one side of that conversation.

For more contra arguments, see also [this Sourceforge issue](http://sourceforge.net/tracker/?func=detail&atid=513503&aid=2872293&group_id=66150) with input from many package authors and community members.

# Poll 

There is a public poll running to determine what users think of the rating and commenting features.

To vote, go to [http://pypi.python.org](http://pypi.python.org) and log in; the home page will offer you the chance to vote in the poll.
