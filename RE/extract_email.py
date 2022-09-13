import re
# Email extraction using all edge cases

text="this is my email: supine.me@gmail.com, this is second one " \
     "jawad@yahoo.org " \
     "jawad.ha-ider_2022@ucentra-_lasia.org"


# pattern="[\w\._\-]+\@\w+[\.\w\.]+"
# pattern="[a-zA-Z0-9_\.\-]+@[A-Za-z0-9\.\-]+[a-zA-Z]{2,}"
# pattern="[a-zA-Z0-9]+(?:(?:\.?\_?|\-?)[a-zA-Z0-9]+)+@[a-zA-Z0-9\.\-]+[a-zA-Z]{2,}"


# For VERBOSE
pattern="""
     [a-zA-Z0-9]+
   (?:
     (?:\.?\_?|\-?)
     [a-zA-Z0-9]+
   )+
   @
   [a-zA-Z0-9\.\-]+
   [a-zA-Z]{2,}
"""


# regex = re.compile(pattern)
regex = re.compile(pattern,re.VERBOSE)

all_matches=regex.findall(text)
search = regex.search(text)
print(all_matches)
print(text)
print(search.group())

