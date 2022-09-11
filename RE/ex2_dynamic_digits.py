'''
Write a regex pattern that will match any non-digits, followed by double digit,
followed by text.
'''


#========================================Exercise======================================#
text = "There are 365 days in a year, 24 hours in a day, and 60 minutes in an hour"

pattern="\D\d\d\D"

#===============================================
# the is done for you. Just create the regex pattern
import re
regex = re.compile(pattern)
match=regex.findall(text)
print('\nYou pattern found this match in the text: \n')
print('\t'+ str(match)+'\n')