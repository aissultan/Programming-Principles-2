a = int(input())

passwords = []

for i in range(a):
    b = input()
    if b.upper() != b and b.lower() != b and b.isalpha() == False:
        if b not in passwords:
            passwords.append(b)

print(len(passwords))
passwords.sort()

for i in passwords:
    print(i)