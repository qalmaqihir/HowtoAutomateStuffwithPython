import re
# White Spaces
# print(' .\t.\n.     .')
text = "The first line \nHere is the tabbed \t second line.."
pattern = "\S\S\S"

regex = re.compile(pattern)

all_matches=regex.findall(text)
print(all_matches)
print(text)