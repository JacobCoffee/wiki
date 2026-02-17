# Response

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Building **Response** object is a common way to return information from URL handler back to web framework for returning to client:

- Django: [https://docs.djangoproject.com/en/1.7/ref/request-response/#httpresponse-objects](https://docs.djangoproject.com/en/1.7/ref/request-response/#httpresponse-objects)

- Flask: [http://flask.pocoo.org/docs/0.10/api/#response-objects](http://flask.pocoo.org/docs/0.10/api/#response-objects)

- Bottle: [http://bottlepy.org/docs/dev/tutorial.html#tutorial-response](http://bottlepy.org/docs/dev/tutorial.html#tutorial-response)

- webapp2/WebOb: [http://webapp-improved.appspot.com/api/webapp2.html#webapp2.Response](http://webapp-improved.appspot.com/api/webapp2.html#webapp2.Response)

::: {}
+:---------------------------------------------------------------------------------------------------------------:+:-----------------------------------:+
| **Default Content-Type**                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [Django](https://docs.djangoproject.com/en/1.7/ref/request-response/#django.http.HttpResponse.__init__) | text/html; charset=utf-8            |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [Flask](http://flask.pocoo.org/docs/0.10/api/#response-objects)                                          | text/html; charset=utf-8            |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [Bottle](http://bottlepy.org/docs/dev/tutorial.html#generating-content)                                  | ﻿text/html; charset=utf-8\           |
|                                                                                                                 | application/json\                   |
|                                                                                                                 | \<empty\>                           |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [webapp2/WebOb](http://webapp-improved.appspot.com/guide/response.html#guide-response)                   | ﻿﻿text/html; charset=utf-8            |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
:::
