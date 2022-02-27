def my_gen(n):
    while n >= 0:
        yield n
        n -= 1

for i in my_gen(int(input())):
    print(i, end = " ")

