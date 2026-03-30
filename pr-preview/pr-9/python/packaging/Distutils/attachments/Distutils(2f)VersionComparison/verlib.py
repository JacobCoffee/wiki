
r"""
"Rational" version definition and parsing for DistutilsVersionFight
discussion at PyCon 2009.

>>> from verlib import RationalVersion as V
>>> v = V('1.2.3')
>>> str(v)
'1.2.3'

>>> v = V('1.2')
>>> str(v)
'1.2'

>>> v = V('1.2.3a4')
>>> str(v)
'1.2.3a4'

>>> v = V('1.2c4')
>>> str(v)
'1.2c4'

>>> v = V('1.2.3.4')
>>> str(v)
'1.2.3.4'

>>> v = V('1.2.3.4.0b3')
>>> str(v)
'1.2.3.4b3'

>>> V('1.2.0.0.0') == V('1.2')
True

# Irrational version strings

>>> v = V('1')
Traceback (most recent call last):
  ...
IrrationalVersionError: 1
>>> v = V('1.2a')
Traceback (most recent call last):
  ...
IrrationalVersionError: 1.2a
>>> v = V('1.2.3b')
Traceback (most recent call last):
  ...
IrrationalVersionError: 1.2.3b
>>> v = V('1.02')
Traceback (most recent call last):
  ...
IrrationalVersionError: cannot have leading zero in version number segment: '02' in '1.02'
>>> v = V('1.2a03')
Traceback (most recent call last):
  ...
IrrationalVersionError: cannot have leading zero in version number segment: '03' in '1.2a03'
>>> v = V('1.2a3.04')
Traceback (most recent call last):
  ...
IrrationalVersionError: cannot have leading zero in version number segment: '04' in '1.2a3.04'

# Comparison

>>> V('1.2.0') == '1.2'
Traceback (most recent call last):
  ...
TypeError: cannot compare RationalVersion and str

>>> V('1.2.0') == V('1.2')
True
>>> V('1.2.0') == V('1.2.3')
False
>>> V('1.2.0') < V('1.2.3')
True
>>> (V('1.0') > V('1.0b2'))
True
>>> (V('1.0') > V('1.0c2') > V('1.0c1') > V('1.0b2') > V('1.0b1') 
...  > V('1.0a2') > V('1.0a1'))
True
>>> (V('1.0.0') > V('1.0.0c2') > V('1.0.0c1') > V('1.0.0b2') > V('1.0.0b1') 
...  > V('1.0.0a2') > V('1.0.0a1'))
True

>>> (V('1.0a1')
...  < V('1.0a2.dev456')
...  < V('1.0a2')
...  < V('1.0a2.1.dev456')  # e.g. need to do a quick post release on 1.0a2
...  < V('1.0a2.1')
...  < V('1.0b1.dev456')
...  < V('1.0b2')
...  < V('1.0c1.dev456')
...  < V('1.0c1')
...  < V('1.0.dev456')
...  < V('1.0')
...  < V('1.0.post456'))
True

"""

import sys
import re
from pprint import pprint


class IrrationalVersionError(Exception):
    """This is an irrational version."""


class RationalVersion(object):
    """A rational version.
    
    Good:
        1.2         # equivalent to "1.2.0"
        1.2.0
        1.2a1
        1.2.3a2
        1.2.3b1
        1.2.3c1
        1.2.3.4
        TODO: fill this out
   
    Bad:
        1           # mininum two numbers
        1.2a        # release level must have a release serial
        1.2.3b
    """
    def __init__(self, s):
        self._parse(s)
    
    _version_re = re.compile(r'''
        ^
        (\d+\.\d+)              # minimum 'N.N'
        ((?:\.\d+)*)            # any number of extra '.N' segments
        (?:
          ([abc])               # 'a'=alpha, 'b'=beta, 'c'=release candidate
          (\d+(?:\.\d+)*)
        )?
        (\.(dev|post)(\d+))?    # pre- (aka development) and post-release tag
        $
        ''', re.VERBOSE)
    # A marker used in the second and third parts of the `info` tuple, for
    # versions that don't have those segments, to sort properly. A example
    # of versions in sort order ('highest' last):
    #   1.0b1           ((1,0), ('b',1), ('f',))
    #   1.0.dev345      ((1,0), ('f',),  ('dev', 345))
    #   1.0             ((1,0), ('f',),  ('f',))
    #   1.0.post345     ((1,0), ('f',),  ('post', 345))
    #                           ^        ^
    #   'f' < 'b' -------------/         |
    #                                    |
    #   'dev' < 'f' < 'post' -----------/
    # Other letters would do, bug 'f' for 'final' is kind of nice.
    _final_marker = ('f',)

    def _parse(self, s):
        match = self._version_re.search(s)
        if not match:
            raise IrrationalVersionError(s)
        groups = match.groups()
        parts = []
        block = self._parse_numdots(groups[0], s, False, 2)
        if groups[1]:
            block += self._parse_numdots(groups[1][1:], s)
        parts.append(tuple(block))
        if groups[2]:
            block = [groups[2]]
            block += self._parse_numdots(groups[3], s, pad_zeros_length=1)
            parts.append(tuple(block))
        else:
            parts.append(self._final_marker)
        if groups[4]:
            parts.append((groups[5], int(groups[6])))
        else:
            parts.append(self._final_marker)
        self.info = tuple(parts)
        #print "_parse(%r) -> %r" % (s, self.info)
    
    def _parse_numdots(self, s, full_ver_str, drop_trailing_zeros=True,
            pad_zeros_length=0):
        """Parse 'N.N.N' sequences, return a list of ints.
        
        @param s {str} 'N.N.N..." sequence to be parsed
        @param full_ver_str {str} The full version string from which this
            comes. Used for error strings.
        @param drop_trailing_zeros {bool} Whether to drop trailing zeros
            from the returned list. Default True.
        @param pad_zeros_length {int} The length to which to pad the
            returned list with zeros, if necessary. Default 0.
        """
        nums = []
        for n in s.split("."):
            if len(n) > 1 and n[0] == '0':
                raise IrrationalVersionError("cannot have leading zero in "
                    "version number segment: '%s' in %r" % (n, full_ver_str))
            nums.append(int(n))
        if drop_trailing_zeros:
            while nums and nums[-1] == 0:
                nums.pop()
        while len(nums) < pad_zeros_length:
            nums.append(0)
        return nums
    
    def __cmp__(self, other):
        if not isinstance(other, RationalVersion):
            raise TypeError("cannot compare %s and %s"
                % (type(self).__name__, type(other).__name__))
        return cmp(self.info, other.info)
    
    def __str__(self):
        main, prerel, devpost = self.info
        s = '.'.join(str(v) for v in main if v)
        if prerel is not self._final_marker:
            s += prerel[0]
            s += '.'.join(str(v) for v in prerel[1:] if v)
        if devpost is not self._final_marker:
            s += '.' + ''.join(str(v) for v in prerel[1:] if v)
        return s
    
    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self)

    
#---- mainline and test

def _test():
    import doctest
    doctest.testmod()

def _play():
    V = RationalVersion
    print V('1.0.dev123') < V('1.0.dev456') < V('1.0') < V('1.0.post456') < V('1.0.post789')

if __name__ == "__main__":
    #_play()
    _test()
