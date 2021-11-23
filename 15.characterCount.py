import pprint

# This program will count how many times each letter appears in the message

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} # 'character': value => ex: 'r': 5

for character in message.upper():
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count) 