def Is_prime(a):
    if a == 2:
        return True
    if a < 2:
        return False
    for j in range(2, a):
        if a % j == 0:
            return False

    return True

a = list(filter(lambda x: Is_prime(x), list(map(int,input().split()))))

print(*a)