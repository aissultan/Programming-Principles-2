# import math 

# number = int(input())
# time = int(input())

# print(f'Square root of {number} after {time} miliseconds is', math.sqrt(number))

import time, math
def delay(number, milliseconds):
    seconds = milliseconds/1000
    answer=math.sqrt(number)
    time.sleep(seconds)
    print('Square root of '+ str(number) + ' after '+str(milliseconds) + ' milliseconds is '+str(answer))
delay(25100,2123)
delay(25,5000)