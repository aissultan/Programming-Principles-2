import re

def capital_words_spaces(text):
  mylist = re.findall('[A-Z][^A-Z]*', text)
  result = ' '.join(mylist)
  return result

print(capital_words_spaces(input()))