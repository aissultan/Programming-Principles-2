a, b = map(int, input().split())

def squares(x, y):
    for i in range(x, y + 1):
        yield i ** 2

for i in squares(a, b):
    print(i)
