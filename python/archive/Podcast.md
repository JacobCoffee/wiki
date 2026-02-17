# Podcast

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Format 

Let\'s try to record a monthly round-table podcast that discusses Python-related events and news.

[Podcast/EpisodePlanning](../people/Podcast/EpisodePlanning)

The [Wikipedia Weekly](http://wikipediaweekly.org/) podcast is a good model for us. Try listening to episode 80 or 81, which are daily wrap-ups from the Wikimania 2009 conference, or episode 78, which is a Skype-recorded episode.

Let\'s aim for 1/2 an hour to an hour of conversation. (Wikipedia Weekly will sometimes be 1.5 hours, but that seems too long; a bit more editing can make the discussion go faster.) We could have short, 5-10 minute episodes that stick to a single topic; one conversation would result in 2-3 episodes.

# Scheduling time 

AMK is available weekends (pretty much any time), and weeknights 7PM-10PM US Eastern (23:00-2:00 UTC).

Brett is available weekends (11:00 Pacific and later), and weeknights typically 19:00 - 23:00 Pacific. Tuesday/Thursday starting at 17:30 Pacific (although Thursday is better). Other days may be negotiable.

Steve, being a poor sad bas\*ard with no life, will attempt to make himself available whenever he can, and looks forward to seeing when everyone else can make it.

# Technical 

Wikipedia Weekly seems to record the audio from one single participant. This means that the audio quality for a remote speaker will occasionally become bad or they\'ll drop out. It would be better, though more effort, if \*everyone\* recorded their audio and sent to it to an editor. That way everyone is represented by a high-quality local recording.

# Workflow 

1\. Write an agenda/list of topics and distribute it to all the participants so they can read up on stuff (or not \-- up to the participant).

2\. Hold a Skype conference call between all the participants. Each participant tries to record their own audio.

3\. Everyone sends their audio to an editor who combines the best of each recording into a single track and edits out glitches and other errors.

4\. Post the audio.

## How to record Skype audio 

[Skype for Interviews](http://www.blogarithms.com/index.php/archives/2007/12/23/skype-for-interviews/) \-- how-to video

[15 Apps for Recording Skype Conversations](http://www.voip-sol.com/15-apps-for-recording-skype-conversations/) \-- Windows/MacOS

Linux tool: [Skype Call Recorder](http://atdot.ch/scr/)

[Record Skype Calls on Ubuntu](http://www.detector-pro.com/2008/08/how-to-record-skype-calls-on-ubuntu.html) (from 2008)

[Recording Skype on Linux](http://www.andrlik.org/blog/2006/feb/17/howto-record-skype-conversations-in-linux/) (from 2006)

We should write a detailed set of instructions here for each platform.

## MacOS 

[Call Recorder](http://www.ecamm.com/mac/callrecorder/) seems to work smoothly.

To use only free software, follow the instructions from [http://zeljkofilipin.com/2009/03/17/recording-a-podcast-with-skype-on-mac-using-only-free-software/](http://zeljkofilipin.com/2009/03/17/recording-a-podcast-with-skype-on-mac-using-only-free-software/) . (These instructions work to make a recording but are not usable, since when you\'re talking, you hear your own voice in your headphones, but with a large enough delay that it\'s really hard to concentrate. \--amk)

Install Audacity, [LineIn](./LineIn.html), and Soundflower (all are free software).

System Preferences/Sound: Output: Built-in Audio or headphones Input: Audio line in for mic

### Skype 

Audio output: Soundflower (2ch) Audio input: Soundflower (2ch)

### Audacity 

Audio playback: Built in Output Audio recording: Soundflower (2ch)

### LineIn Application 

Input from: Built-in Audio: Line In (ie the Mic) Output to [SoundFlower](./SoundFlower.html) (2ch)

And then click the 'Pass Thru' Button in [LineIn](./LineIn.html) to actually begin transferring audio between the input and output.

## Linux 

## Windows 
