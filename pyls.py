import argparse

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
