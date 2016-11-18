def plus(a, b):
    return int(a) + int(b)


def minus(a, b):
    return int(a) - int(b)


def multiply(a, b):
    return int(a) * int(b)


def divide(a, b):
    try:
        return int(a) // int(b)
    except ZeroDivisionError:
        return None

a, operator, b = input().split(' ')

if operator == 'plus':
    print(plus(a, b))
elif operator == 'minus':
    print(minus(a, b))
elif operator == 'multiply':
    print(multiply(a, b))
elif operator == 'divide':
    print(divide(a, b))
else:
    print("Operator doesn't supported")


