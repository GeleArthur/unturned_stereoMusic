# created by gelearthur
import os
import re
import argparse

# argunemts
parser = argparse.ArgumentParser()

# stolen from https://stackoverflow.com/questions/11415570/directory-path-types-with-argparse
def removeSpaces(values):
    # is this a folder if true ERROR
    if not os.path.isdir(values):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(values))
    # do we have permission
    if os.access(values, os.R_OK):
        # loop over every file in that folder
        for filename in os.listdir(values):
            # tbe new file name
            filename_new = filename.replace(" ","_")
            filename_new = re.sub(r'[^\.a-zA-Z0-9_-]',"",filename_new)
            # why change if they are the same
            if filename_new != filename:
                print(filename_new)
                # make the change
                os.rename(values + '\\'+ filename, values + '\\' + filename_new)
    else:
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(values))

# arguments
parser.add_argument('-f','--folder',help="a folder to remove spaces",required=True)
args = parser.parse_args()
removeSpaces(args.folder)