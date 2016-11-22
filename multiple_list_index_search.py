lst = input()
num = int(input())
out = ''

for index, number in enumerate(lst.split()):
    if int(number) == num:
        out += str(index) + ' '
if out == '':
    print(None)
else:
    print(out)

