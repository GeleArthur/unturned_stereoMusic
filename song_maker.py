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
core = core.replace(".content.manifest","")

# we begin the making the translation file with the standart 
Translation_songs = open(os.path.join(pathtoFile,'English ' + core +'.translation'),"w",newline='\n')
Translation_songs.write('"Metadata"\n')
Translation_songs.write('{\n')
Translation_songs.write('	"Language" "english"\n')
Translation_songs.write('	"Namespace" "SDG"\n')
Translation_songs.write('}\n')
Translation_songs.write('"Translation"\n')
Translation_songs.write('{\n')
Translation_songs.write('	"Stereo_Songs"\n')
Translation_songs.write('	{\n')
Translation_songs.write('		"'+'Unturned_Theme'+'"\n')
Translation_songs.write('		{\n')
Translation_songs.write('			"Title"\n')
Translation_songs.write('			{\n')
Translation_songs.write('				"Text" "'+'Unturned Theme' + '"\n')
Translation_songs.write('				"Version" "1"\n')
Translation_songs.write('			}\n')
Translation_songs.write('		}\n')



for asset in assests:
    filename = os.path.basename( ( os.path.splitext(asset)[0] ))
    if not os.path.exists(os.path.join(pathtoFile, core + ' assest songs')):
        os.makedirs(os.path.join(pathtoFile, core + ' assest songs'))
    filedescriptor = open(os.path.join(pathtoFile, core + ' assest songs/', filename +'.asset'),"w")
    filedescriptor.write('"Metadata"\n')
    filedescriptor.write('{\n')
    filedescriptor.write('	"GUID" "' + uuid.uuid4().hex + '"\n')
    filedescriptor.write('	"Type" "SDG.Unturned.StereoSongAsset, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null"\n')
    filedescriptor.write('}\n')
    filedescriptor.write('"Asset"\n')
    filedescriptor.write('{\n')
    filedescriptor.write('	"ID" "0"\n')
    filedescriptor.write('	"Title"\n')
    filedescriptor.write('	{\n')
    filedescriptor.write('		"Namespace" "SDG"\n')
    filedescriptor.write('		"Token" "Stereo_Songs.' + filename + '.Title"\n')
    filedescriptor.write('	}\n')
    filedescriptor.write('	"Song"\n')
    filedescriptor.write('	{\n')
    filedescriptor.write('		"Name" "' + core + '.content"\n')
    filedescriptor.write('		"Path" "' + asset + '"\n')
    filedescriptor.write('	}\n')
    filedescriptor.write('}')
    filedescriptor.close

    Translation_songs.write('		"'+filename+'"\n')
    Translation_songs.write('		{\n')
    Translation_songs.write('			"Title"\n')
    Translation_songs.write('			{\n')
    Translation_songs.write('				"Text" "'+ filename.replace("_"," ") +'"\n')
    Translation_songs.write('				"Version" "1"\n')
    Translation_songs.write('			}\n')
    Translation_songs.write('		}\n')
    print(filename.replace("_"," "))

Translation_songs.write('	}\n')
Translation_songs.write('}\n')

print('done')
Translation_songs.close