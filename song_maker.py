# created by gelearthur

# imports
import uuid
import os
import argparse

# arguments
parser = argparse.ArgumentParser("Script that makes music files for unturned")
parser.add_argument('-f','--file',help="A path to the myMusic.content.manifest",required=True)
args = parser.parse_args()

# a loop thing
assests_found = 0
# all the file names
assests = []
# the name of the .content.manifest file
core = os.path.basename(args.file)
# path to the .content.manifest file
pathtoFile = os.path.dirname(args.file)

# we loop over every line in the .content.manifest file
# if we hit the Assets: line we know that the assets names begin record
# and add them to the assets array
# then if we see Dependencies: [] we stop
with open(os.path.join(pathtoFile,core) ,'r') as file:
    for line in file:
        if assests_found == 1:
            if line =='Dependencies: []\n':
                assests_found=0
            else:
                assests.append(line.strip('\n- '))
        if line == 'Assets:\n':
            assests_found=1

# print them
print(assests)

# we don't need the .content.manifest any more
core = core.replace(".manifest","")

for asset in assests:
    asset = asset.replace("Assets/", "")
    filename = os.path.basename( ( os.path.splitext(asset)[0] ))
    if not os.path.exists(os.path.join(pathtoFile, filename)):
        os.makedirs(os.path.join(pathtoFile, filename))
    filedescriptor = open(os.path.join(pathtoFile, filename, filename +'.asset'),"w")
    filedescriptor.write('"Metadata"\n')
    filedescriptor.write('{\n')
    filedescriptor.write('	"GUID" "' + uuid.uuid4().hex + '"\n')
    filedescriptor.write('	"Type" "SDG.Unturned.StereoSongAsset, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null"\n')
    filedescriptor.write('}\n')
    filedescriptor.write('"Asset"\n')
    filedescriptor.write('{\n')
    filedescriptor.write('	"ID" "0"\n')
    filedescriptor.write('	"Title" "' + filename + '"\n')
    filedescriptor.write('	"Song"\n')
    filedescriptor.write('	{\n')
    filedescriptor.write('		"Name" "' + core + '"\n')
    filedescriptor.write('		"Path" "' + asset + '"\n')
    filedescriptor.write('	}\n')
    filedescriptor.write('}')
    filedescriptor.close

    print(filename.replace("_"," "))


print('done')
