import re
# only if smth followed is matched
#
# text="ABCDFE"
# pattern="ABC(?=DF)"

text="I am Issac Asimov and he is Issac Johnper"
# pattern="Issac (?=Asimov)"

# text="ABCFE"
# pattern="ABC(?!DF)"

# text="ABCDEF"
# pattern="(?<=BC)DEF"
pattern="(?<=Issac )\w+"

"""
Used patterns
(?=) (?!) (?<=)(?<!)
"""

regex = re.compile(pattern)
all_match=regex.findall(text)
print(all_match)