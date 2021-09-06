# ------------------------------------------#
# Title: ProcessingClasses.py
# Desc: A Module for processing classes
# Change Log: (Who, When, What)
# Charles Hodges(hodges11@uw.edu), 2021-Sep-05, Created File
# ------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself.')

import DataClasses as DC


class DataProcessor:
    """Processing the data in the application."""
    @staticmethod
    def add_CD(CDInfo, table):
        """Function to add CD info in CDinfo to the inventory table.

        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist)
                to be added to inventory.
            table (list of dict): 2D data structure (list of dicts)
                which holds the data during runtime.

        Returns:
            None.
        """
        cd_id, title, artist = CDInfo
        cd_id = int(cd_id)
        cd_obj = DC.CD(cd_id, title, artist)
        table.append(cd_obj)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """Selects a CD object out of table that has the ID cd_idx.

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        cd_idx = int(cd_idx)
        for row in table:
            if row.cd_id == cd_idx:
                return row
        raise Exception('This CD/Album index does not exist.')

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """Adds a Track object with attributes in track_info to cd.

        Args:
            track_info (tuple): Tuple containing track info
                (position, title, length).
            cd (DC.CD): cd object the track gets added to.

        Raises:
            Exception: Raised in case position is not an integer.

        Returns:
            None:
        """

        position, title, length = track_info
        position = int(position)
        track = DC.Track(position, title, length)
        cd.add_track(track)
