a_list = list()

a = input()

while a != '0':
    a_list.append(a)
    a = input()

textfile = open("a_file.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()