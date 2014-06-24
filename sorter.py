from musicfile import MusicFile
import os
import os.path
import shutil


def find_music(dir):
    print "Searching in", dir

    files = []

    filenames = os.listdir(dir)
    for filename in filenames:
        if os.path.isdir(dir + "/" + filename):
            print "Adding folder", filename
            for file in find_music(dir + "/" + filename):
                files.append(file)
        elif os.path.isfile(dir + "/" + filename):
            print "Adding", filename
            try:
                files.append(MusicFile(dir + "/" + filename))
            except:
                print "Invalid tags or not a music file:", \
                    os.path.join(dir, filename)
        else:
            print "Not a file or directory:", dir + "/" + filename

    return files


def sort(basedir, destdir, debug, quiet):
    # Get a list of files
    musicfiles = find_music(basedir)

    if not debug:
        if not os.path.exists(destdir):
            print "Destination dir does not exist - creating it"
            os.makedirs(destdir)

    for file in musicfiles:
        if not quiet:
            print "Old path:", file.filepath
            print "New path:", file.get_new_path(destdir)
        if not debug:
            if not os.path.exists(os.path.join(destdir, file.artist,
                                               file.albumstr)):
                os.makedirs(os.path.join(destdir, file.artist, file.albumstr))
            shutil.copy2(file.filepath, file.get_new_path(destdir))
