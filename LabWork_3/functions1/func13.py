from random import randint

a = randint(1, 20)

print("Hello! WHat is your name?") 

name = input()

print(" ")

print("Well, " + name + ", I am thinking of a number between 1 and 20." + '\n' + "Take a guess.")

ok = True
cnt = 1
while ok == True:
    b = int(input())
    if b == a:
        print("Good job, " + name + "! You duessed my number in " + str(cnt) + " guesses!")
        ok = False
    else:
        print('\n' + "Your guess is too low." + '\n' + "Take a guess.")
    cnt += 1



