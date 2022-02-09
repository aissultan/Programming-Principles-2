a = int(input())

b = []
c = []

for i in range(a):
    oper = input().split(" ")
    if(oper[0] == "1"):
        b.append(oper[1])
    else:
        c.append(b[0])
        b.pop(0)

for i in c:
    print(i, end = " ")
    