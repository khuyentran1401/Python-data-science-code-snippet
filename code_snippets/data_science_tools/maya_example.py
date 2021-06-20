import maya

# Automatically parse datetime string
string = '2016-12-16 18:23:45.423992+00:00'
print(maya.parse(string).datetime())
# 2016-12-16 18:23:45.423992+00:00

print(maya.parse(string).datetime(to_timezone='US/Central'))
# 2016-12-16 12:23:45.423992-06:00