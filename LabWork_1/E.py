a, b = map(int, input().split())

isPrime = True

for i in range(2, a):
    if(a % i == 0):
        isPrime = False
        break

if (a < 500 and isPrime and b % 2 == 0): 
    print("Good job!") 
else: 
    print("Try next time!")