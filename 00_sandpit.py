import re

a = str.split("another one")
print(a)



a = "opposite and adjacent"

regex = "opposite"

if re.match(regex, a):
    a = str.split(a)
    a.remove("and")
print(a)