a = input() 
if a == ''.join(reversed(a)): 
    print("The string is a palindrome.") 
else: 
    print("The string is not a palindrome.")