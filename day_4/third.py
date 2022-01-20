string = input()
length = len(string)


def isInRange(int_: str, lowerRange, upperRange) -> int:
    return ord(int_) >= lowerRange and ord(int_) <= upperRange


def specialCharacters(numberCharacters, upperCaseCharacters,
                      lowerCaseCharacters, length) -> int:
    return length - numberCharacters - upperCaseCharacters - lowerCaseCharacters


def numberCharacters(string: str) -> int:
    ans = 0

    for i in range(length):
        intChar = string[i]

        if isInRange(intChar, 48, 57):
            ans += 1

    return ans


def upperCaseCharacters(string: str) -> int:
    ans = 0

    for i in range(length):
        intChar = string[i]

        if isInRange(intChar, 65, 90):
            ans += 1

    return ans


def lowerCaseCharacters(string: str) -> int:
    ans = 0

    for i in range(length):
        intChar = string[i]

        if isInRange(intChar, 97, 122):
            ans += 1

    return ans


numbers = numberCharacters(string)
lower = lowerCaseCharacters(string)
upper = upperCaseCharacters(string)
special = specialCharacters(numbers, lower, upper, length)

print('numbers:', numbers)
print('lower:', lower)
print('upper:', upper)
print('special:', special)
