import re
# we can specify the full control of what we want to extract from the text
# Nything inside () is group
text = "First Name: jawad, Last Name: Haider" # how to extract the name
text1="Full Name: jawad haider"


# pattern = "Name: \w+"
# pattern = "First Name: (\w+), Last Name: (\w+)"
# pattern1="Full Name: (.*)"
pattern1="Full Name: ((\w+)\s*(\w+))"
# pattern1="Full Name: ((.+)\s+(.+))"
# pattern3= "(IMG(\d+))\.png"

regex = re.compile(pattern1)

all_matches=regex.findall(text1)
search = regex.search(text1)

print(all_matches)
# print(text)
print(search.group())
print(search.group(1))
print(search.group(2))
print(search.group(3))
