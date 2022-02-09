a = int(input())

m = {}

for i in range(a):
    x, y = input().split()
    if y in m:
        m[y] += 1
    else:
        m[y] = 1

b = int(input())

n = {}

for j in range(b):
    q, w, r = input().split()
    r = int(r)
    if w in n:
        n[w] += r
    else:
        n[w] = r

count = 0

for i in m:
    if i in n:
        if(m[i] > n[i]):
            count += m[i] - n[i]
    else:
        count += m[i]

print("Demons left:", count)