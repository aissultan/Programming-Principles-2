import re

for i in re.findall(r'[A-Z][^A-Z]*', input()):
    print(i, end = " ")
