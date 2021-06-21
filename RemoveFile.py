import os
import shutil
import time

def removeFolder(path):
    if not shutil.rmtree(path):
        print("the path is removed successfully")

    else:
        print(f"Unable to delete the path")
        
def removeFile(path):
    if not os.remove(path):
        print("the path is removed successfully")

    else:
        print(f"Unable to delete the path")

def getAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

def removeAll():
    foldersDeleted = 0
    filesDeleted = 0

    path = input("Enter the path: ")
    days = 30
    second=days * 24 * 3600
    seconds = time.time() - second

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= getAge(root_folder):
                removeFolder(root_folder)
                foldersDeleted += 1 
                break

            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if seconds >= getAge(folder_path):
                        removeFolder(folder_path)
                        foldersDeleted += 1
                        
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    if seconds >= getAge(file_path):
                        removeFile(file_path)
                        filesDeleted += 1 
        else:
            if seconds >= getAge(path):
                removeFile(path)
                filesDeleted += 1 
    else:
        print(f'"{path}" is not found')
        filesDeleted += 1 

    print("Total folders deleted:" ,foldersDeleted)
    print("Total files deleted: ",filesDeleted)




removeAll()