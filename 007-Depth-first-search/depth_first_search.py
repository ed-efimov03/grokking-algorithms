from os import listdir
from os.path import isfile, join

def printnames(dir):
    for file in sorted(listdir(dir)):
        full_path = join(dir, file)
        if isfile(full_path):
            print(file)
        else:
            printnames(full_path)

if __name__ == "__main__":
    printnames("./007-Depth-first-search/test_folder_main")