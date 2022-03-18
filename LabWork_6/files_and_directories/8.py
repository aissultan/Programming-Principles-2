import os
filePath = "C:\\Users\\юзер\\Desktop\\PP2\\LabWork_6\\files_and_directories\\example3.txt"
# As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")
