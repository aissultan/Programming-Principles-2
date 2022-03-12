import re

def camel_to_snake(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()

text = input()
print(camel_to_snake(text))

# camel case: someAwesomeVar
# snake case: some_awesome_var