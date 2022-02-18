a = list(map(int, input().split()))

def histogram(a):
    for i in a:
        print("*" * i)
    
histogram(a)
