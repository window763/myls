import argparse

parser =argparse.ArgumentParser(
                    prog='ArgTest',
                    description='Tests arg parse understanding',
                    epilog='Thats all folks')

parser.add_argument('filename', default='.')
parser.add_argument('-F','--filetype', 
                    help="Adds a character at the end certain names to indicate whether the file is a directory (/) or an executable file (*).",
                    action='store_true')
parser.add_argument('-l', '--longform',
                    help="Prints the last modified date, file size and file name for each file in the specified directory",
                    action='store_true')

args = parser.parse_args()
print (args) 
