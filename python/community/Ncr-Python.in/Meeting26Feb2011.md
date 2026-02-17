# Ncr-Python.in/Meeting26Feb2011

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Details 

- Venue : Sarai-CSDS 29 Rajpur Road Civil Lines Delhi - 110054 India
  - Ph no: 91-11-23928391, 23942199

==Agenda==

- There was no agenda as such this meeting being the first one.

### Minutes 

\*Meeting started at around 2.15 Pm , we started the discuss why we were here and how we can improve on the attendance, everyone agreed on having a central location as meeting place , IITD is one of such potential venue proposed for future meetings.

the points which were discussed in order to make Python the language of choice were

- Promoting Python
- Meetups (Regular Meetups) , find a place in center of Delhi IITD, any other suggestions welcome
- Finding Out Speaker in NCR for Python talks/workshops, Some suggestions we short listed from mailing list and people we
  - know

  <!-- -->

  - 1\) Arulalan.T \-- IITDelhi - CDAT, [NumPy](NumPy)

  - 2\) Rajat Khandelwal (Panda3d, Modelling engine Blender3d, ) [rajatgupta59@gmail.com](mailto:rajatgupta59@gmail.com)

  - 3\) Nandeep Mali \<[n9986.mali@gmail.com](mailto:n9986.mali@gmail.com)\> - [GameDeveloper](./GameDeveloper.html)

  - 4\) Amit Singh Sethi - \<[amit.pureenergy@gmail.com](mailto:amit.pureenergy@gmail.com)\> -Scipy,Numpy

  - 5\) Tavish Naruka \<[tavishnaruka@gmail.com](mailto:tavishnaruka@gmail.com) -realtime audio processing

  - 6\) Vijay shanker \<[deontics@gmail.com](mailto:deontics@gmail.com)\> - web developer

  - 7\) Rakesh Kumar \<[kumar3180@gmail.com](mailto:kumar3180@gmail.com) - Ghaziabad (Django )

  - 8\) Rohan Malhotra \<[yourbuddyrohan@gmail.com](mailto:yourbuddyrohan@gmail.com) ( webpy )

  - 9\) Tarun Arora \<[silent.arora@gmail.com](mailto:silent.arora@gmail.com)

  - 10\) Vivek Khurana

  - 11)Priya Kuber

  - Learning Python

  - Introduction in colleges.

  - Representing NCR in [PyCon](PyCon) India.

  - We wish to have a Python India (Pycon India ) In NCR area by 2011.

  Started exploring the bluetooth module in python Narendra demostrated some code , in the meantime Prof Kanan came in and st tarted talking about his work involving Scilab and Spoken tutorials , explored Sarai then we all dispersed .

==Coding==

- [http://people.csail.mit.edu/albert/bluez-intro/c212.html](http://people.csail.mit.edu/albert/bluez-intro/c212.html)

- [https://github.com/karulis/pybluez/wiki](https://github.com/karulis/pybluez/wiki)

- [http://lightblue.sourceforge.net/](http://lightblue.sourceforge.net/) Code:

<!-- -->

- bluetooth.discover_devices(lookup_names = True) import bluetooth target_name = \"firepower-0\" target_address = None nearby_devices = bluetooth.discover_devices() for bdaddr in nearby_devices:
  - if target_name == bluetooth.lookup_name( bdaddr ):
    - target_address = bdaddr break

  if target_address is not None:
  - print \"found target bluetooth device with address \", target_address

  else:
  - print \"could not find target bluetooth device nearby\"

  <!-- -->

  - ==Attendees==

\* Satyakam Goswami \* [GauravLuthra](./GauravLuthra.html) \* Anuvrat Parashar \* Vivek Chugh \* Narendra Sisodiya \* Arulalan \* Priya Kuber \* Nandeep Mali \* Prof Kannan Moudgalya

Pictures:http://www.satyaakam.net/meetings/NCR_python26feb2011/
