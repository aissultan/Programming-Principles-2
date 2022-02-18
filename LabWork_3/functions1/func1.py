def toOunces(n):
    return n / 28.3495231

a, b = input().split()

b = int(b)

print(a, toOunces(b))

