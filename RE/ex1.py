'''
write a regex pattern that will match the word 'regex' in the text
make your pattern generate the same match as my pattern does
'''

#========================================Exercise======================================#
text = "I just wann regex the crap out of everything man."
pattern="regex"

#===============================================
# the is done for you. Just create the regex pattern
import re
regex = re.compile(pattern)
match=regex.findall(text)
print('\nYou pattern found this match in the text: \n')
print('\t'+ str(match)+'\n')