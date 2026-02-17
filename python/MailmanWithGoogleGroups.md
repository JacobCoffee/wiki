# MailmanWithGoogleGroups

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[Mailman](http://en.wikipedia.org/wiki/GNU_Mailman) is a piece of software by Barry Warsaw that runs all \@python.org mailing lists. It is a good product, but there is a major flaw with it - in the era of web technologies, it doesn\'t have the web interface that conforms to the modern standard of usability.

Two biggest problems with Mailman:

1.  No search
2.  No thread notifications

Other problems:

1.  No OpenID/OpenAuth login
2.  No way to track read/unread messages in archive
3.  Etc etc.

There are many other features you will find missing from Mailman if you ever used Google Groups interface. The most noticeable one is posting from web-browser. There is a lot of resistance from core Python community for switching to Google Groups from a product in Python, and they can be understood. But it seems that nobody has time to implement all missing features of Google Groups in Mailman, so the only way to enjoy the technical side of communication is to find a way to use Groups with Mailman archive in parallel, so that Mailman posts are appearing in Google Groups and vice versa.

Please, add and clarify these pages if you find the integration of Google Groups with Mailman is a great thing to have.

## Solution 

Create Google Groups mirror of mailing list is quite easy - just follow the instructions at [https://support.google.com/groups/bin/answer.py?hl=en&answer=46387](https://support.google.com/groups/bin/answer.py?hl=en&answer=46387) This will make all messages posted to list automatically appear in the Google Group. The next problem is to make messages from group appear in mailing list.

## Problems 

1\. Messages from Google Groups subscribers did not end up in remote mailing list. This often happens with remote mailing lists that require subscription to post. There should be a way to allow Google Groups subscribers post to Mailman list without additional registration.
