def toOunces(n):
    return n / 28.3495231

def toCelsius(a):
    return (5/9) * (a - 32)

def filter_prime(a):
    b = []
    for i in a:
        if i == 0 or i == 1:
            ok = False
        elif i == 2:
            ok = True
        else:
            ok = True
            for j in range(2, i):
                if i % j == 0:
                    ok = False
            if(ok == True):
                b.append(i)
                ok = False
        if(ok == True):
            b.append(i)

    for i in b:
        print(i, end = " ")

def reverse(s):
    a = list(s.split())
    print(*a[::-1])
    
def has_33(nums):
    s = ""
    for i in nums:
        s += str(i)
    if (s.find("33") != -1):
        print("True")
    else:
        print("False")