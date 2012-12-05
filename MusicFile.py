#import id3
#import os.path

class MusicFile:

    def __init__(self, filepath):
        self.filepath = filepath
        self.addId3Tags()

    def addId3Tags(self):
        # For title, artist, album etc we will replace ' ' with '_' etc
        self.trackNo = 133
        self.title = "Title"
        self.artist = "Artist_Person"
        self.album = "My_Album_(Self_Titled)"
        self.albumArtist = "Artist_Person"
        self.year = 1937

        self.format = ".mp3" # ???!

        return None

    def getOldPath(self):
        return self.filepath

    def getNewPath(self, basepath):
        if basepath[len(basepath)-1] == '/':
            separator = ''
        else: separator = '/'
        return basepath + separator + self.artist + "/" + self.album + "_" + str(self.year) + "/" + str(self.trackNo) + "_" + self.title + self.format

