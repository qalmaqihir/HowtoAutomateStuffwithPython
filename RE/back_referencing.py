import re
# Advanced referencing; Back referencing


text="ABC DEF DF DEF ABCE"
# pattern="ABC"
# pattern="(ABC) (ABC)"
# pattern="(ABC) DEF (ABC)"
pattern="(ABC) (DEF) DF \\2 \\1" # Back referencing


# (Doe)\w+\\1
# (\w+) (?:\w+\s+)+\\1

regex = re.compile(pattern)
all_match=regex.findall(text)
match=regex.search(text)
# print(all_match)
print(match.group())