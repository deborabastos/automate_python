# There are many things you do with list that can be applied for strings
print(list('Hello'))

name = 'Zophie'
print(name[0]) #Z
print(name[1:3]) #op
print(name[-2]) #i

bol = 'Zo' in name
print(bol) #True
bol = 'xxx' in name
print(bol) #False

for letter in name:	
	print(letter)

# The difference between them is that lists are mutable data types and strings are immutable
# Mutable data types works as pointer in C (only strores the reference, not the actual data)
# name = 'Zophie the cat'
# print(name[7])
# name[7] = 'X'
# print(name[7])

# So, if you want to modify a string. You will have to use slices
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name) 
print(newName)

def eggs(cheese):
	cheese.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) #[1, 2, 3, 'Hello'] - Note that Hello will be added to the list. This is only possible because is a reference

# If you want to make a real copy of a list, use function deepcopy from copy library 
import copy
spam = [1, 2, 3]
cheese = copy.deepcopy(spam)
cheese[1] = 0
print(spam) #[1, 2, 3]
print(cheese) #[1, 0, 3]


# Line continuation
spam = ['apple',
		'banana', 
		'orange', 
		'grape']

# You can do the same by using tha \ continuation
print('Four score and seven' + \
	' years ago') #Four score and seven years ago
