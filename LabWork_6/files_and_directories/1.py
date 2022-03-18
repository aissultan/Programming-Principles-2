import os

path = os.getcwd()
# path = "C:\\Users\\юзер\\Desktop\\PP2\\LabWork_6"

print("Only directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Only files:")
print([f for f in os.listdir(path) if not os.path.isdir(os.path.join(path, f))])
print("All directories and files :")
print([x for x in os.listdir(path)])

# print("Only directories:")
# for d in os.listdir(path):
#     if os.path.isdir(os.path.join(path, d)):
#         print(d)

# print("\nOnly files: ")
# for f in os.listdir(path):
#     if not os.path.isdir(os.path.join(path, f)):
#         print(f)

# print("\nAll directories and files:")
# for x in os.listdir(path):
#     print(x)