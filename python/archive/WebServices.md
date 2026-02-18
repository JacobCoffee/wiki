# WebServices

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Web Services 

Web services can be generally regarded as functions or functionality of applications or systems exposed over the Web using standardised message formats and typically interfaced to other software using traditional APIs, although \"message-centric\" usage of such services is also possible and may be favoured by certain technologies.

## JSON-RPC 

[JSON-RPC](http://json-rpc.org/) is an increasingly popular Web Services specification that uses the light-weight [JSON](http://json.org/) ([JavaScript](./JavaScript.html) Object Notation) data-interchange format (in comparison to the protocols listed below, which all use XML). JSON-RPC was created in 2004 and implementations exist in [JavaScript](./JavaScript.html), Java, PHP and Perl (among other languages) in addition to Python.

- [python-json-rpc](http://json-rpc.org/wiki/python-json-rpc) The specification website includes a Python implementation.

- [JsonUtils](http://pypi.python.org/pypi/JsonUtils/) is another library that supports JSON-RPC.

## JSON-WSP 

[JSON-WSP](http://en.wikipedia.org/wiki/Jsonwsp) is another JSON based webservice protocol. It is inspired by JSON-RPC but designed with a JSON based description format (like WSDL in SOAP). For the time being there is only a Python based implementation, but a PHP implementation is in progress and will also be openly available.

- Ladon is a multiprotocol approach to creating a webservice. See below, in the SOAP section, for more information.

- [pfacka/jsonwsp](https://bitbucket.org/pfacka/jsonwsp) is another JSON-WSP server and client implementation.

## SOAP 

[SOAP](../archive/SOAP) is a Web services technology favoured in certain environments. The following projects seek to support SOAP and related technologies such as WSDL:

- [zeep](https://github.com/mvantellingen/python-zeep) ([on PyPi](https://pypi.org/project/zeep/)) - Zeep is a modern and high performant SOAP client build on top of lxml and requests. It\'s well maintained, and compatible with Python 2 and 3.

- [suds](https://github.com/suds-community/suds) ([on PyPi](https://pypi.org/project/suds-community/)) - Suds is a lightweight SOAP python client that provides a service proxy for Web Services. This is the best maintained fork of the original Suds project by Jeff Ortel, and it\'s compatible with Python 2 and 3.

- [spyne](https://github.com/arskom/spyne) ([on PyPi](https://pypi.org/project/spyne/)) - Spyne, formerly known as Soaplib, is transport and architecture agnostic RPC library that focuses on exposing services with a well-defined API using popular protocols, including SOAP. It\'s well maintained, and compatible with Python 2 and mostly 3.

- [ladon](https://bitbucket.org/jakobsg/ladon/) ([on PyPi](https://pypi.org/project/ladon/)) - Ladon is a framework for exposing python methods to several internet service protocols. It\'s compatible with Python 2 and 3.

- [pysimplesoap](https://github.com/pysimplesoap/pysimplesoap/) ([on PyPi](https://pypi.org/project/PySimpleSOAP/)) - PySimpleSOAP is a simple and functional client/server. It\'s compatible with Python 2 and 3.

- [osa](https://bitbucket.org/sboz/osa) - osa is a fast/slim easy to use SOAP python client library.

- [Python Web Services](http://sourceforge.net/projects/pywebsvcs) and Zolera Soap Infrastructure (([ZSI on PyPi](https://pypi.org/project/ZSI/)) provides both client and server SOAP libraries. It was very popular, but it\'s a dead project (last release 2007) without any Python 3 support.

## SOAPjr 

- [http://en.wikipedia.org/wiki/SOAPjr](http://en.wikipedia.org/wiki/SOAPjr)

## XML-RPC 

The first popular and largely standardised Web services technology was [XML-RPC](../networking/XmlRpc), supported in Python by the following libraries:

- xmlrpclib - found in the standard library

## XMPP 

More in common with the message-centric usage of [SOAP](../archive/SOAP), [XMPP](http://www.xmpp.org/) - an Internet standard which provides the foundation for the Jabber instant messaging technology - could be used as a Web services protocol. See [PythonXml](../archive/PythonXml) for details of suitable projects.

## Editorial Note 

The above lists should be arranged in ascending alphabetical order - please respect this when adding new solutions. When specifying release dates please use the format YYYY-MM-DD.
