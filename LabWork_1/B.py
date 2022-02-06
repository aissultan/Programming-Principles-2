a = input()

result = 0

def isTasty(s):
    if(s > 300):
        print("It is tasty!")
    else:
        print("Oh, no!")
    
for i in range(len(a)):
    result = result + ord(a[i])

isTasty(result)