import re
# Alpha Numeric

text = "abcd10947XYZ-9-1+3 % -$"
pattern = "\w"

text1 = " @%^  ( ) 123 cat  -+ dog run away 840"
pattern1 = "\w\w"
pattern2 = "\W" #Non- alphaNumrics

regex = re.compile(pattern2)

all_matches=regex.findall(text)
print(all_matches)
