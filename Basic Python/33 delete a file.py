import os
import shutil #to delete folders containing files.

path = "folder"

try:
    #os.remove(path) #removes local to the program file.
    #os.rmdir(path) #removes EMPTY folder as opposed to file.
    #shutil.rmtree(path) #removes folder with files and other folders within.
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to delete that.")
except OSError:
    print("You cannot delete that using that function.")
else:
    print(path+" was deleted.")

