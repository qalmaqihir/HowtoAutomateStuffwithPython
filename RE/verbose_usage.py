import re
# Using VERBOSE parameter of re

text="Hello1 Hello99 # AB.aaaaa"
pattern="""
        Hello       # static string match for Hello, with trailing white spaces ignored
        \d \d       # Any double digit with white spaces ignored
         \          # A single space, with the rest of the traling white space  ignored
         \#         #Checking for an actual # sign. Not starting a comment
         [abc ]     # macth a, b, c or a single space
         (?: A B)   # ignores the white space (checks for AB)
         \. $        # Line has to end with a period and (white space is ignored)       
         
"""
pattern1="""
        Hello\ # white space is ignored
        \d\d
"""
regex = re.compile(pattern, re.VERBOSE)

all_matches=regex.findall(text)
search = regex.search(text)
print(all_matches)
# print(text)
# print(search.group())
