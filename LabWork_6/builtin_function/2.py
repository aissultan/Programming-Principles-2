# def string_test(s):
#     cnt_upper, cnt_lower = 0, 0
#     for char in s:
#         if char.isupper():
#             cnt_upper += 1
#         elif char.islower():
#             cnt_lower += 1
#         else:
#             pass
    # print('Original string:', s)
    # print('Number of upper case characters:', cnt_upper)
    # print('Number of lower case characters:', cnt_lower)

def string_test(s):
    cnt_upper, cnt_lower = 0, 0
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            cnt_upper += 1
        elif ord(char) >= 97 and ord(char) <= 122:
            cnt_lower += 1
    print('Original string:', s)
    print('Number of upper case characters:', cnt_upper)
    print('Number of lower case characters:', cnt_lower)

string_test(input())