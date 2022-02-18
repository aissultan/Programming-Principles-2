import math

r = int(input())

def getVolume(r):
    return (4/3) * math.pi * (r**3)

print(getVolume(r))