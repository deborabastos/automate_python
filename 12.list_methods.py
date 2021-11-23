# Method
# The method name comes after the variable, separeted by .

# INDEX method returns tha index number of a value
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))
# if the value doesnt exist in the list, a error will occur
# print(spam.index('ups'))
# if the value is duplicated in the list, the first one will return
spam = ['heyas', 'hello', 'hi', 'howdy', 'heyas']
print(spam.index('heyas'))

# APPEND method adds a value at the end of the list
spam = ['heyas', 'hello', 'hi', 'howdy', 'heyas']
spam.append('UPS')
print(spam)

# INSERT method adds a value wherever you want
spam = ['heyas', 'hello', 'hi', 'howdy', 'heyas']
spam.insert(1,'UPS')
print(spam)

# OBS: you cannot assign a append or insert result into the variable. That's because the return of this fuction is null
# spam = spam.append('hola') will clear the spam list

# REMOVE method removes a value from the list (only removes the first apperance)
# if value doesnot exist, you get a error
spam = ['heyas', 'hello', 'hi', 'howdy', 'heyas']
spam.remove('heyas')
print(spam)

# SORT method sorts values according to asciibetical
spam = [5, 2, 6, 0, 1, -5]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# to reverse order
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort(reverse=True)
print(spam)

# You cant sort list with numbers and strings
# spam = [1, 2, 'ants', 'cats', 'dogs', 'badgers', 'elephants']
# spam.sort()
# print(spam)

# In asciibetical order, uppercase comes before lowercase
spam = ['ants', 'cats', 'Alice', 'Zumba', 'ziggy']
spam.sort()
print(spam)

# If you want real alphabetical order, you nedd to add key=str.lower
spam = ['ants', 'cats', 'Alice', 'Zumba', 'ziggy']
spam.sort(key=str.lower)
print(spam)

