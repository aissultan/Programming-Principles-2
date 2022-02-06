a = int(input())

for i in range(a):
    s = input()
    b = s.find("@gmail.com")
    if(b != -1):
        print(s[0: b])