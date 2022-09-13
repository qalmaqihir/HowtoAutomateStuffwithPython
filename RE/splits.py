import re
# Splits

# text="Apples, Carrots, Oranges, Graphs"
text="this sentences has vowles."
# l=text.split(', ')
# print(l)
# pattern=", "
# pattern="\s*,\s* "
pattern="[aeiou]"

regex = re.compile(pattern,re.VERBOSE)
# all_match=regex.findall(text)
all_match=regex.split(text)
print(all_match)