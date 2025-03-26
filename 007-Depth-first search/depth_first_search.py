from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
    def printnames(dir):
        for file in sorted(listdir(dir)):
            full_path = join(dir, file)
            if isfile(full_path):
                print(file)
            else:
                printnames(full_path)

    printnames("./test_folder_main")

