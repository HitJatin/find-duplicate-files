import os
import filecmp
files = os.listdir("./test")
pathOfFolder = "path of test folder"
print(files)
# filesPath = {}
# for file in files:
#     if file != file_name:
#         if filecmp.cmp(file_name, file):
#             os.remove(file)
#             print('file has deleted - ', file)
#HashMap - What it is and how it's implemented in python (Remember not to import any library)
#How to find files in a path
# Expected Outcome
# test1.java - ["/"]
# test2.java - ["/", "/practice/"]
# test3.java - ["/", "/practice/"]
# test4.java - ["/"]