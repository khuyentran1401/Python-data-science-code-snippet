import re

text = 'Today is 3/7/2021'
match_pattern = r'(\d+)/(\d+)/(\d+)'

print(re.sub(match_pattern, 'Sunday', text))
# Today is Sunday

print(re.sub(match_pattern, r'\3-\1-\2', text))
# Today is 2021-3-7