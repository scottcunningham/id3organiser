import eyed3
import string
import os.path

class MusicFile:

    def __init__(self, filepath):
        self.filepath = filepath
        self.audiofile = eyed3.load(filepath)
        self.addId3Tags()

    def addId3Tags(self):
        # For title, artist, album etc we will replace ' ' with '_' etc
        self.trackNo = self.audiofile.tag.track_num[0] # track_num returns a tuple (songNo, songNoOf)
        self.title =  string.replace(self.audiofile.tag.title, ' ', '_')
        self.artist = string.replace(self.audiofile.tag.artist, ' ', '_')
        self.album = string.replace(self.audiofile.tag.album, ' ', '_') 
        self.year = self.audiofile.tag.recording_date
 
        self.format = self.filepath.split('.')[-1:][0]
       
        self.albumstr = self.album + "_(" + str(self.year) + ")"
        self.trackstr = str(self.trackNo) + "_-_" + self.title + "." + self.format
        return None

    def getOldPath(self):
        return self.filepath

    def getNewPath(self, basepath):
        return (os.path.join(basepath, self.artist, self.albumstr, self.trackstr))
    
    def dump(self):
        print "Track #:", self.trackNo
        print "Title:", self.title
        print "Artist:", self.artist
        print "Album:", self.album
        print "Year:", self.year
