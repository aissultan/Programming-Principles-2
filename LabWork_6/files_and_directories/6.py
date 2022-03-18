for i in range(0,26):
    letter = chr(65 + i)
    with open(letter + '.txt', 'w') as file:
        file.writelines(letter)