def gensquares(N):
    for i in range(N + 1):
        yield i ** 2

for x in gensquares(int(input())):
    print(x)