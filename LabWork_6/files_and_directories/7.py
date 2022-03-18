# with open("test.txt") as f:
#     with open("out.txt", "w") as f1:
#         for line in f:
#             f1.write(line)
            
# import module
import shutil

# use copyfile()
shutil.copyfile('test.txt','out.txt')