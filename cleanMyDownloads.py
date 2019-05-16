'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Clean myDownloads is a script for moving files into folders.
Grouped by extension
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import shutil
from pathlib import Path

#-------------------------------------------------------------
#downloadsFolder = r"C:\Users\radebep\Downloads"
downloadsFolder = "C:/Users/radebep/Downloads/"
#-------------------------------------------------------------
audioPath       ='C:/Users/radebep/Downloads/Audio/'
documentsPath   ='C:/Users/radebep/Downloads/Documents/'
softwarePath    ='C:/Users/radebep/Downloads/Applications/'
photosPath      ='C:/Users/radebep/Downloads/Photos/'
compressedPath  ='C:/Users/radebep/Downloads/Compressed/'
videoPath       ='C:/Users/radebep/Downloads/Video/'
#-------------------------------------------------------------
#Formats
#audioF  = [".mp3",".mp4"]
#Create folders, if not available to save files (Documents/Applications/Audio/Photos/Compressed Files)
#Only create folder for existing extensions
#If the extension does not have a predefined folder name, create folder based on extension definition (Future Feature)
def createFolder(directory):
    try:
        if not os.path.exists(directory):   #Check folder availability, create if not available
            os.makedirs(directory)          #
    except OSError:
        print ('Error: Creating directory. ' +  directory + 'Folder already exist')

#List out all files in the Downloads Folder
myFiles = os.listdir(downloadsFolder)
for files in myFiles:
    #Copy all mp3 files to Audio Folder.
    if ".mp3" in files and not os.path.exists(downloadsFolder + audioPath + files):
        # Call creatFolder Function
        createFolder(audioPath)
        shutil.copy(downloadsFolder + files, audioPath)

    #Copy all doo files to Documents Folder.
    elif ".doc" in files and not os.path.exists(downloadsFolder + documentsPath + files):
        # Call creatFolder Function
        createFolder(documentsPath)
        shutil.copy(downloadsFolder + files, documentsPath)
