import	os
import	urllib
import requests
import zipfile


r	=	requests.get(
		'https://hpxeosandthermocalc.files.wordpress.com/2020/12/tc-prefs.txt_-1.zip')

with open('data.zip','wb')	as	f:
	f.write(r.content)








ZipFileName	=	input("Enter full path to zip file:")
fh	=	open(	ZipFileName, 'rb')
z	=	zipfile.ZipFile(fh)

DestZipFolderName	=	input("Assign destination folder a name:")
DestPathName	=	input("Enter destination directory:")
DestPathName	=	DestPathName	+	"\\"	+	DestZipFolderName

for name in	z.namelist():
	outpath	=	DestPath
	z.extract(name,	outpath)
fh.close()
	

				





