# Email SIG/DesignOverviewProposal

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The email package consists of two major conceptual pieces: the API, and the internal data model. The API needs to have facilities for accepting data in either text format or bytes format, and this data is used to generate a model of the input message (a Message). Likewise the API needs to provide facilities for serializing a Message as either bytes or text. The API also provides ways to build up a Message from pieces, or to extract information from a Message in pieces, and to modify a Message, and again input and output as both text and bytes must be supported, except that in some cases text output may not make sense (eg: binary attachments).

The data model used by the email package is an \"implementation detail\", and we should not spend effort at this stage trying to optimize it for anything except memory requirements with respect to potentially large sub-objects, and even there it is more a matter of providing ways to deal with potentially large sub-objects than it is a true optimization. In general correctness and robustness is much more important than speed.

The data model will need to be a practical hybrid of the input data, possibly transformed in some way in some cases, and various sorts of meta-data. The current email package already works this way.

An important characteristic of the model is that it be invertable whenever sensible; that is, if a given byte stream is used to create a Message or subobject, serializing that Message or subobject as bytes should return the original byte stream whenever sensible (ie: when the data is not pathologically malformed). Likewise if a text stream is used to create a Message or subobject, serializing it as text should produce, whenever sensible, the original text stream. In particular, well-formed (per RFC) message data should always come out of a round trip through the email module in exactly the format it went in.

An important property of the API is that both the parser that transforms an input stream into a Message and Message serialization should not raise exceptions. Instead a defects list is maintained and exposed through the API. In the face of some defects it may not be sensible to maintain invertability. In the worst case for parser input the resulting Message object may have no headers, a binary blob body, and a defect list, but a Message object will always be produced.

The APIs that manipulate the data model either for piecewise construction or for transformations may raise exceptions, and in most cases *should* raise exceptions when encountering invalid data or operations. APIs that query the model should return as much information as possible without throwing an exception. (The current proposal to implement this is to return objects that have defect lists, and/or raise exceptions when methods of the object are called that would have worked if the input data were valid, leaving the queryable object itself in the hands of the application so that the application has the maximum possible information available to try to handle the error if it wishes to do so.)
