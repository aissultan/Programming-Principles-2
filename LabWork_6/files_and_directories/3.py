import os
path = input()
existance = os.access(path, os.F_OK)
print("Existance:", existance)

if existance: 
    print("File Name:", os.path.basename(path))
    print("Dir Name:", os.path.dirname(path))
