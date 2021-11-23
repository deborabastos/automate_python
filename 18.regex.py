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



