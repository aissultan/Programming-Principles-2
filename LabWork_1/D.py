a = int(input())

ch = input()

if(ch == "b"):
    print(a * 1024)
else:
    b = int(input())
    a = a / 1024
    res = round(a, b)
    print(res)