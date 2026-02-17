# CloudPyPI/ExampleCDN

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Cloud PyPI \-- Example CDN 

In order to test drive a PyPI CDN, we\'ve setup an example CDN on Amazon Cloudfront for pypi.python.org.

- [https://d1t66zoqn9vlte.cloudfront.net/simple/](https://d1t66zoqn9vlte.cloudfront.net/simple/)

## Settings 

These are the settings:

- Origin: pypi.python.org

- Default Root Object: pypi

- Origin Protocol Policy: HTTP [OnlyMatch](./OnlyMatch.html) Viewer

- Viewer Protocol Policy: HTTPS Only

- Minimum TTL: 3600

- No forwarding of cookies or query strings

As a result, the CDN is only available over HTTPS (there\'s no redirect in place) and the content is fetched from PyPI using HTTPS as well.

The TTL is set to a low value for testing purposes. For a deployment, the value can be set to a much higher value for the package pages; and a lower value for the /simple/ index itself.

*Note:* Without cache headers in the PyPI response (it currently doesn\'t send cache headers), the default TTL for the cache retention is 24h, according to the Amazon documentation.

## Example fetching the /simple/ index 

First request:

    200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 1323539
    Connection: keep-alive
    Server: nginx/1.1.19
    Date: Thu, 28 Feb 2013 13:56:22 GMT
    Strict-Transport-Security: max-age=86400
    X-Amz-Cf-Id: vXAxMoustlCxyzFAVjjg3EUJG5OgP-ALefiF1mbvbJlW9ZsHCxtdLg==
    Via: 1.0 3dee24f419c49cc32df542a9410fda87.cloudfront.net (CloudFront)
    X-Cache: Miss from cloudfront

Second request:

    200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 1323539
    Connection: keep-alive
    Server: nginx/1.1.19
    Date: Thu, 28 Feb 2013 13:56:22 GMT
    Strict-Transport-Security: max-age=86400
    Age: 337
    X-Amz-Cf-Id: -2COLjgkKLDF83jrr0iFahyAO4UGOMB0hXNM_ROMFJQpII1goFyi-A==
    Via: 1.0 3dee24f419c49cc32df542a9410fda87.cloudfront.net (CloudFront)
    X-Cache: Hit from cloudfront

## Issues found in the experiment 

- The URL is not easy to remember

  It\'s possible to setup a nicer URL for the CDN, but even then, the URL will still read `something.cloudfront.net`. Unfortunately, we cannot use CNAMEs for this, e.g. use pypi-cdn.python.org as name, since the HTTPS verification would not work with this URL. It would be possible to install a redirect from pypi-cdn.python.org to the something.cloudfront.net URL - at a cost: if the redirector is down, the CDN would not be reachable via the nicer URL.
