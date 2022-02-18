a = input().split()

def uniqueList(a):
    b = []
    for i in a:
        if b.count(i) == 0:
            b.append(i)
    return b

c = uniqueList(a)
for i in c:
    print(i, " ")        
