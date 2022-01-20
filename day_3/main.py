size = int(input())
"""
 # 
### mokshee.ashri@brightchamps.com
 # 
"""


def abs(value):
    if (value < 0):
        return value * -1

    return value


def shape(size):
    spaces = int(size / 2)

    for _ in range(size):
        trueSpaces = abs(spaces)
        print(' ' * trueSpaces, '#' * (size - trueSpaces * 2),
              ' ' * trueSpaces)
        spaces -= 1


shape(size)
