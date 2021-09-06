# ------------------------------------------#
# Title: DataClasses.py
# Desc: A Module for data classes
# Change Log: (Who, When, What)
# Charles Hodges(hodges11@uw.edu), 2021-Sep-05, Created File
# ------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself.')


class Track():
    """Stores Data about a single Track:

    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        __str__() --> (str): Track details as formatted string.
        get_record() -> (str): Track record formatted for saving to file.
    """

    # -- Constructor -- #
    def __init__(self, position, title, length):
        self.__position = position
        self.__title = title
        self.__length = length

    # -- Properties -- #
    # Getter and Setter for the Track's position
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    # Getter and Setter for the Track's title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    # Getter and Setter for the Track's length
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    # -- Methods -- #
    def __str__(self):
        """Returns: Track details as formatted string."""
        return ('{: <7} {: <20} {: <20}'.format(
            str(self.position), str(self.title), str(self.length)))

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{},{},{}\n'.format(
                                   str(self.position),
                                   str(self.title),
                                   str(self.length)
                                   )


class CD:
    """Stores data about a CD / Album.

    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)

    """

    # -- Constructor -- #
    def __init__(
                 self,
                 cd_id: int,
                 cd_title: str,
                 cd_artist: str
                 ) -> None:
        """Set ID, Title, and Artist of a new CD Object"""
        #    -- Attributes  -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__tracks = []
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # Getter and Setter for the CD's ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be an Integer')

    # Getter and setter for the CD's Title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be a String!')

    # Getter and Setter for the CD's Artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be a String!')

    # Getter for the CD's tracks
    @property
    def cd_tracks(self):
        return self.__tracks

    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string."""
        return '{:>2}\t{} (by: {})'.format(
            self.cd_id, self.cd_title, self.cd_artist)

    def get_record(self):
        """Returns: CD record formatted for saving to file."""
        return '{},{},{}\n'.format(
                                   self.cd_id,
                                   self.cd_title,
                                   self.cd_artist
                                   )

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD/Album.

        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.
        """
        # Append track
        self.__tracks.append(track)

        # Sort tracks
        self.__sort_tracks()

    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from the Album.

        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.
        """
        # Remove track
        self.__tracks.remove(self.__tracks[int(track_id)-1])

        # Sort tracks
        self.__sort_tracks()

    def __sort_tracks(self):
        """Sorts the tracks using Track.position.
           Fills blanks with None."""
        n = len(self.__tracks)
        for track in self.__tracks:
            if (track is not None) and (n < track.position):
                n = track.position
        tmp_tracks = [None] * n
        for track in self.__tracks:
            if track is not None:
                tmp_tracks[track.position - 1] = track
        self.__tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album.

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.
        """
        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track.\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """Gets a formatted long record of the Album:
           Album information plus track details.

        Returns:
            result (string): Formatted information about Album
                             and its tracks.

        """
        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result
