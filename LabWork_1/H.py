s = input()

ch = input()

a, b = s.find(ch), s.rfind(ch)

if(a == b):
    print(a)
else:
    print(a, b)