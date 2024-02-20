import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)

if search :
    print("Pattern found: ", search.group())
else:
    print("Pattern not found")



text1 = "The quick brown fox"
pattern1 = r"The"
pattern2 = r"quick"


""" re.match will only look for start of the string
not the whole string use re.search for the whole string search
"""
match = re.match(pattern1, text1) 
if match:
    print("Match found: ",match.group())
else:
    print("No match")

match2 = re.match(pattern2, text1) 
if match2:
    print("Match found: ",match2.group())
else:
    print("No match") # no match is found because quick is not first word

text3 = "The quick brown fox jumps over the lazy brown dog"
pattern3 = "brown"

replacement = "red"

new_text = re.sub(pattern3,replacement,text3)
print("Modified text: ", new_text)



text4 = "The quick bown fox"
pattern4 = "brown"

search1 = re.search(pattern4, text4)
if search1:
    print("pattern found: ",search1.group())
else: 
    print("Pattern not found")


