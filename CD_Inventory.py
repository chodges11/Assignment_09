# ------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# Charles Hodges(hodges11@uw.edu), 2021-Sep-05, Created File
# ------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

# Variables
lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']

# Load files
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)


# Logic to accommodate User interaction with the Inventory menu.
while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':  # Exit
        break

    if strChoice == 'l':  # Load Inventory from the files
        print('WARNING: If you continue, all unsaved data will be lost '
              'and the Inventory will be re-loaded from the file.')
        strYesNo = input(
                         'Type \'yes\' to continue and '
                         'reload from the file. '
                         'Otherwise reload will be canceled. ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('Canceling... Inventory data was NOT reloaded. '
                  'Please press [ENTER] to continue to the menu. ')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    elif strChoice == 'a':  # Add CD
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    elif strChoice == 'd':  # Display Inventory
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    elif strChoice == 'c':  # Select CD
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        while True:
            try:
                cd_idx = int(input('Select the CD / Album ID: '))
                break
            except ValueError:
                print('ID must be an Integer!')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)

        # Logic to accommodate User interaction with the CD sub-menu.
        while True:
            IO.ScreenIO.print_CD_menu()
            strCdChoice = IO.ScreenIO.menu_CD_choice()

            if strCdChoice == 'x':  # Exit
                break

            if strCdChoice == 'a':  # Add a track
                # Display track list prior to addition
                try:
                    IO.ScreenIO.show_tracks(cd)
                except Exception:
                    print('No tracks saved for this album yet. Add some!')
                tplTrkInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrkInfo, cd)
                # Display Track list after addition
                IO.ScreenIO.show_tracks(cd)
                continue  # start loop back at top.

            elif strCdChoice == 'd':  # Display Tracks
                IO.ScreenIO.show_tracks(cd)
                continue  # start loop back at top.

            elif strCdChoice == 'r':  # Remove Tracks
                IO.ScreenIO.show_tracks(cd)
                track_to_rmv = input(
                    '\nSelect the track you wish to remove, '
                    'by Position #: ')
                cd.rmv_track(track_to_rmv)

            else:
                print('General Error')

    elif strChoice == 's':  # Save Inventory to to the files
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input(
            'Save this inventory to the file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The Inventory was NOT saved to the file. '
                  'Please press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    else:
        print('General Error')
