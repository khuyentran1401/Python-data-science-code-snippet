# pip install datefinder

from datefinder import find_dates

text = """"We have one meeting on May 17th,
2021 at 9:00am and another meeting on 5/18/2021
at 10:00. I hope you can attend one of the
meetings."""

matches = find_dates(text)

for match in matches:
    print("Date and time:", match)
    print("Only day:", match.day)

"""Output:
Date and time: 2021-05-17 09:00:00
Only day: 17
Date and time: 2021-05-18 10:00:00
Only day: 18
"""