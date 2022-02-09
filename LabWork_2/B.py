a = int(input())

mylist = list(map(int, input().split()))

mylist.sort()

print(mylist[-1] * mylist[-2])



