import re

text = "Hello, this is some text. Hello"
pattern="Hello"

regex= re.compile(pattern)
# print(regex)

match=regex.search(text)
print(match)
print(match.group())
print(match.start())
print(match.end())
print(match.span())

# For the second instance we use
all_matches = regex.findall(text)
print(all_matches)