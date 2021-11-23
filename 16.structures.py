import pprint

# A list of dictionaries are called data structure

cat = {'name':'Zophie', 'age':7, 'color':'gray'}
allCats = []
allCats.append({'name':'Zophie', 'age':7, 'color':'gray'})
allCats.append({'name':'Pooka', 'age':5, 'color':'black'})
allCats.append({'name':'Fat-tail', 'age':5, 'color':'gray'})
allCats.append({'name':'???', 'age':-1, 'color':'orange'})

pprint.pprint(allCats)

# type() return the data type 
type(42) # <class 'int'>
type('hello') # <class 'str'>
type(3.14) # <class 'float'>
type(cat) # <class 'dict'>
type(cat['name']) # <class 'str'>
type(cat['age']) # <class 'int'>
