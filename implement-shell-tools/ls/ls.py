import os
import argparse

parser = argparse.ArgumentParser(
    prog="ls",
    description="list directory contents",
)

parser.add_argument("-1",dest="one",action='store_true', help="list one file per line")
parser.add_argument("-a", action='store_true', help="Used to list all files, including hidden files, in the current directory")
parser.add_argument("path", nargs="?", default=".", help="The path to search")

args = parser.parse_args()

def arguments_proceeding(files):
    data_to_proceed = files

    if args.a:
        data_to_proceed = [f for f in files]
        data_to_proceed.sort()
        data_to_proceed.insert(0, "..")
        data_to_proceed.insert(0, ".")
    else:
        data_to_proceed = [f for f in files if not f.startswith('.')]
    data_to_proceed.sort(key=str.lower)
    if args.one:
        output = [f for f in data_to_proceed]
        for f in output:
            print(f)
    else: 
        print("         ".join(data_to_proceed))
        

def path_proceeding(path_argument):
    if os.path.isfile(path_argument):
        print(path_argument)
    elif os.path.isdir(path_argument):
        files = os.listdir(path_argument)
        arguments_proceeding(files)
    
path_proceeding(args.path)