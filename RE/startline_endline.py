import re
# find matches that are only in the start or end of  a word
# \\b

text = "This is writtenT twice. This is written twice."

pattern = "\\bT"
# pattern = "T\\b"
regex = re.compile(pattern)

all_matches=regex.findall(text)
searched=regex.search(pattern)
print(searched)
print(all_matches)
print(text)