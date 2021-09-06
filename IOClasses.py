# ------------------------------------------#
# Title: IOClasses.py
# Desc: A Module for Input/Output classes
# Change Log: (Who, When, What)
# Charles Hodges(hodges11@uw.edu), 2021-Sep-05, Created File
# ------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself.')

import DataClasses as DC
import ProcessingClasses as PC


class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """Saves the Inventory from the file.

        Args:
            file_name (list): list of file names
                [CD Inventory, Track Inventory], which holds the data
            lst_Inventory (list): list of CD objects

        Returns:
            None.
        """
        # Unpack the file names
        file_cd, file_track = file_name

        try:
            # Save to the CD file
            obj_file = open(file_cd, 'w')
            for disc in lst_Inventory:
                obj_file.write(disc.get_record())
            obj_file.close()

            # Save to the tracks file
            obj_file = open(file_track, 'w')
            for disc in lst_Inventory:
                tracks = disc.cd_tracks
                disc_id = disc.cd_id
                for track in tracks:
                    if track is not None:
                        record = '{},{}'.format(
                                                disc_id,
                                                track.get_record()
                                                )
                        obj_file.write(record)
            obj_file.close()
        except Exception as e:
            print('SAVE INVENTORY - There was a general error!',
                  e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """Loads the Inventory from the file.

        Args:
            file_name (list): list of file names
                [CD Inventory, Track Inventory] that hold the data

        Returns:
            list: list of CD objects
        """
        lst_Inventory = []
        # Unpack the file names
        file_cd, file_track = file_name

        try:
            # Load the CD file
            obj_file = open(file_cd, 'r')
            for line in obj_file:
                cd_info = line.strip().split(',')
                row = DC.CD(
                            cd_info[0],
                            cd_info[1],
                            cd_info[2]
                            )
                lst_Inventory.append(row)
            obj_file.close()

            # Load the Tracks file
            obj_file = open(file_track, 'r')
            for line in obj_file:
                track_info = line.strip().split(',')
                cd = PC.DataProcessor().select_cd(
                                                  lst_Inventory,
                                                  int(track_info[0])
                                                  )
                track = DC.Track(
                                 int(track_info[1]),
                                 track_info[2],
                                 track_info[3]
                                 )
                cd.add_track(track)
            obj_file.close()
        except FileNotFoundError:
            # Create the files if they do not already exist
            FileIO.create_file(file_name)
        except Exception as e:
            print('LOAD INVENTORY - There was a general error!',
                  e, e.__doc__, type(e), sep='\n')
        return lst_Inventory

    @staticmethod
    def create_file(file_name: list) -> None:
        # Unpack the file names
        file_cd, file_track = file_name
        # Create the file
        obj_file = open(file_cd, 'a')
        obj_file.close()
        # Create the file
        obj_file = open(file_track, 'a')
        obj_file.close()


class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user.

        Args:
            None.

        Returns:
            None.
        """

        print(
              'Main Menu\n\n'
              '[l] Load Inventory from file\n'
              '[a] Add CD / Album\n'
              '[d] Display Current Inventory'
              )
        print(
              '[c] Choose CD / Album\n'
              '[s] Save Inventory to file\n'
              '[x] Exit\n'
              )

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection.

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input,
                out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? '
                           '[l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user.

        Args:
            None.

        Returns:
            None.
        """

        print(
              '\nCD Sub Menu\n\n'
              '[a] Add track\n'
              '[d] Display CD / Album details\n'
              '[r] Remove track\n'
              '[x] Exit to Main Menu'
              )

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection.

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input
                out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? '
                           '[a, d, r, or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table.

        Args:
            table (list of dict): 2D data structure (list of dicts)
                which hold the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album.

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """Function to request CD information
           from User to add CD to inventory

        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """
        while True:
            try:
                cdId = int(input('Enter ID: '))
                break
            except ValueError:
                print("ID must be an Integer!")
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """Function to request Track information from User
               to add Track to CD / Album.

        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.
        """
        while True:
            try:
                trkId = int(input('Enter Position on CD / Album: '))
                break
            except ValueError:
                print('Position must be an Integer!')
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength
