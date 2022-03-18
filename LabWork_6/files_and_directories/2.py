import os

path = "C:\\Users\\юзер\\Desktop\\PP2\\LabWork_6\\files_and_directories"

ret = os.access(path, os.F_OK)
print("F_OK - return value %s"% ret)

ret = os.access(path, os.R_OK)
print("R_OK - return value %s"% ret)

ret = os.access(path, os.W_OK)
print("W_OK - return value %s"% ret)

ret = os.access(path, os.X_OK)
print("X_OK - return value %s"% ret)