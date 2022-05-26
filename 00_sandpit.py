import re

# split the input into a list
a = str.split("opposite and adjacent")
# take out the 'and'
a.remove("and")

# check each item in the list to match with specific side, making true if
# comparison found
for item in a:
    if re.match("adjacent", item):
        print("hi")
        adjacent = True


# print to check adjacent true
print(adjacent)