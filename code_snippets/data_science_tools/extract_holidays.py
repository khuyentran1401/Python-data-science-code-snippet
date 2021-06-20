# pip install holidays
from datetime import date 
import holidays

us_holidays = holidays.UnitedStates()

print('2014-07-04' in us_holidays)
# True

print(us_holidays.get('2014-7-4'))
# Independence Day

print(us_holidays.get('2014/7/4'))
# Independence Day
