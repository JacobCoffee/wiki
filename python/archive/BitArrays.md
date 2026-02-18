# BitArrays

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Bit arrays, bitstrings, bit vectors, bit fields.

Whatever they are called, these useful objects are often the most compact way to store data. If you can depict your data as boolean values, and can correlate each value with a unique integer, a bit array is a natural choice.

Sets of positive integers are straightforward. The set containing 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 (the prime numbers less than 32) can be represented in 4 bytes by:

:::: 
::: 
``` 
   1 # bit 31                          bit 0
   2 #      |                              |
   3 #      10100000100010100010100010101100  =  0xA08A28AC
```
:::
::::

The entire set of signed bytes can be represented in 256 bits, where **bit n** corresponds to the number **n - 128**. The set of all integers can be mapped to the positive integers:

:::: 
::: 
``` 
   1 for n in range(17):
   2     if (n & 1):                   # if n is odd, n
   3         i = -((n + 1) >> 1)       # represents a negative number
   4     else:
   5         i = (n >> 1)
   6     print(i, end = ' ')
   7 
   8 # result: 0 -1 1 -2 2 -3 3 -4 4 -5 5 -6 6 -7 7 -8 8
```
:::
::::

Increasingly sophisticated modules are available for generating and using bit arrays (see bit\* in the Python package index) but it isn\'t hard to set up and use a simple bit array. The following demonstration calculates the number of 32-bit integers needed for all the data bits requested and builds an array initialized to all 0\'s or all 1\'s. The program reports the number of \"excess\" bits if the number requested was not an exact multiple of 32.

:::: 
::: 
``` 
   1 # A bit array demo - written for Python 3.0
   2 import array
   3 def makeBitArray(bitSize, fill = 0):
   4     intSize = bitSize >> 5                   # number of 32 bit integers
   5     if (bitSize & 31):                      # if bitSize != (32 * n) add
   6         intSize += 1                        #    a record for stragglers
   7     if fill == 1:
   8         fill = 4294967295                                 # all bits set
   9     else:
  10         fill = 0                                      # all bits cleared
  11 
  12     bitArray = array.array('I')          # 'I' = unsigned 32-bit integer
  13 
  14     bitArray.extend((fill,) * intSize)
  15 
  16     return(bitArray)
  17 
  18 # testBit() returns a nonzero result, 2**offset, if the bit at 'bit_num' is set to 1.
  19 def testBit(array_name, bit_num):
  20     record = bit_num >> 5
  21     offset = bit_num & 31
  22     mask = 1 << offset
  23     return(array_name[record] & mask)
  24 
  25 # setBit() returns an integer with the bit at 'bit_num' set to 1.
  26 def setBit(array_name, bit_num):
  27     record = bit_num >> 5
  28     offset = bit_num & 31
  29     mask = 1 << offset
  30     array_name[record] |= mask
  31     return(array_name[record])
  32 
  33 # clearBit() returns an integer with the bit at 'bit_num' cleared.
  34 def clearBit(array_name, bit_num):
  35     record = bit_num >> 5
  36     offset = bit_num & 31
  37     mask = ~(1 << offset)
  38     array_name[record] &= mask
  39     return(array_name[record])
  40 
  41 # toggleBit() returns an integer with the bit at 'bit_num' inverted, 0 -> 1 and 1 -> 0.
  42 def toggleBit(array_name, bit_num):
  43     record = bit_num >> 5
  44     offset = bit_num & 31
  45     mask = 1 << offset
  46     array_name[record] ^= mask
  47     return(array_name[record])
  48 #* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
  49 bits = 65536                     # change these numbers to 
  50 
  51 ini = 1                          # test the function
  52 
  53 myArray = makeBitArray(bits, ini)
  54 
  55 # array info: input bits; final length; excess bits; fill pattern
  56 print(bits, len(myArray), (len(myArray) * 32) - bits, bin(myArray[0]))
```
:::
::::

For a more concrete example, the following code uses the Sieve of Eratosthenes (for an explanation, see Wikipedia) to find all of the primes less than 65536 (2 to the 16th power) and leaves them in a bit array. This is not the place to go into all the details of how the Sieve works, so it is left in an informal form. To run the Sieve, change the main body of the program (everything after the function definitions) to:

:::: 
::: 
``` 
   1 # Python 3.0
   2 bits = 65536                             # upper limit on primes
   3 ini = 1
   4 myArray = makeBitArray(bits, ini)
   5 #* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
   6 # 0 and 1 are not prime, and not included in the Sieve of Eratosthenes:
   7 bit = 0
   8 clearBit(myArray, bit)
   9 bit = 1
  10 clearBit(myArray, bit)
  11 
  12 for index in range(256):            # range is to "square root" of limit
  13     test = testBit(myArray, index)
  14 
  15     if test:
  16         zeroBit = index * index     # prime squared is lowest multiple left
  17 
  18         while zeroBit < 65536:
  19             clearBit(myArray, zeroBit)
  20             zeroBit += index
  21 
  22 for index in range(65536):
  23     test = testBit(myArray, index)
  24     if test:
  25         print(index)
```
:::
::::

You might want to redirect output to a file, especially if you increase the limits.

The above demo does not use either setBit() or toggleBit(), and storage of lists of integers only scratches the surface of what can be done with bits as data. There is a huge amount of work out there, dating back to the days when computers had memories and storage measured in bytes, on this topic.

See also:

[BitManipulation](BitManipulation)

[BitwiseOperators](BitwiseOperators)
