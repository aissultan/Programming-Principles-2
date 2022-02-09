num = int(input())

numbers = []

ans = []

while num != 0:
    numbers.append(num)
    num = int(input())

for x in range(int(len(numbers)/2)):
    n = numbers[0] + numbers[-1]
    numbers.pop(0)
    numbers.pop(-1)
    ans.append(n)

if len(numbers) == 1:
    ans.append(numbers[0])

for x in ans:
    print(x , end = " ")