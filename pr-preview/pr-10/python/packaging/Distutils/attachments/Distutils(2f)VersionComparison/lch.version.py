import itertools

fields = []
accumulator = []
fieldType = None


def endField():
    global accumulator
    global fields
    global fieldType
    stringMap = { "alpha" : -30, "beta" : -20, "rc" : -10, "final" : None }
    if accumulator:
        s = "".join(accumulator)
        if s in stringMap:
            value = stringMap[s]
            if value is not None:
                fields.append(value)
        elif fieldType == 'ascii':
            fields.extend([ord(c.upper()) for c in accumulator])
        else:
            assert fieldType == 'digits'
            while len(accumulator) > 1 and accumulator[0] == '0':
                accumulator.pop(0)
            fields.append(int(s))
    accumulator = []
    fieldType = None



def split_version(s):
    """Splits a version string into a tuple of integers."""

    global accumulator
    global fields
    global fieldType

    fields = []

    for c in s:
        if c.isdigit():
            if fieldType == 'ascii':
                endField()
            fieldType = 'digits'
            accumulator.append(c)
            continue
        if c.isalpha():
            if fieldType == 'digits':
                endField()
            fieldType = 'ascii'
            accumulator.append(c)
            continue
        endField()
    endField()
    while fields and (fields[-1] == 0):
        fields.pop()
    return tuple(fields)

def _split_nonfinal(v):
    for i, field in enumerate(v):
        if field < 0:
            return v[:i], v[i:]
    return v, ()

def compare_version_tuples(a, b):
    """Compares two version tuples.

    Returns 0 if they are equivalent,
    a negative number if the first version is less than the second version,
    and a positive number if the first version is greater than the second version.
    """
    a, aBeta = _split_nonfinal(a)
    b, bBeta = _split_nonfinal(b)
    for fa, fb in itertools.chain(itertools.izip_longest(a, b, fillvalue=0), itertools.izip_longest(aBeta, bBeta, fillvalue=0)):
        if fa == fb:
            continue
        return 1 if (fa > fb) else -1
    return 0

def is_final(a):
    """Returns true if this is a 'final' version.
    Returns false if it is not a 'final' version (an alpha, beta, rc)."""
    for field in a:
        if field < 0:
            return False
    return True

if __name__ == "__main__":
    for s, version in (
    ("1.2", (1, 2)),
    ("1.2.0", (1, 2)),
    ("1.0alpha1", (1, 0, -30, 1)),
    ("1.0 alpha 1", (1, 0, -30, 1)),
    ("1-0pa3", (1, 0, ord('p'.upper()), ord('a'.upper()), 3)),
    ("1.003", (1, 3)),
    ("1.3", (1, 3)),
    ):
        assert split_version(s) == version
    
    for s in """
    1.0 1.0            0
    1.0 1              0
    1.0 1.0.0.0        0
    1.0 1.2           -1
    1.2.0 1            1
    1.0alpha1 1.0     -1
    1.0alpha 1.0beta  -1
    1-0p3 1-0p4       -1
    1.003 1.4         -1
    1.0.0.0 1alpha3    1
    """.strip().split("\n"):
        v1, v2, expected = s.split()[:3]
        expected = int(expected)
        result = compare_version_tuples(split_version(v1), split_version(v2))
        assert result == expected

