a = input()

def isPalindrome(a):
    b = a[::-1]
    if a == b:
        print("Palindrome")
    else:
        print("No")

isPalindrome(a)