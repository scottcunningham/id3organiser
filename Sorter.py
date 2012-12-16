from MusicFile import MusicFile
import os
import os.path
import shutil

def findMusic(dir):
    print "Searching in", dir

    files = []

    filenames = os.listdir(dir)
    for filename in filenames:
        if os.path.isdir(dir + "/" + filename):
            print "Adding folder", filename
            for file in findMusic(dir + "/" + filename):
                files.append(file)
        elif os.path.isfile(dir + "/" + filename):
            print "Adding", filename
            try:
                files.append(MusicFile(dir + "/" + filename))
            except: 
                print "Not a music file -", dir + "/" + filename
        else:
            print "Not a file or directory:", dir + "/" + filename

    return files

basedir = "/media/windows/Users/Scott/Music/The Cure"
destdir = "/home/scott/mus"

# Get a list of files
musicfiles = findMusic(basedir)

for file in musicfiles:
    print "Old path: ", file.filepath
    print "New path: ", file.getNewPath(destdir)
    if not os.path.exists(destdir + '/' + file.artist):
        os.makedirs(destdir + '/' + file.artist)
    if not os.path.exists(destdir + '/' + '/' + file.artist + '/' + file.albumstr):
        os.makedirs(destdir + '/' + file.artist + '/' + file.albumstr)
    shutil.copy2(file.filepath, file.getNewPath(destdir))
