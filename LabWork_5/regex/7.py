import re

def snake_to_camel(text):
    mylist = re.split('_', text)
    result = ""
    for word in mylist:
        result += word[0].upper() + word[1:]
    print(result)

snake_to_camel(input())

# snake case: some_awesome_var
# camel case: someAwesomeVar