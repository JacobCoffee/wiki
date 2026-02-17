# Asking for Help/thread started using 'bg' ends without any notification

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: thread started by \'bg\' ends without any notification 

\...

I already have a tool programmed using python language and I am trying to add a functionality over it. For that purpose I have written certain functions and utilities and I start these functions in separate threads using \'bg \<func_name\>\'. Now some of the threads are dying without any notification or exception.

Here is the output showing threads just after all the threads are started -

    sae_sim In[8]: threading.enumerate
    -------------> threading.enumerate()
    sae_sim Out[8]:

    [<_MainThread(MainThread, started)>,

     <SelectThread(MME UserData Thread, started daemon)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <BackgroundJob: SendData(mme, sgsn, LocalImsi='404660000110000', callNo=10000, delay=2, destIpv4=tunra, destIpv6='', randomize=1)>,     >>>>>>>>>>>>>>>>>>>>>>

     <BackgroundJob: GnGpHand(mme, sgsn, LocalImsi='404660000110000', callNo=10000, delay=2, TAU=1, pco_v1=pco_v1, com_flags=None, randomize=1)>,     >>>>>>>>>>>>>>>>>>>>>>

     <SelectThread(SGSN UserData Thread, started daemon)>,

     <BackgroundJob: MultipleCallsUp(mme, LocalImsi='404660000110000', callNo=5000, delay=1, myApnStr='imsauthapn', ue_tz=None, pco=None, pco_v1=None, com_flags=None, uli_v1=None, rai_v1=None, static=0, trace=1, app_type=APP_TYPES.MME, randomize=1)>,     >>>>>>>>>>>>>>>>>>>>>>

     <SelectThread(EGTP node thread, started daemon)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <_Timer(Thread-1, started)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <BackgroundJob: MultipleCallsUp(sgsn, LocalImsi='404660000115000', callNo=5000, delay=1, myApnStr='imsauthapn', ue_tz=None, pco=None, pco_v1=pco_v1, com_flags=None, uli_v1=None, rai_v1=None, static=0, app_type=APP_TYPES.SGSN, randomize=1)>,     >>>>>>>>>>>>>>>>>>>>>>

     <_Timer(Thread-41, started)>]

Somewhere during the execution \'`<BackgroundJob: MultipleCallsUp(sgsn, LocalImsi='404660000115000', callNo=5000, delay=1, myApnStr='imsauthapn', ue_tz=None, pco=None, pco_v1=pco_v1, com_flags=None, uli_v1=None, rai_v1=None, static=0, app_type=APP_TYPES.SGSN, randomize=1)>`\' thread gets killed and there is no trace on how and why it has ended. Here is the output of threading.enumerate() captured when I understood from the execution stats the some of the threads might have gotten killed -

    --------------> threading.enumerate()
    sae_sim Out[14]:

    [<_Timer(Thread-107597, started daemon)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <BackgroundJob: SendData(mme, sgsn, LocalImsi='404660000110000', callNo=10000, delay=2, destIpv4=tunra, destIpv6='', randomize=1)>,    >>>>>>>>>>>>

     <BackgroundJob: GnGpHand(mme, sgsn, LocalImsi='404660000110000', callNo=10000, delay=2, TAU=1, pco_v1=pco_v1, com_flags=None, randomize=1)>,   >>>>>>>>>>>>>>

     <SelectThread(EGTP node thread, started daemon)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <_Timer(Thread-107607, started daemon)>,

     <_Timer(Thread-107602, started daemon)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <_Timer(Thread-107587, started daemon)>,

     <BackgroundJob: MultipleCallsUp(mme, LocalImsi='404660000110000', callNo=5000, delay=1, myApnStr='imsauthapn', ue_tz=None, pco=None, pco_v1=None, com_flags=None, uli_v1=None, rai_v1=None, static=0, trace=1, app_type=APP_TYPES.MME, randomize=1)>,      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

     <SelectThread(SGSN UserData Thread, started daemon)>,

     <_Timer(Thread-120447, started)>,

     <_MainThread(MainThread, started)>,

     <SelectThread(EGTP node thread, started daemon)>,

     <SelectThread(MME UserData Thread, started daemon)>]

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help]() page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)
