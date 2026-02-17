# CloudPyPI

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Cloud PyPI - Mirroring PyPI in the cloud 

*Update:* This project is now canceled, since PyPI is being on hosted on a fastly CDN and the PyPI server itself is hosted on a VM at OSL/OSU.

## Idea 

We are setting up a PyPI mirror of the static content of PyPI in Amazon [CloudFront](./CloudFront.html).

## Proposal 

- [CloudPyPI/Proposal](CloudPyPI/Proposal)

The proposal was accepted by the PSF in their December 2010 board meeting.

Funding was limited to an initial USD 500 for Amazon costs to see whether the project would succeed.

## Resources 

- [Amazon AWS Getting Started Guide](http://docs.amazonwebservices.com/AmazonCloudFront/2010-11-01/GettingStartedGuide/)

- [Developer Intro to the PyPI code](CheeseShopDev)

- [PyPI RPC interface](PyPIXmlRpc) (which we likely won\'t use, but gives an idea of how the meta data is stored)

- [PyPI Code](https://bitbucket.org/loewis/pypi)

## Example CDN 

We\'ve setup an example CDN which only provides caching services to the PyPI server and uses the pypi.python.org server as origin:

- [https://d1t66zoqn9vlte.cloudfront.net/simple/](https://d1t66zoqn9vlte.cloudfront.net/simple/)

- For more details on the used setup, please see [CloudPyPI/ExampleCDN](CloudPyPI/ExampleCDN)

## Team 

Implementation:

- [Marc-André Lemburg](MarcAndreLemburg)

- [Grig Gheorghiu](GrigGheorghiu)

- [Neil Schemenauer](NeilSchemenauer)

- [Vern Ceder](VernCeder)

Helping with the PyPI code:

- Richard Jones
- Martin von Löwis

## Mailing List 

- [cloud-pypi@lists.egenix.com](mailto:cloud-pypi@lists.egenix.com) (private to the project team)

## Amazon EC2: Project Development Server 

- [CloudPyPI/DevelopmentServer](./CloudPyPI(2f)DevelopmentServer.html)

## Amazon S3 

- [CloudPyPI/S3](./CloudPyPI(2f)S3.html)

## Access Control 

- [CloudPyPIGroup](CloudPyPIGroup)

This is a public page. Please don\'t add any sensitive information to the page. Instead, create subpages that are only available to team members.

Please put the following ACL line at the top of subpages with sensitive information:

    #acl CloudPyPIGroup:read,write,revert,admin All:
