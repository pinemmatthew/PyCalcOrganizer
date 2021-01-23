from pathlib  import Path
import	urllib.request
import subprocess
import sys
import shutil
import zipfile




	

#user_input = input("Enter name: ")
#user_input1 = input('Enter case: ')
#user_input2	= input('Enter case: ')
#user_input3	= input('Enter case: ')


#path1 = user_input
#if not os.path.exists(path1):
 #   os.makedirs(path1)
#path2 = user_input1
#if not os.path.exists(os.path.join(user_input, user_input1,)):
 #   os.makedirs(os.path.join(path1, path2,))
#path3 = user_input2
#if not os.path.exists(os.path.join(user_input, user_input1,user_input2)):
 #   os.makedirs(os.path.join(path1, path2,path3))
#path4 = user_input3
#if not os.path.exists(os.path.join(user_input, user_input1,user_input2,user_input3)):
 #   os.makedirs(os.path.join(path1, path2,path3,path4))



rootdir = Path(input('Enter root dir: '))
subdirs = [input(f'Enter sub dir {i+1}: ') for i in range(3)]
 
full_path = rootdir.joinpath(*subdirs)
full_path.mkdir(parents=True, exist_ok=True)





url	=	'https://hpxeosandthermocalc.files.wordpress.com/2020/12/tc350-win-bundle.zip'
file_name	=	'tc350_win_bundle.zip'

with urllib.request.urlopen(url)	as	response, open(file_name, 'wb')	as	out_file:
	shutil.copyfileobj(response, out_file)
	with zipfile.ZipFile(file_name) as zf:
		zf.extractall()




ZipFileName	=input("Enter full path to zip file:")
fh	=	open(ZipFileName, 'rb')
z	=	zipfile.ZipFile(fh)

DestZipFolderName	=	input("Assign destination folder a name:")
DestPathName	=	input("Enter destination directory:")
DestPathName	=	DestPathName	+	"\\"	+	DestZipFolderName

for name in	z.namelist('example.zip'):
	outpath	=	DestPath
	z.extract(name,	outpath)
fh.close()




#filename	=	input("filename: ")
#with open(filename,	"w")	as	f:
#	f.write(input())
	
				





