from ftplib import FTP
import os

ftp = FTP("10.10.104.200")
ftp.login()
ftp.cwd('/DATA/My Documents/OTDR')
filenames = ftp.nlst()

print(filenames)