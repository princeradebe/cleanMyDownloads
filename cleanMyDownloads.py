'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Clean myDownloads is a script for moving files into folders.
Grouped by extension
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import shutil
from pathlib import Path

#-------------------------------------------------------------
#Get path to be cleaned and append '/' 
downloadsFolder = input("which folder path would you like to clean? : ").replace('\\', '/') + '/'
#-------------------------------------------------------------
audioPath       = f'{downloadsFolder}Audio/'
documentsPath   = f'{downloadsFolder}Documents/'
softwarePath    = f'{downloadsFolder}Applications/'
photosPath      = f'{downloadsFolder}Photos/'
compressedPath  = f'{downloadsFolder}Compressed/'
videoPath       = f'{downloadsFolder}Video/'
#-------------------------------------------------------------
#File Formats
audioFormat      = [".aac",".flac",".m4a",".mp3",".ogg",".wma",".wav"]
documentFormat   = [".djvu",".doc",".docx",".epub",".odt",".pdf",".xls",".xlsx",".xltx",".ptt",".pttx",".txt", ".dotx", ".torrent"]
softwareFormat   = [".exe", ".jar", ".apk", ".rp", ".msi", ".bat", ".vce"]
photoFormat      = [".bmp",".gif",".ico",".jpg",".jpeg",".jfif",".png",".psd",".tif",".tiff", ".webp"]
compressedFormat = [".7z",".bz2",".gz",".iso",".zip",".rar"]
videoFormat      = [".avi",".flv",".m4v",".mkv",".mov",".mp4",".mpg",".mpeg",".mpeg4",".vid",".wmv"]
#Create folders, if not available to save files
#Only create folder for existing extensions
#If the extension does not have a predefined folder name, create folder based on extension definition (Future Feature)
def createFolder(directory):
    try:
        if not os.path.exists(directory):   #Check folder availability, create if not available
            os.makedirs(directory)
        else:
            print(f"{directory} Already Exist")          #
    except OSError:
        print (f'Error: Creating directory. {directory} Folder already exist')

#List out all files in the Downloads Folder
myFiles = os.listdir(downloadsFolder)
for files in myFiles:
    #Copy all mp3 files to Audio Folder.
    name, ext = os.path.splitext(files)
    if ext.lower() in audioFormat and not os.path.exists(downloadsFolder + audioPath + files):
        # Call creatFolder Function
        createFolder(audioPath)
        shutil.move(downloadsFolder + files, audioPath)

    #Copy all doo files to Documents Folder.
    elif ext.lower() in documentFormat and not os.path.exists(downloadsFolder + documentsPath + files):
        # Call creatFolder Function
        createFolder(documentsPath)
        shutil.move(downloadsFolder + files, documentsPath)

    #Copy all Software files to Software Folder.
    elif ext.lower() in softwareFormat and not os.path.exists(downloadsFolder + softwarePath + files):
        # Call createFolder Function
        createFolder(softwarePath)
        shutil.move(downloadsFolder + files, softwarePath)

    #Copy all Photos to the Photos Folder
    elif ext.lower() in photoFormat and not os.path.exists(downloadsFolder + photosPath + files):
        #Call createFolder Function
        createFolder(photosPath)
        shutil.move(downloadsFolder + files, photosPath)

    #Copy all Compressed files to the Compressed Folder
    elif ext.lower() in compressedFormat and not os.path.exists(downloadsFolder + compressedPath + files):
        #Call createFolder Function
        createFolder(compressedPath)
        shutil.move(downloadsFolder + files, compressedPath)

    #Copy all Video files to the Compressed Folder
    elif ext.lower() in videoFormat and not os.path.exists(downloadsFolder + videoPath + files):
        #Call createFolder Function
        createFolder(videoPath)
        shutil.move(downloadsFolder + files, videoPath)