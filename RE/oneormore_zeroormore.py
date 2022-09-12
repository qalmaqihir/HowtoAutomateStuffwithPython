import re
# Parenthesis helps us to define how many times a regex should be popped
# like using with [] it will reduce the code
### These are just a shortcut for braces
# cksajl
# Instead use [aeiou]{2}
# [aeiou]{1,} ==[aeiou]+ --> + =={1,}
# [aeiou]{0,} == [aeiou]* ---> *=={0,}
# .* ===> match 0 or more anything .* == [\s\S]*

text = "1, 10, 100 , 1000 "
pattern = "10*"

regex = re.compile(pattern)

all_matches=regex.findall(text)
print(all_matches)
print(text)