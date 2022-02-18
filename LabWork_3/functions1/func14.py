from allfunc import *

s = input()

if s == "reverse":
    reverse(input())
if s == "Ounces":
    print(toOunces(int(input())))
if s == "Celsius":
    print(toCelsius(int(input())))
if s == "primes":
    filter_prime(list(map(int, input().split())))
if s == "33":
    has_33(list(map(int, input().split())))