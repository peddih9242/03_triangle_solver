import re

yes = input("what")
# split the input into a list
a = str.split(yes)
# take out the 'and'
if "and" in a:
    a.remove("and")
print(a)
# check each item in the list to match with specific side, making true if
# comparison found
for item in a:
    if re.match("adjacent", item):
        print("hi")
        adjacent = True


# print to check adjacent true
print(adjacent)