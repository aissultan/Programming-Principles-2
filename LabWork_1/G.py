binarynum = input()

decimalnum = 0

for digit in binarynum:
    decimalnum = decimalnum*2 + int(digit)
print(decimalnum)

# print(int(binarynum, 2)) - another method