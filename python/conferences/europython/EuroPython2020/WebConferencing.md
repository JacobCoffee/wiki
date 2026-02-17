# EuroPython2020/WebConferencing

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here are some of the findings in the webconferencing openspace session and #av-clubroom discord discussion at EuroPython 2020.

# Hardware 

## Webcams 

## Aukey PC-LM1E Webcam SKU ITAN1014662 

Function:

- standard webcam for PC

Pros:

- just works with linux, e.g. with guvcview on ubuntu 20.04
- available, ca. 49 EUR

Cons:

- 65 degress wide angle (so little of \"you\" in lots of \"room around you\")
- default settings seem to be too white, can be adjusted via sw

## Logitech Brio 

Pros:

- camera and microphone are really nice
- plug and play, works on Linux (Ubuntu 20.04)

## Headsets (Headphones with Microphone) 

- wired USB headset,works great on Linux and does some amount of noise cancelation

- [https://www.microsoft.com/accessories/en-us/business/lifechat-lx-4000-for-business/7yf-00001](https://www.microsoft.com/accessories/en-us/business/lifechat-lx-4000-for-business/7yf-00001)

### MPOW HC5 Bluetooth Headset X0016X73LR 

Function:

- over-the-ears BT5 headphones
- Microphone

Pros:

- works as headset with Android phone (speakers+mic)
- works as headphones with PC (speakers only)

Cons:

- **does not work as headset (speakers+mic) with BT4 USB adapter at computer**

- **does not work as headset (speakers+mic) via 1Mii B10 at computer** (not able to switch to \"call\" mode)

## Microphones 

### Blue Yeti Mic 

works very well, but no built in noise cancellation so it picks up everything unless you use it in Cardiod mode with the gain all the way down.

## Bluetooth Adapters 

### 1Mii USB Bluetooth Audio Transmitter B10 EAN X0014UJEH3 

Function:

- for computer it is just a USB \"sound card\"
- internally, it transmits sound output via BT5 to headphones speakers
- internally, it receives sound input via BT5 from headset microphone
- 2 modes, switch by hw button:
  - music - high quality (aptX) - output only
  - call - lower quality - input/output

Pros:

- just a soundcard, keeps all the BT stuff away from computer
- nice for Qubes OS (just forward USB device to VM with teleconf sw)
- nice for Linux and BT5 (not \[m\]any working BT5 adapters yet)
- some stuff \"just works\"

Cons:

- lots of states signalled via single multicolor LED
- misc. state changing inputs via a single hw button
- no \"debugging\" possible if something BT does not work
- just a soundcard, no BT exposed to computer

### plugable Bluetooth USB Adaptor USB-BT4LE X0004WCG5T 

- BT 4.0 LE + classic BT
- just works with Linux (Ubuntu 20.04)

## Other / Unsorted 

### Blackmagic Design ATEM Mini 

\"ATEM Mini switchers make it easy to create professional multi camera production.\"

### Rode Wireless Go Mic 

### Panasonic GX85 camera 

# Software 

## Linux Webcam Software 

### guvcview

- quite to adjust camera parameters
- good video quality
- just works on Ubuntu 20.04

### OBS Studio 

Free and open-source cross-platform streaming and recording program.

Pro:

- working nicely on windows
- packages for Linux, old .deb package + recent snap for Ubuntu 20.04
- powerful processing / mixing / assembling of video output signal from misc sources
- powerful processing of the audio, like noise suppression, gain. also mixing of microphone plus desktop audio is possible.

Con:

- to emulate a virtual webcam (which then can be used by your video conf software)
  - you need an extra plugin and a kernel module and you might need to compile some stuff.

# Online Services 

- zoom.us
- meet.jit.si
- bigbluebutton
- cryptpad

# Other stuff 
