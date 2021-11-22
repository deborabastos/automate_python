# Dictionay is a collection of many values
# Unlike list, it accepts different data types
# Indexes for dictionary are called keys 

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age': 8}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur')

# Unlike list, dictionaries are unordered (itens order do not matter)
spam = {12345: 'Luggage combination', 42: 'The Answer'}
eggs = {42: 'The Answer', 12345: 'Luggage combination'}
print(spam == eggs) # True

# You can check if a key belongs to a dictionary using "in"
'42' in spam # True
'name' in spam # False

# DICTIONARIES METHODS
# keys(), values(), items()
print(list(myCat.keys()))
print(list(myCat.values()))
print(list(myCat.items()))

for k in myCat.keys():
	print(k)

for v in myCat.values():
	print(v)

for k, v in myCat.items():
	print(k, v)

# To check if a value belongs to a dictionary, you need to call method items
'gray' in myCat.items() # True

# get() method will look for a key. If it exists, returns the value, if it does not exist, the secound parameter is returned
print(myCat.get('age', 0)) # return 8
print(myCat.get('ages', 'x')) # return 'x'

# setdefault(). Defines a key and value only if it is not set yet.
myCat.setdefault('name', 'Zophie')
print(myCat)
myCat.setdefault('name', 'Puka')
print(myCat)
