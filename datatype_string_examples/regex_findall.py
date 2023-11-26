import re

text = "The quick brown fox"

pattern = r"brown"

search = re.search(pattern, text)

if search:
    print("Pattern is matching", search.group())
else:
   print("Pattern not found")


