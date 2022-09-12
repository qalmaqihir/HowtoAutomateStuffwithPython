import re
# wild card
text = "text 1234 .>>.. .... !@# ()*&% ^%&# JK lad I _+08 \t \t\n\n .  sdf     "
pattern = "\.\."
# . matches everything
# \.\.\.matches special .
# .^ $ * + ? > () {} <> [] --. these are specail charachters and need a \
# like below
pattern2="\. \^ \$ ........."
text2="these . specail characters need \ to be found . ^ $ + - * > < ( {][})"

regex = re.compile(pattern2)

all_matches=regex.findall(text2)
print(all_matches)
print(text2)