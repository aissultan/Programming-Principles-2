n, m = map(int, input().split())

def solve(numheads, numlegs):
    # если бы были только куры, тогда ног было бы всего:
    a = numheads * 2
    # но по условию количество ног - m (numlegs), значит, лишние ноги принадлежат кроликам (по две на каждую голову):
    b = numlegs - a
    # выходит, что кроликов:
    rabbits = b / 2
    # на долю кур остается:
    chickens = numheads - rabbits 
    print(int(chickens), int(rabbits))

solve(n, m)