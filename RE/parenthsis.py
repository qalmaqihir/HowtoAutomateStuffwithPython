import re
# Parenthesis helps us to define how many time a regex should be popped
# like using with [] it will reduce the code

#[aeiou][aeiou] two vowels
# Instead use [aeiou]{2}
# [aeiou]{2,4}
# [aeiou]{2,}
# [aeiou]{,6}
# raange can be also defined [aeiou]{2,4}
#Yo!{3,}    
# print(' .\t.\n.     .')
text = "I am grooot. Youuuoooou are you"
pattern = "[aeiou]{,3}"

regex = re.compile(pattern)

all_matches=regex.findall(text)
print(all_matches)
print(text)