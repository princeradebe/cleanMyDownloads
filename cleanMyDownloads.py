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
#File Formats
audioFormat      = [".aac",".flac",".m4a",".mp3",".ogg",".wma",".wav"]
documentFormat   = [".djvu",".doc",".docx",".epub",".odt",".pdf",".xls","xlsx",".ptt",".pttx",".txt"]
softwareFormat   = [".exe"]
photoFormat      = [".bmp",".gif",".ico",".jpg",".jpeg",".png",".psd",".tif",".tiff"]
compressedFormat = [".7z",".bz2",".gz",".iso",".zip",".rar"]
videoFormat      = [".avi",".flv",".m4v",".mkv",".mov",".mp4",".mpeg",".mpeg4",".vid",".wmv"]
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
    name, ext = os.path.splitext(files)
    if ext in audioFormat and not os.path.exists(downloadsFolder + audioPath + files):
        # Call creatFolder Function
        createFolder(audioPath)
        shutil.copy(downloadsFolder + files, audioPath)

    #Copy all doo files to Documents Folder.
    elif ext in documentFormat and not os.path.exists(downloadsFolder + documentsPath + files):
        # Call creatFolder Function
        createFolder(documentsPath)
        shutil.copy(downloadsFolder + files, documentsPath)

    #Copy all Software files to Software Folder.
    elif ext in softwareFormat and not os.path.exists(downloadsFolder + softwarePath + files):
        # Call createFolder Function
        createFolder(softwarePath)
        shutil.copy(downloadsFolder + files, softwarePath)

    #Copy all Photos to the Photos Folder
    elif ext in photoFormat and not os.path.exists(downloadsFolder + photosPath + files):
        #Call createFolder Function
        createFolder(photosPath)
        shutil.copy(downloadsFolder + files, photosPath)

    #Copy all Compressed files to the Compressed Folder
    elif ext in compressedFormat and not os.path.exists(downloadsFolder + compressedPath + files):
        #Call createFolder Function
        createFolder(compressedPath)
        shutil.copy(downloadsFolder + files, compressedPath)

    #Copy all Video files to the Compressed Folder
    elif ext in videoFormat and not os.path.exists(downloadsFolder + videoPath + files):
        #Call createFolder Function
        createFolder(videoPath)
        shutil.copy(downloadsFolder + files, videoPath)