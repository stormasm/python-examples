## https://www.geeksforgeeks.org/python-os-mkdir-method/

import os


def mkdir_ifnothere(parent_dir, dirname):

    # check to see that parent_dir exists
    # and if does not print problem and exit

    mybool = os.path.isdir(parent_dir)

    if not mybool:
        print("mkdir_ifnothere: parent directory does not exist exiting process")
        exit()

    # Path
    path = os.path.join(parent_dir, dirname)
    mybool = os.path.isdir(path)

    # check to see if dirname exists
    # and if it does then do not create a new directory

    if not mybool:
        os.mkdir(path)


if __name__ == "__main__":
    path = os.environ["BMTOP"]
    path = path + "/zzz/rick/"
    mkdir_ifnothere(path, "lives")
    print("done")
