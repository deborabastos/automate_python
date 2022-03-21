# To create a file path you can use the os library and join fucntion
import os

# The path separator symbol differs from operating system. 
# For exemple, Windows uses \, while MacOs uses /
# os library will chose the correct separator for the running os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png')) 	# MacOs: folder1/folder2/folder3/file.png
															# Windows: folder1\\folder2\\folder3\\file.png
print(os.sep) #return the os path separator

# To get the current working directory
print(os.getcwd())

# To change the current working directory
os.chdir('/Users/deborabastos/Documents/')
print(os.getcwd())

os.chdir('/Users/deborabastos/Documents/3.DataScience/automate_python')


# Absolute file path always beggings with the root folder
# Relative file path is always relative to the current working directory

# . 	current folder
# .. 	parent folder

# abspath() returns the absolute path of a file in the current working directory
print(os.path.abspath('teste.txt'))
print(os.path.abspath('../../teste.txt'))

# isabs() checks whether a path is absolute
print(os.path.isabs('../../teste.txt'))
print(os.path.isabs('/../../teste.txt'))

# realpath() gives you the relative path between two paths that you give it
print(os.path.relpath('/folder1/folder2/teste.txt', '/folder1'))

# dirname() returns only the directory part of a path (not the file name)
print(os.path.dirname('/Users/deborabastos/Documents/test.txt'))

# basename() returns the last part of a given path
print(os.path.basename('/Users/deborabastos/Documents/test.txt'))

# exist() checks if a file actually exists
print(os.path.exists('/Users/deborabastos/Documents/test.txt'))
print(os.path.exists('/Users/deborabastos/Documents/IMG_9606.jpg'))

# isfile() checks if is a file
# isdir() checks if is a directory

print(os.path.isfile('/Users/deborabastos/Documents/IMG_9606.jpg')) # True
print(os.path.isdir('/Users/deborabastos/Documents/IMG_9606.jpg')) # False

print(os.path.isfile('/Users/deborabastos/Documents/')) # False
print(os.path.isdir('/Users/deborabastos/Documents/')) # True

# getsize() # returns the size in bytes as a integer
# print(os.path.getsize('/Users/deborabastos/Documents/IMG_9606.jpg'))

# listdir()
print(os.listdir('/Users/deborabastos/Documents/'))


#### total size of all files in a folder
totalSize = 0
for filename in os.listdir('/Users/deborabastos/Documents/'):
	if not os.path.isfile(os.path.join('/Users/deborabastos/Documents/', filename)):
		continue
	totalSize = totalSize + os.path.getsize(os.path.join('/Users/deborabastos/Documents/', filename))
print(totalSize)

# makedirs() creates a new folder () or a sequence of new folders
# os.makedirs('/Users/deborabastos/Documents/delicious/walnut/waffles')

################################################################
# Reading and writing PLAINTEXT (for variables, use shelve module)
# open('path')

helloFile = open('01.hello.py')

# read() and close() method
content = helloFile.read()
print(content)
helloFile.close()

# readlines() saves every line as a string inside of a list. read() only returns a single string
helloFile = open('01.hello.py')
content = helloFile.readlines()
print(content)
helloFile.close()

# Write mode
# w open a file in write mode. It will overwrite any existing content with the new content. It returns how many chars was written to the file
# a open a file in append mode. It will append the new content to the existing content
# In both cases, is the file does not exists, python will create a new file

helloFile = open('write.txt', 'w')
helloFile.write('Hello!!!!!!!!')
helloFile.close()

helloFile = open('write.txt', 'w')
helloFile.write('World!!!') # overwrites
helloFile.close()

helloFile = open('write.txt', 'w')
helloFile.write('Hello!!!!!!!!')
helloFile.close()

helloFile = open('write.txt', 'a')
helloFile.write(' World!!!') # appends
helloFile.close()

## shelve module is needed to store variables that have lists or dictionaries
# shelve module saves in binary shelve files

import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

################################################################
# Coping and moving files
import shutil
# shutil.copy(<file>, <destiny path>)
# you can also rename file
shutil.copy('write.txt', '/Users/deborabastos/Documents/3.DataScience/automate_python/automate_online-materials')

# To copy folder
shutil.copytree('automate_online-materials', 'automate_online-materials_backup')

# Move a file to another folder
# You can use the move function to rename a file
shutil.move('mydata.db', 'automate_online-materials')
shutil.move('automate_online-materials/mydata.db', 'automate_online-materials/mydata2.db')



############################################################################
# DELETING
# Delete and remove files
# ATENTION IT WILL BE DELETED PERMANENTLY
import os
os.unlink('automate_online-materials/mydata2.db') # deletes a single file
os.unlink('automate_online-materials/write.txt') # deletes a single file
# os.unlink('write.txt')

# Delete a EMPTY folder
# ATENTION IT WILL BE DELETED PERMANENTLY
# os.rmdir('automate_online-materials_backup')

# Delete a folder and it contents
# ATENTION IT WILL BE DELETED PERMANENTLY
shutil.rmtree('automate_online-materials_backup')


# Dry run
# for filename in os.listdir():
	# if filename.endswith('.txt'):
		# os.unlink(filename) uncomment after you check filenames
		# print(filename)

# If you want to send to trash instead of permanent deleting, use send2trash module
import send2trash
send2trash.send2trash('write.txt')

############################################################################
# Walking a dictionary tree
for folderName, subfolders, filenames in os.walk('/Users/deborabastos/Documents/3.Data Science/Curso Python'):
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are ' + str(subfolders))
	print('The filenames in ' + folderName + ' are ' + str(filenames))
	print('\n')

	for subfolder in subfolders:
		if 'fish' in subfolder:
			os.rmdir(subfolder)
	for file in filenames:
		if file.endswith('.py'):
			shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))