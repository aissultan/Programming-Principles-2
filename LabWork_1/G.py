binar = input()

a = len(binar) - 1 

res = 0

def toDec(binar, cnt):
    global res
    if cnt == a + 1:
        return res

    res += int(int(binar[cnt]) * (2 **(a - cnt)))
    return toDec(binar, cnt + 1)

toDec(binar, 0)
print(res)

# without recursion 
# _________________________________________
# binarynum = input()

# decimalnum = 0

# for digit in binarynum:
#     decimalnum = decimalnum*2 + int(digit)
# print(decimalnum)
# _________________________________________
# print(int(binarynum, 2)) - another method
