import re 

def text_match(text):
    patterns = '^ab*?$' 
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

text = input()
print(text_match(text))