spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0]) # cat

#Slices
print(spam[1:3]) # ['bat', 'rat']
print(spam[:2]) # ['cat', 'bat']
print(spam[:]) # ['cat', 'bat', 'rat', 'elephant']

#list of list
spam = [['cat', 'bat', 'rat'], [10, 20, 30]]
print(spam[0][1]) # bat 
print(spam[1][2]) # 30
print(spam[1][-1]) # 30
print(spam[1][-2]) # 20

spam = ['cat', 'bat', 'rat', 'elephant']
# delete list item
del spam[2] 
print(spam) # ['cat', 'bat', 'elephant'] => it doens leave a gap
del spam[2] 
print(spam) # ['cat', 'bat']

spam = ['cat', 'bat', 'rat', 'elephant']
#count list
print(len(spam)) # 4
print(len([1,2,3])) # 3

#Concatenate lists
lista = [1,2,3] + [4,5,6]
print(lista)
print(lista + spam) # [1, 2, 3, 4, 5, 6, 'cat', 'bat', 'rat', 'elephant']

#Multiply lists
multi = [1,2,3] * 3
print(multi) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#Transform string in list 
hi = list('Hello')
print(hi) # ['H', 'e', 'l', 'l', 'o']

#Verify if a string or value is contained within the list
test = 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
print(test) # True
test = 'oie' in ['hello', 'hi', 'howdy', 'heyas']
print(test) # False
test = 'howdy' not in ['hello', 'hi', 'howdy', 'heyas']
print(test) # False
test = 'oie' not in ['hello', 'hi', 'howdy', 'heyas']
print(test) # True

#Create a sequencial list
print(list(range(0,50,2)))
