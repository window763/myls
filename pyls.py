import argparse
import os
from datetime import datetime

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
        action="store_true",
        )

parser.add_argument(
        "-F",
        "--filetype",
        help="Adds an extra character to the end of the printed filename that indicates whether a file is a directory (/) or an executable (*).",
        action="store_true",
        )

args = parser.parse_args()

"""
Three arguments are checked for in the input gathering step using argparse,
with the flag arguments being stored as bools.
long_format = True if -l or --long-format is input
filetype = True if -F or --filetype is input
"""

def readFilesinDir (directory):
    """
    Reads files from a given folder input (must be in the pwd unless entire path is given) using the os library.
    directory = name of directory input whose contents must be listed.
    dir_ls = A list that will have lists containing each file's metadata appended to it.
    """
    dir_ls = []

    """
    The nested if statements check if the given directory is empty.
    If empty, dir_path = Present working directory
    If input is a directory or file, dir_path = the directory input itself
    Else, dir_path = Present working directory with "directory" input appended afterwords
    (This assumes the user has input a directory within the current working directory)
    If no directory is found, an error message displays.
    """
    if (directory == None):
        dir_path = os.getcwd()
    elif (os.path.isdir(directory) or os.path.isfile(directory)):
        dir_path = directory
    else:
        dir_path = os.getcwd() + "/" + directory

    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)

        metadata = os.stat(filepath)

        date = datetime.fromtimestamp(metadata.st_mtime)

        data = [date.strftime("%Y-%m-%d %H:%M:%S"), metadata.st_size, filename, filepath]
        dir_ls.append(data)

    return dir_ls

def formatData (dir_ls, long_format, filetype):
    """
    Formats data based on the directory list input, as well as whether the long-format or filetype flags are True.
    The first if statement checks if filetype is True.
    If True, the function appends the specified special characters to the filenames depending on whether it's a directory or an executable.
    (NOTE: The executable append doesn't seem to be working because os.acces(filepath, os.X_OK) isn't registering actual executable files.
           This still needs to be resolved.)

    The second if statement checks if long_format is True.
    If True, the function simply prints the list elements in a single line to the specified formatting.
    """
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

def main ():
    """
    These variables are used to read the input data and pass them as arguments for the functions.
    """
    directory = readFilesinDir(args.directory_name)
    final_out = formatData (directory, args.long_format, args.filetype)

    """
    Outputs the list of elements in the specified directory.
    """
    print (final_out)

if __name__ == "__main__":
    main()
