#!/usr/bin/env bash

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 202-647-4000, 647-4000, (415) 647-4000, 647-4000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?		# area code (optional)
(\s | -)						# first separator
\d\d\d							# first 3 digits
-								# separator
\d\d\d\d						# last 4 digits
((ext(\.)?\s | x)				# extension word-part (optional)
(\d{2,5}))?						# extension number-part (optional)
)								# put everything in a group, so it will be returned
''', re.VERBOSE)

# Create a regex for e-mail addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+		# name part
@					# @ symbol
[a-zA-Z0-9_.+]+		# domain name part
''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text) # Returns a list of multiples
extractedEmail = emailRegex.findall(text) # Returns a list

print(extractedPhone)
print(extractedEmail)

# Extract the first number at extractedPhone to form a list
allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail) # put every result in a line
pyperclip.copy(results)


