s = input()

word = ""
result = ""

def getLen(t):
    cnt = 0
    for i in t:
        cnt = cnt + 1
    return cnt

for i in range(len(s)):
    if(s[i] != " "):
        word = word + s[i]

    if(s[i] == " "):
        if(getLen(word) >= 3):
            result = result + word + " "
        word = ""

    if(i == len(s) - 1):
        if(getLen(word) >= 3):
            result = result + word

print(result)