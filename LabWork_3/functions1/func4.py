a = list(map(int, input().split()))

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

filter_prime(a)


            

