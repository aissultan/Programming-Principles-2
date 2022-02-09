a = input()

mylist = a.split()
lst = []

for i in mylist:
    s = ""
    for j in i: 
        if((j >= 'a' and j <= 'z') or (j >= 'A' and j <= 'Z')):
            s += j
    lst.append(s)

x = list(set(lst))
x.sort()
print(len(x))

for i in x:
    print(i)
