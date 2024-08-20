import os

source = "folder"
destination = "C:\\Users\\ttorres\\OneDrive - Market Resource Partners\\Desktop\\2024\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source,destination)
        print(source+" was moved.")
except FileNotFoundError:
    print(source+" was not found.")