def EvenGenerator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

values = []
for i in EvenGenerator(int(input())):
    values.append(i)

# print(",".join(values))

for i in range(len(values)):
    if i < len(values) - 1:
        print(i, end = ", ")
    else:
        print(i)
