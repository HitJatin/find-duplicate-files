import os
filesPath = {}
def addFilesInHashMap(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(path + "/" + file):
            addFilesInHashMap(path + "/" + file)
        else:
            if filesPath.get(file) == None:
                filesPath[file] = []
            filesPath[file].append(path)
addFilesInHashMap("./test")
print(filesPath)