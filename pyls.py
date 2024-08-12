import argparse
import os

'''
parser = argparse.ArgumentParser(
        prog="pyls",
        description="Outputs a list of files in a given directory (or present working directory if no input given)",
        epilog="That's all folks.",
        )

parser.add_argument(
        "directory_name",
        help="Name of directory to list the contents of",
        action="store",
        nargs="?",
        default=".",
        )

parser.add_argument(
        "-l",
        "--long-format",
        help="Outputs list of files + metadata in the following format: Last Modified Date (YYYY-MM-DD HH:MM:SS), Size of Entry, Filename).",
        action="store-true",
        )

parser.add_argument(
        "-F",
        "--filetype",
        help="Adds an extra character to the end of the printed filename that indicates whether a file is a directory (/) or an executable (*).",
        action="store-true",
        )

args = parser.parse_args()

"""
Three arguments are checked for in the input gathering step,
with the flag arguments being stored as bools.
"""
'''

def readFilesinDir (directory):
    """
    Reads files from a given folder input (must be in the pwd unless entire path is given) using the os library
    """
    dir_ls = []

    if (directory == None):
        dir_path = os.getcwd()
    elif (os.path.isdir(directory) or os.path.isfile(directory)):
        dir_path = directory
    else:
        dir_path = os.getcwd() + "/" + directory

    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)

        metadata = os.stat(filepath)

        data = [metadata.st_mtime, metadata.st_size, filename, filepath]
        dir_ls.append(data)

    return dir_ls

def formatData (dir_ls, long_format, filetype):
    if (filetype):
        for i in range (len(dir_ls)):
            if (os.path.isdir(dir_ls[i][3])):
                dir_ls[i][2] = dir_ls[i][2] + "/"
            elif (os.access(dir_ls[i][3], os.X_OK)):
                dir_ls[i][2] = dir_ls[i][2] + "*"

    if (long_format):
        for i in range (len(dir_ls)):
            date = dir_ls[i][0]
            size = dir_ls[i][1]
            file = dir_ls[i][2]

            print (date, f'{size:>10}', "\t", file)
    else:
        for i in range (len(dir_ls)):
            print (dir_ls[i][2])


x = readFilesinDir("/home/window763/COMP350")

print ("key")
print (formatData (x, 1, 1))
print (os.access("/home/window763/COMP350/lstest.exe", os.X_OK))
