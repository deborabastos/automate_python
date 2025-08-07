# 'Hello'

# 'That is Aliece's cat.' => need to use double quote
# "That is Aliece's cat."
# If you need to use single quotes and double quotes inside a string, you need to have a escape character \
# 'That is Aliece\'s cat.'

#		\' 		Single quotes
#		\" 		Double quotes
#		\t 		Tab
#		\n 		Newline
#		\\		Backslash


print('Hello there!\nHow are you?\nI\'m fine.')
print("Hello there!\nHow are you?\nI\'m fine.")

# Row string. Put a r in the beginning of the string. Will ignore any backslashes and escapes.
print(r'This is Carol\'s cat.')

# MULTILINE STRINGS. Use triple quotes (single or double)
print("""Dear Alice, 
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob.""")

spam = """Dear Alice, 
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob."""

print(spam)

#METHODS
# String methods return a new string, rather than modifying a string itself. That's becouse strings are immutable
spam = 'Hello world!'
print(spam.upper()) # Not permanent
print(spam) # Still Hello world!

# To make ir permanet, you can assign the changed string to the variable
spam = spam.upper()
print(spam)

print(spam.lower()) # Not permanent

# isupper() and islower() return True or False
print(spam.islower()) # False
print(spam.isupper()) # True

print('HELLO'.isupper()) # True
print('Hello'.upper().isupper()) # True

#title() :all first letters of words are uppercase. Ex: This Is Title Case
print('hello world!'.title())

# isupper() 		uppercase letters only
# islower() 		lowescase letters only
# isalpha() 		letters only
# isalnum() 		letters and numbers only
# isdecimal() 		numbers only
# isspace() 		whitespace only
# istitle() 		titlecase only (all first letters of words are uppercase. Ex: This Is Title Case)

# startswith() endswith()
print('Hello world'.startswith('H')) # True
print('Hello world'.startswith('Hello')) # True
print('Hello world'.startswith('ello')) # False

print('Hello world'.endswith('d')) # True
print('Hello world'.endswith('world')) # True
print('Hello world'.endswith('w')) # False

# join() useful to join a list into a single string
print(','.join(['cat', 'rat', 'bat'])) #cat,rat,bat
print('-'.join(['cat', 'rat', 'bat'])) #cat-rat-bat
print(' '.join(['cat', 'rat', 'bat'])) #cat rat bat
print(''.join(['cat', 'rat', 'bat'])) #catratbat

# split() takes a string and return a list. By standard space is used to split, but you can change it by adding a argumment
print('My name is Debora'.split()) #['My', 'name', 'is', 'Debora']
print('My name is Debora'.split('m')) #['My na', 'e is Debora']
print('My,name,is,Debora'.split(',')) #['My', 'name', 'is', 'Debora']

#ljust() and rjust() adds a padding after or before the string and fill it it with second argument
print('Hello'.ljust(20)) #"Hello               "
print('Hello'.rjust(20)) #"               Hello"
print('Hello'.ljust(20, '-')) #Hello---------------
print('Hello'.rjust(20, '*')) #***************Hello

#center() adds padding to centralize the string and fill it it with second argument
print('Hello'.center(20)) #'       Hello        '
print('Hello'.center(20, '-')) #-------Hello--------
print('Hello'.center(20, '*')) #*******Hello********

#strip(), rstrip(), lstrip() removes whitespace temporarily (it doesnt substitute the original variable)
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')) #order doesnt matter # BaconSpamEggs

#replace()
print('Hello There! Hey You!'.replace('H', 'h')) #hello There! hey You!

import pyperclip

pyperclip.copy('Hello!!!!!!!!') # sends 'Hello!!!!!!!! to transfer area
print(pyperclip.paste()) # gets 'Hello!!!!!!!! from transfer area


# String FORMATTING
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

str1 = 'Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time +'. Please bring ' + food + '.'
print(str1) # Hello Alice, you are invited to a party at Main Street at 6 pm. Please bring turnips.

# Using place holder
str2 = 'Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)
print(str2) # Hello Alice, you are invited to a party at Main Street at 6 pm. Please bring turnips.



