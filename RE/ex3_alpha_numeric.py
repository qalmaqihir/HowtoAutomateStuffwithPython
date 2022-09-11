'''
Write a regex pattern that will match any four alphanumic, followed by a
non alphanumic.
'''


#========================================Exercise======================================#
text = "Yo! How are you doin? I just made $1000"

pattern="\w\w\w\w\W"

#===============================================
# the is done for you. Just create the regex pattern
import re
regex = re.compile(pattern)
match=regex.findall(text)
print('\nYou pattern found this match in the text: \n')
print('\t'+ str(match)+'\n')