def rec(number):
    out.append(str(number))
    if number == 1:
        print(' '.join(out))
    elif number % 2:
        rec(number * 3 + 1)
    else:
        rec(number // 2)


number = int(input())
out = list()

rec(number)
