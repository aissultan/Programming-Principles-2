import collections

a = int(input())

b = {}

i = 0
while i < a:
    m, n = input().split()
    n = int(n)
    if m in b:
        b[m] += n
    else:
        b[m] = n
    i = i + 1

y = collections.OrderedDict(sorted(b.items()))
x = max(b.values())

for i in y:
    if b[i] != x:
        print(i, "has to receive", x - b[i], "tenge")
    else:
        print(i, "is lucky!")