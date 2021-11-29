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

os.chdir('/Users/deborabastos/Documents/3.Data Science/Curso Python')


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
print(os.path.getsize('/Users/deborabastos/Documents/IMG_9606.jpg'))

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

