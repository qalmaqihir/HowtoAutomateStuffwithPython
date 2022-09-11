import re

text='121212141512'
text2='123 and we go now 132 again, 980'
pattern='\d' # maps to any single digits, for two digits use \d\d, similarly for more \d\d\d\d\d
pattern2='\d\d\d' # 3 digits
pattern3 = '\D\D\D\D' # inverse, => not digit
regex = re.compile(pattern3)

all_match=regex.findall(text2)

print(all_match)