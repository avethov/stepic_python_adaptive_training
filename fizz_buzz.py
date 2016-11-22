numbers = input().split()

for number in range(int(numbers[0]), int(numbers[1]) + 1):
    if not int(number) % 15:
        print('FizzBuzz')
    elif not int(number) % 3:
        print('Fizz')
    elif not int(number) % 5:
        print('Buzz')
    else:
        print(number)
