import re
# (|)  match either x | y
# text = "apple banana orangeS" # how to extract the name
text="I like cats" \
     "I like dogs" \
     "I like bats" \
     "I like hogs"

# pattern="(apples?|banana|orangeS?)"
# pattern="(I like (cats|dogs?|bats))"
# pattern="I like (cats|dogs?|bats)"
# pattern="(I like (?:cats|dogs?|bats|hogs))"
pattern="(I like (?:[cb]ats?|[dg]ogs?))"
# different from (a|b) != [ab] or (apple|banana) != [applebanana]


regex = re.compile(pattern)


all_matches=regex.findall(text)
search = regex.search(text)
print(all_matches)
print(text)
print(search.group())

