# Voicent Simple Telephone Call API

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The Voicent Python Simple Interface class contains the following functions.

- callText callAudio callStatus callRemove callTillConfirm

These functions are used to invoke telephone calls from your Python program. For example, callText is used to call a specified number and automatically play your text message using text-to-speech engine.

In order for this class to work, you\'ll need to have Voicent Gateway installed somewhere in your network. This class simply sends HTTP request for telephone calls to the gateway. Voicent has a free edition for the gateway. You can download it from [http://www.voicent.com/download](http://www.voicent.com/download)

More information can be found at: [Python Simple Telephone Call API](http://www.voicent.com/devnet/docs/pyapi.htm)
