class Song:
    """
    Class to represent a song

    Attributes:
        title(str):the title of the song
        artist(Artist):artist object representing song creator
        duration(int): duration of songs in seconds

    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method

        :param title: intialises the title of the song
        :param artist: An artis object representing songs creator
        :param duration: Initial value for duration attribute
            will default ot zero if not specified
        """

        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class that represents an Album using track list

    Attributes:
        name (str):The name of the album
        year (int): the year it was released
        artist (Artist): the artis behind the album,
                    It will be defaulted to an artist with various artist
        tracks (List[Song]): A List of songs on the album

        Methods:
            add_song: used to add new song to albums tracklist
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """
        Adds song to a track list

        :param song :(Song) A song to add
        :param position :(int) If specified add the song to the position
        :return: None
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """
    Basic class to store artist details

    Attributes:
        name (str): the name of the artist
        albums (List(albums)): A list of the albums by the artist

    Methods:
        add_album: use add to add new album to artists album
    """

    def __init__(self,name):
        self.name = name
        self.albums = []

    def add_album(self,album):
        """
        Add new album to the list
        :param album: (Album) object to add to the list
                    If album already present not to add again
        :return:None
        """
        self.albums.append(album)

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #  data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for new Artist
                # store the current album in current artists albums collection and then create new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # We've just read anew album for current artist
                # store current album in artists collection and then create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)


            # create new Song object and add it ti current albums collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line of text file we have an artist and album that hasn't been stored process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

