from os import listdir
from os.path import isfile, join

def printnames(dir):
    for file in sorted(listdir(dir)):
        full_path = join(dir, file)
        if isfile(full_path):
            print(file)
        else:
            printnames(full_path)

printnames("/home/mario/grokking-algorithms/test_folder_main")