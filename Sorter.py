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
                print "Invalid tags or not a music file -", dir + "/" + filename
        else:
            print "Not a file or directory:", dir + "/" + filename

    return files

def sort(basedir, destdir, debug):
    # Get a list of files
    musicfiles = findMusic(basedir)

    if not os.path.exists(destdir):
        print "Destination dir does not exist - creating it"
        os.makedirs(destdir)

    for file in musicfiles:
        print "Old path:", file.filepath
        print "New path:", file.getNewPath(destdir)
        if not os.path.exists(os.path.join(destdir, file.artist, file.albumstr)):
            os.makedirs(os.path.join(destdir, file.artist, file.albumstr))
        if not debug:
            shutil.copy2(file.filepath, file.getNewPath(destdir))

