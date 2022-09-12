import re
# Determine if something is optional, yes or no 0 or 1
# ?
# 1,?000 === 1000 with or without a comma

text = "1 , 1, 10, 100 , 1,000, 1,000,000, 100,00, 100 , "
pattern = "1,?0"

regex = re.compile(pattern)

all_matches=regex.findall(text)
print(all_matches)
print(text)