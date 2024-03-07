import re

lines = "   test  \n   tes, tttt , sss\n"
lines = re.sub(r'\s+', ' ', lines)
lines = lines.strip()
lines = lines.replace(" ,", ",")
lines = lines.replace(", ", ",")
print('"' + lines+ '"')
