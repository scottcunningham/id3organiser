from MusicFile import MusicFile

def findMusic(dir):
    print "Searching in", dir

    files = []

    filenames = ["abc.mp3", "dododo.mp3", "blah.mp3"]
    #filenames = findAllInCurDir
    for filename in filenames:
        print "Adding", filename
        files.append(MusicFile(filename))    

    if dir == "/home/scott/Music":
        folders = ["folder1"]
    #folders = findAllFoldersInCurDir
    else:
        folders = []

    for folder in folders:
        files.appendall(findMusic(dir + folder))

    return files

basedir = "/home/scott/Music"

# Get a list of files
musicfiles = findMusic(basedir)

for file in musicfiles:
    # We'll want to move each file from current dir to dest dir
    # Just print it for now
    print "Old path: ", file.filepath
    print "New path: ", file.getNewPath(basedir)
