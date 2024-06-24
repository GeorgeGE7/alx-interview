#!/usr/bin/python3
"""UTF-8 Validation function"""


def validUTF8(data):
    """
    check for valied utf8 
    """
    byts = 0

    b1 = 1 << 7
    b2 = 1 << 6

    for i in data:
        b = 1 << 7
        if byts == 0:
            while b & i:
                byts += 1
                b = b >> 1
            if byts == 0:
                continue
            if byts == 1 or byts > 4:
                return False
        else:
            if not (i & b1 and not (i & b2)):
                return False
        byts -= 1
    return byts == 0
