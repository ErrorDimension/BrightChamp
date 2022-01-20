string = input()
length = len(string)

for i in range(length):
    print(string[length - i - 1], end='')
