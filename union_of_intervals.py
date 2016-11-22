number = int(input())

if (number == -10) or \
        ((number > -5) and (number <= 3)) or \
        ((number > 8) and (number < 12)) or \
        (number >= 16):
    print(True)
else:
    print(False)
