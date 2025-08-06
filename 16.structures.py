import pprint

# A list of dictionaries are called data structure

cat = {'name':'Zophie', 'age':7, 'color':'gray'}
allCats = []
allCats.append({'name':'Zophie', 'age':7, 'color':'gray'})
allCats.append({'name':'Pooka', 'age':5, 'color':'black'})
allCats.append({'name':'Fat-tail', 'age':5, 'color':'gray'})
allCats.append({'name':'???', 'age':-1, 'color':'orange'})

pprint.pprint(allCats)

print(type(42)) # <class 'int'>
print(type('hello')) # <class 'str'>
print(type(3.14)) # <class 'float'>
print(type(cat)) # <class 'dict'>
print(type(cat['name'])) # <class 'str'>
print(type(cat['age'])) # <class 'int'>
