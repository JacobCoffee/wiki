# DbusExamples

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The [D-Bus library](http://www.freedesktop.org/wiki/Software/dbus) is a messaging library used by various desktop environments (GNOME, KDE, etc) for interprocess communication.

There are multiple Python bindings for DBus:

- GDbus and [QtDbus](./QtDbus.html) are wrappers over the C/C++ APIs of GLib and Qt

- [pydbus](https://github.com/LEW21/pydbus) is a modern, pythonic API with the goal of being as invisible a layer between the exported API and its user as possible

- [dasbus](https://github.com/rhinstaller/dasbus) is a Python3-only alternative to pydbus with additional features and better flexibility

- [dbus-python](https://dbus.freedesktop.org/doc/dbus-python/) is a legacy API, built with a deprecated dbus-glib library, and involving a lot of type-guessing (despite \"explicit is better than implicit\" and \"resist the temptation to guess\").

- [txdbus](https://pypi.python.org/pypi/txdbus) is a native Python implementation of the D-Bus protocol for the Twisted networking framework.

- [dbus-next](https://pypi.org/project/dbus-next/) is a native Python library for D-Bus with support for multiple IO backends suitable for GUI develeopment and cross platform projects.

- [python-sdbus](https://github.com/python-sdbus/python-sdbus) modern D-Bus library supporting both asyncio and blocking calls, unified client-server classes and type hints.

See also: [DBusBindings](https://www.freedesktop.org/wiki/Software/DBusBindings/#python) on Freedesktop wiki.

The `dbus-viewer`{.backtick} and `qdbusviewer`{.backtick} programs let you browse through the services and interfaces available on your system.

# pydbus

For more information see [pydbus\'s Readme](https://github.com/LEW21/pydbus/blob/master/README.rst).

## Introspection 

    from pydbus import SessionBus
    bus = SessionBus()

    # Create an object that will proxy for a particular remote object.
    remote_object = bus.get(
        "org.freedesktop.DBus", # Bus name
        "/org/freedesktop/DBus" # Object path
    )

    # Introspection returns an XML document containing information
    # about the methods supported by an interface.
    print("Introspection data:\n")
    print(remote_object.Introspect())

Output:

    Introspection data:

    <!DOCTYPE node PUBLIC "-//freedesktop//DTD D-BUS Object Introspection 1.0//EN"
    "http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd">
    <node>
      <interface name="org.freedesktop.DBus.Introspectable">
        <method name="Introspect">
          <arg name="data" direction="out" type="s"/>
        </method>
      </interface>
      <interface name="org.freedesktop.DBus">
        <method name="RequestName">
          <arg direction="in" type="s"/>
          <arg direction="in" type="u"/>
          <arg direction="out" type="u"/>
        </method>
     ...

## Calling an interface method 

After executing the introspection example:

    print(remote_object.ListNames())

Output:

    ['org.freedesktop.DBus', 'org.freedesktop.Notifications', 'org.freedesktop.PowerManagement', ':1.8', ':1.9', 'org.kde.kaccess', 'org.kde.kded', 'org.kde.StatusNotifierItem-655-1', 'org.freedesktop.systemd1', 'org.ktorrent.ktorrent', 'org.kde.StatusNotifierItem-656-1', 'org.kde.konversation', 'org.pulseaudio.Server', 'org.kde.KScreen', 'org.kde.krunner', 'org.kde.konsole', ':1.40', 'org.a11y.Bus', ':1.41', ':1.42', ':1.20', ':1.43', 'org.kde.klauncher5', ':1.21', ':1.23', 'org.kde.dolphin-3012', 'org.freedesktop.PowerManagement.Inhibit', 'org.kde.Solid.PowerManagement', ':1.24', ':1.25', ':1.49', 'org.kde.kmix', 'org.kde.screensaver', 'org.kde.KWin', 'org.bluez.obex', ':1.29', 'ca.desrt.dconf', 'org.kde.kgpg', 'org.freedesktop.ScreenSaver', 'org.kde.plasmashell', 'org.kde.plasmanetworkmanagement', 'org.kde.StatusNotifierItem-666-1', 'org.kde.kglobalaccel', 'org.freedesktop.FileManager1', 'org.kde.kwalletd5', 'org.PulseAudio1', 'org.kde.polkit-kde-authentication-agent-1', ':1.93', 'org.kde.kded5', 'org.kde.ActivityManager', 'org.kde.keyboard', 'org.kde.kate-3030', ':1.31', 'org.kde.kuiserver', ':1.32', ':1.55', ':1.33', ':1.11', 'org.kde.kwin.Screenshot', ':1.56', ':1.34', 'org.kde.StatusNotifierWatcher', 'org.kde.JobViewServer', ':1.35', ':1.0', ':1.13', ':1.58', 'org.kde.StatusNotifierHost-616', ':1.14', ':1.59', ':1.15', ':1.38', ':1.16', 'org.kde.ksmserver', ':1.39', ':1.17', ':1.5', 'org.kde.Solid.PowerManagement.PolicyAgent', ':1.18', 'org.kde.klauncher', ':1.6', ':1.19']

The following example makes your system hibernate:

    # Get the power management object
    power = bus.get('org.gnome.PowerManager', '/org/gnome/PowerManager')

    # Hibernate the system
    if power.CanHibernate():
        power.Hibernate()

# dasbus

For more information see [dasbus\'s documentation](https://dasbus.readthedocs.io/).

## Introspection of a remote object 

Introspection returns an XML string containing information about interfaces, methods, properties and signals of the remote object.

    from dasbus.connection import SessionMessageBus
    bus = SessionMessageBus()

    # Create an object that will be a proxy for a particular remote object.
    remote_object = bus.get_proxy(
        "org.freedesktop.DBus",  # The bus name
        "/org/freedesktop/DBus"  # The object path
    )

    # Call the Introspect method of the remote object.
    print(remote_object.Introspect())

## Accessing a remote property 

The following example prints the current hostname.

    from dasbus.connection import SystemMessageBus
    bus = SystemMessageBus()

    proxy = bus.get_proxy(
        "org.freedesktop.hostname1",
        "/org/freedesktop/hostname1"
    )

    print(proxy.Hostname)

## Calling a remote method 

The following example sends a notification to the notification server.

    from dasbus.connection import SessionMessageBus
    bus = SessionMessageBus()

    proxy = bus.get_proxy(
        "org.freedesktop.Notifications",
        "/org/freedesktop/Notifications"
    )

    id = proxy.Notify(
        "", 0, "face-smile", "My notification",
        "Hello World!", [], {}, 0
    )

    print("The notification {} was sent.".format(id))

# dbus-next

For more information see [dbus-next\'s documentation](https://python-dbus-next.readthedocs.io/).

## The client interface 

To use a service on the bus, the library constructs a proxy object you can use to call methods, get and set properties, and listen to signals.

This example connects to a media player and controls it with the MPRIS DBus interface using python\'s asyncio backend.

:::: 
::: 
``` 
   1 from dbus_next.aio import MessageBus
   2 
   3 import asyncio
   4 
   5 loop = asyncio.get_event_loop()
   6 
   7 
   8 async def main():
   9     bus = await MessageBus().connect()
  10     # the introspection xml would normally be included in your project, but
  11     # this is convenient for development
  12     introspection = await bus.introspect('org.mpris.MediaPlayer2.vlc', '/org/mpris/MediaPlayer2')
  13 
  14     obj = bus.get_proxy_object('org.mpris.MediaPlayer2.vlc', '/org/mpris/MediaPlayer2', introspection)
  15     player = obj.get_interface('org.mpris.MediaPlayer2.Player')
  16     properties = obj.get_interface('org.freedesktop.DBus.Properties')
  17 
  18     # call methods on the interface (this causes the media player to play)
  19     await player.call_play()
  20 
  21     volume = await player.get_volume()
  22     print(f'current volume: {volume}, setting to 0.5')
  23 
  24     await player.set_volume(0.5)
  25 
  26     # listen to signals
  27     def on_properties_changed(interface_name, changed_properties, invalidated_properties):
  28         for changed, variant in changed_properties.items():
  29             print(f'property changed: {changed} - {variant.value}')
  30 
  31     properties.on_properties_changed(on_properties_changed)
  32 
  33     await loop.create_future()
  34 
  35 loop.run_until_complete(main())
```
:::
::::

## The service interface 

To define a service on the bus, use the [ServiceInterface](./ServiceInterface.html) class and decorate class methods to specify DBus methods, properties, and signals with their type signatures.

:::: 
::: 
``` 
   1 from dbus_next.service import ServiceInterface, method, dbus_property, signal, Variant
   2 from dbus_next.aio MessageBus
   3 
   4 import asyncio
   5 
   6 class ExampleInterface(ServiceInterface):
   7     def __init__(self, name):
   8         super().__init__(name)
   9         self._string_prop = 'kevin'
  10 
  11     @method()
  12     def Echo(self, what: 's') -> 's':
  13         return what
  14 
  15     @method()
  16     def GetVariantDict() -> 'a{sv}':
  17         return {
  18             'foo': Variant('s', 'bar'),
  19             'bat': Variant('x', -55),
  20             'a_list': Variant('as', ['hello', 'world'])
  21         }
  22 
  23     @dbus_property()
  24     def string_prop(self) -> 's':
  25         return self._string_prop
  26 
  27     @string_prop.setter
  28     def string_prop_setter(self, val: 's'):
  29         self._string_prop = val
  30 
  31     @signal()
  32     def signal_simple(self) -> 's':
  33         return 'hello'
  34 
  35 async def main():
  36     bus = await MessageBus().connect()
  37     interface = ExampleInterface('test.interface')
  38     bus.export('/test/path', interface)
  39     # now that we are ready to handle requests, we can request name from D-Bus
  40     await bus.request_name('test.name')
  41     # wait indefinitely
  42     await asyncio.get_event_loop().create_future()
  43 
  44 asyncio.get_event_loop().run_until_complete(main())
```
:::
::::

# python-sdbus

See [python-sdbus documentation for API reference and quickstart guides](https://python-sdbus.readthedocs.io/en/latest/index.html).

Python-sdbus has a unified client and server classes where one class can be used both as a client proxy and as a server.

## Interface class definition 

:::: 
::: 
``` 
   1 from sdbus import (DbusInterfaceCommonAsync, dbus_method_async,
   2                    dbus_property_async, dbus_signal_async)
   3 
   4 # This is file only contains interface definition for easy import
   5 # in server and client files
   6 
   7 class ExampleInterface(
   8     DbusInterfaceCommonAsync,
   9     interface_name='org.example.interface'
  10 ):
  11     @dbus_method_async(
  12         input_signature='s',
  13         result_signature='s',
  14     )
  15     async def upper(self, string: str) -> str:
  16         return string.upper()
  17 
  18     @dbus_property_async(
  19         property_signature='s',
  20     )
  21     def hello_world(self) -> str:
  22         return 'Hello, World!'
  23 
  24     @dbus_signal_async(
  25         signal_signature='i'
  26     )
  27     def clock(self) -> int:
  28         raise NotImplementedError
```
:::
::::

## Server 

:::: 
::: 
``` 
   1 from asyncio import new_event_loop, sleep
   2 from random import randint
   3 from time import time
   4 
   5 from example_interface import ExampleInterface
   6 
   7 from sdbus import request_default_bus_name_async
   8 
   9 loop = new_event_loop()
  10 
  11 export_object = ExampleInterface()
  12 
  13 
  14 async def clock() -> None:
  15     """
  16     This coroutine will sleep a random time and emit
  17     a signal with current clock
  18     """
  19     while True:
  20         await sleep(randint(2, 7))  # Sleep a random time
  21         current_time = int(time())  # The interface we defined uses integers
  22         export_object.clock.emit(current_time)
  23 
  24 
  25 async def startup() -> None:
  26     """Perform async startup actions"""
  27     # Acquire a known name on the bus
  28     # Clients will use that name to address this server
  29     await request_default_bus_name_async('org.example.test')
  30     # Export the object to D-Bus
  31     export_object.export_to_dbus('/')
  32 
  33 
  34 loop.run_until_complete(startup())
  35 task_clock = loop.create_task(clock())
  36 loop.run_forever()
```
:::
::::

## Client 

:::: 
::: 
``` 
   1 from asyncio import new_event_loop
   2 
   3 from example_interface import ExampleInterface
   4 
   5 # Create a new proxied object
   6 example_object = ExampleInterface.new_proxy('org.example.test', '/')
   7 
   8 
   9 async def print_clock() -> None:
  10     # Use async for loop to print clock signals we receive
  11     async for x in example_object.clock:
  12         print('Got clock: ', x)
  13 
  14 
  15 async def call_upper() -> None:
  16     s = 'test string'
  17     s_after = await example_object.upper(s)
  18 
  19     print('Initial string: ', s)
  20     print('After call: ', s_after)
  21 
  22 
  23 async def get_hello_world() -> None:
  24     print('Remote property: ', await example_object.hello_world)
  25 
  26 loop = new_event_loop()
  27 
  28 # Always bind your tasks to a variable
  29 task_upper = loop.create_task(call_upper())
  30 task_clock = loop.create_task(print_clock())
  31 task_hello_world = loop.create_task(get_hello_world())
  32 
  33 loop.run_forever()
```
:::
::::
