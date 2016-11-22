str = input().split()

dic = {}

for word in str:
    if not len(word) in dic:
        dic[len(word)] = 1
    else:
        dic[len(word)] += 1

for key in sorted(dic.keys()):
    print('{0}: {1}'.format(key, dic[key]))
