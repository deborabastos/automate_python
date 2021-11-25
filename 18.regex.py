# Regular expressions are mini-language for specifying text patterns (telephone, social security, etc)
# Regex string often uses backslash, so it is worthy to use raw strings (r'\d')
# You need to import the r module
# re.compile() creates a regex object (a pattern that should be reconized)
# search() method looks for a match
# group() method gets matched strings (actual text)

import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999'

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search(message); #matched object
print(mo.group())

print(phoneRegex.findall(message));

# Is possible to separate the regex in groups using parentheses. For ex, separate the area code from the phone code.
# Parentheses marks where a group begins and ends
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex.search(message);
print(mo.group())
print(mo.group(1))
print(mo.group(2))

# If the regex uses parentheses literally, it is nedeed to use escape character
phoneRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneRegex.search('Call me at (415) 555-1011 tomorrow, or at (415) 555-9999');
print(mo.group())


# Pipe character can be used to match more than a pattern
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

mo = batRegex.search('Batmotocycle lost a wheel')
print(mo== None)

# Sintaxe to match a specific number of repetitions
# ? (zero or one)
batRegex = re.compile(r'Bat(wo)?man') # wo can appers one or zero times
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowoman') # Wont find


# Other example
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('Call me at 415-555-1011 tomorrow');
print(mo.group())
mo = phoneRegex.search('Call me at 555-1011 tomorrow');
print(mo.group())


# * (zero or more)
batRegex = re.compile(r'Bat(wo)*man') # wo can appers one or zero times
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())

# + (one or more)
batRegex = re.compile(r'Bat(wo)+man') # wo can appers one or zero times
mo = batRegex.search('The Adventures of Batman') # Wont find

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowoman') # Wont find
print(mo.group())

# {x} exact number of matches

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('Lalala HaHaHa Papapa')
print(mo.group())
mo = haRegex.search('HaHa') # Wont find

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1011,555-4242,212-555-0000')
print(mo.group())

# {x,y} at leat x, at most y
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('Lalala HaHaHa Papapa')
print(mo.group())
mo = haRegex.search('HaHaHaHaHa')
print(mo.group())

#Greedy and Nongreedy match
#Greedy longest possible match
#Nongreedy shortest possible match

digitRegex = re.compile(r'(\d){3,5}') #Greedy
mo = digitRegex.search('1234567890')
print(mo)

digitRegex = re.compile(r'(\d){3,5}?') #NonGreedy
mo = digitRegex.search('1234567890')
print(mo)

# findall()
# returns a list with each match been a element of the list
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall('Call me at 415-555-1011 tomorrow, or at 415-555-9999'))
# ['415-555-1011', '415-555-9999']

# If you have more then one group, the return will be a list of list

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall('Call me at 415-555-1011 tomorrow, or at 415-555-9999'))
# [('415', '555-1011'), ('415', '555-9999')]

# Characters classes
# digit.Regex = re.compile(r'\d') == re.compile(r'(0|1|2|3|4|5|6|7|8|9)')

# Shorthand character classes			Represents
# \d									Any numeric digit from 0 to 9
# \D									!d
# \w									Any letter, numeric digit, or the underscore character (word)
# \W									!w
# \s									Any space, tab, or newline character. (space)
# \S									!s

# Making your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u)'
print(vowelRegex.findall('Robocop eats baby food.'))
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}') # two vowels in a row
print(doubleVowelRegex.findall('Robocop eats baby food.'))
notVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(notVowelRegex.findall('Robocop eats baby food.'))

aToFRegex = re.compile(r'[a-fA-F]')

# Matching the ^start and end$ 
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there'))
print(beginsWithHelloRegex.search('he said "Hello"')) #None

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world! He said')) # None

# using ^both$ means pattern must match the entire string
allDigitsRegex = re.compile(r'^\d+$') #only numbers
print(allDigitsRegex.search('432423423423423423'))
print(allDigitsRegex.search('432423423x423423423')) #None
print(allDigitsRegex.search('432423423 423423423')) #None

# dot .
# any character except for newline
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat in the flat mat.'))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat in the flat mat.'))

# .*
# any character

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Débora Last Name: Bastos'))

# (.*) is greedy
# (.*?) is nongreedy

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

# re.DOTALL \n
prime = 'Serve the public.\nProtect the innocent.\nUpload the law.'
dotStar = re.compile(r'.*')
print(dotStar.search(prime)) # stops at \n

# To include \n
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime)) # stops at \n

# re.IGNORECASE or re.I
vowelRegex = re.compile(r'[aeiou]', re.I) # or re.IGNORECASE
print(vowelRegex.findall('Robocop Eats baby food.'))

# sub() method
# find and replace

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*') # only return the group (first letter of name)
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')) # 1 is for group 1

# Verbose mode with re.VERBOSE
# ignores \n inside compile - can add commets 
# re.compile(r'''
# (\d\d\d-)		# area code (without parens, with dash)
# |				# or
# (\(\d\d\d) )	# area code (with parens and no dash)
# \d\d\d			# first 3 digits
# -				# second dash
# \d\d\d\d		# last 4 digits
# \sx\d{2,4}		# extension, like x1234
# ''', re.VERBOSE)


