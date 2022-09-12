from ftplib import FTP
import os


ftp = FTP("10.10.104.200") # ftp server (odtr device)
ftp.login() # default credentials
fipPath = ('C:/temp2/fip') #locations of the copied files
otdrPath = ('C:/temp2/otdr') #locations of the copied files


## creates folder Dirs if it does not exist ##
isExistODTR = os.path.exists(otdrPath)
if not isExistODTR:
    os.makedirs(otdrPath)
isExistFIP = os.path.exists(fipPath)
if not isExistFIP:
    os.makedirs(fipPath)


#### OTDR ####
ftp.cwd('/DATA/My Documents/OTDR') # moves the wd to otdr
filenamesodtr = ftp.nlst() #creates list of current working dir
for filename in filenamesodtr:
    os.chdir(otdrPath) #save location
    with open( filename, 'wb' ) as file :
        ftp.retrbinary('RETR %s' % filename, file.write) #RETR copies the file


#### FIP ####
#function for copying the  file
ftp.cwd('/DATA/My Documents/CMAX2') #moves read location to cmax2
filenamesfip = ftp.nlst() # makes a list of the files in cwd
for filename in filenamesfip:
    os.chdir(fipPath) # save location
    with open( filename, 'wb' ) as file :
        ftp.retrbinary('RETR %s' % filename, file.write)
    file.close() # closes ftw collection


ftp.quit()