# Asking for Help/remove escape characters

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How To Remove Escape Characters 

system: ubuntu connected to a serial port connected datalogger pls look at this post using \"source txt\"or\"bron txt\" button rigth top for better lay-out

python program

:::: 
::: 
``` 
   1 #! /usr/bin/env python
   2 import serial
   3 import time
   4 ser = serial.Serial('/dev/ttyS0',9600, bytesize=8, timeout=9)
   5 ser.open()              
   6 if ser.isOpen():                                        
   7     ser.write( b'\x1b' )  #this is the binary format for chr(27) esc
   8     #time.sleep(1)
   9     response = ser.read(ser.inWaiting())
  10     data = ser.readlines()
  11 #data = data.split()
  12 f = open('../../../minicom/python.txt', 'a')
  13 s = str(data)
  14 f.write(s)
  15 f.close()
  16 data.Sstrip("\n\r")
  17 print data
  18 ser.close()
  19 print "port closed"
```
:::
::::

sample of the data received

    '10-3-11\t15:28\t23,8\t14,4\t0\r\n', '10-3-11\t15:35\t12,0\t13,5\t8\r\n', '10-3-11\t15:45\t12,0\t14,0\t1\r\n', '10-3-11\t15:46\t12,0\t14,0\t0\r\n', '10-3-11\t15:55\t12,0\t13,5\t11\r\n', '10-3-11\t16:4\t12,0\t13,5\t0\r\n', '10-3-11\t16:5\t23,8\t14,4\t0\r\n', '10-3-11\t16:5\t12,0\t13,5\t2\r\n', '10-3-11\t16:6\t12,0\t13,5\t0\r\n']

data should look like this example

    10-3-11 14:31   21,9    4,2     0
    10-3-11 14:33   11,7    13,5    11
    10-3-11 14:39   11,7    13,5    0
    10-3-11 14:39   24,8    14,4    0
    10-3-11 14:39   8,5     18,9    0
    10-3-11 14:44   11,7    13,5    10
    10-3-11 14:54   12,0    13,0    5
    10-3-11 15:4    12,0    13,5    10
    10-3-11 15:8    12,0    13,5    0
    10-3-11 15:9    23,8    14,4    0
    10-3-11 15:14   12,0    13,5    5
    10-3-11 15:16   12,0    13,5    0
    10-3-11 15:17   23,8    14,4    0
    10-3-11 15:18   11,7    18,9    0

is there anyone with a similar problem fspr

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help]() page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)
