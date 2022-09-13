import re
# Splits

#
# text="this sentences has vowles."
# pattern="[aeiou]"

# text="7 plus 7 is fourteen"
# pattern="7"
text="My number is 123-213-4358 your number is 435-234-3123"
pattern="\d{3}-\d{3}-\d{4}"


regex = re.compile(pattern,re.VERBOSE)
# all_match=regex.findall(text)
# all_match=regex.split(text)
# all_match = regex.sub("Vv",text)
# all_match = regex.sub("seven",text)

all_match = regex.sub("hiddenNumber",text)
print(all_match)