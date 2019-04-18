'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Clean myDownloads is a script for moving files into a folder.
Grouped by extension
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os

audioPath       ='C:/Users/radebep/Downloads/Audio/'
domumentsPath   ='C:/Users/radebep/Downloads/Documents/'
softwarePath    ='C:/Users/radebep/Downloads/Softwares/'
photosPath      ='C:/Users/radebep/Downloads/Photos/'
compressedPath  ='C:/Users/radebep/Downloads/Compressed/'

#Create folders, if not available to save files (Documents/Softwares/Audio/Photos/Compressed Files)
#Only create foder for existing extensions
#If the extension does not have a predefined folder name, create folder based on extension definition
def createFolder(directory):
    try:
        if not os.path.exists(directory):   #Check folder availability, create if not available
            os.makedirs(directory)          #
    except OSError:
        print ('Error: Creating directory. ' +  directory + 'Folder already exist')
        
# Call creatFolder Function
#createFolder()

myFiles = os.listdir(r"C:\Users\radebep\Downloads")
for files in myFiles:
    print(files)




#List out all files in the Downloads Folder

#Copy files to the relevent folder.
