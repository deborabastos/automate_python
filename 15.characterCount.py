import pprint

# This program will count how many times each letter appears in the message

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} # count is a dictionary with key:value => 'character': value => ex: 'r': 5

for character in message.upper():
	count.setdefault(character, 0)
	count[character] = count[character] + 1

#pprint = pretty print: better outlook
pprint.pprint(count) 

#to save as a string use pformat
rjtext = pprint.pformat(count) 
print(rjtext)

