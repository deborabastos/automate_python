# Print list items using for
for i in range(4):
	print(i)

#range(4) = range(0,4) = [0,1,2,3]
print(list(range(4)))
print(list(range(0,4)))
print(list([0,1,2,3]))
print(list(range(0,26)))
print(list(range(0,50,2)))

#print values of a list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is ' + supplies[i])

#Multiple assignments
cat = ['fat', 'orange', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]
size, color, disposition = cat
print(size, color, disposition)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size, color, disposition)

#Swapping variables
a = 'AAA'
b = 'BBB'
print(a, b)
a, b = b, a
print(a, b)

#Augmented assignments statements
spam = 42
print(spam)
spam = spam + 1
print(spam)
spam += 1
print(spam)

# spam += 1 == spam = spam + 1
# spam -= 1 == spam = spam - 1
# spam *= 1 == spam = spam * 1
# spam /= 1 == spam = spam / 1
# spam %= 1 == spam = spam % 1

