import re
# Barakets, explicitly typing out exactly what we need, instead of the boilerpates
# Tells what to pop up


text = " 0there is a man12, 293 484 with^0 a98(09) 92034 heart0-= 801 02 and 14H"
pattern = "[^a-zA-Z0-9 ]" # [inthing inside is the option],
# \w == [a-zA-Z0-9]
# - for range of values  [0-9] == \d ([0-9][0-9][0-9]==\d\d\d)
# [^0-9] == \D not digit
# [^-zA-Z]
#[aeiou][aeiou] two vowels
# [1234567890] == \d
# a-z-Z == [abced...xyz]

regex = re.compile(pattern)

all_matches=regex.findall(text)
print(all_matches)
print(text)